import requests
from xml.etree import ElementTree as ET
import os 
import csv
import pandas as pd

PATH_PREFIX = "/Users/sidkaus/Desktop/projects/scripts/paper_texts"

def get_pmc_text(pmc_id):
    base_url = f"https://www.ncbi.nlm.nih.gov/pmc/oai/oai.cgi"
    params = {
        "verb": "GetRecord",
        "identifier": f"oai:pubmedcentral.nih.gov:{pmc_id}",
        "metadataPrefix": "pmc"
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch the text from PMC. Status code: {response.status_code}")
        return None

def parse_xml(xml_text, pmc_id):
    root = ET.fromstring(xml_text)
    
    # Define the namespace
    ns = {'pmc': 'https://jats.nlm.nih.gov/ns/archiving/1.3/'}
    
    # Function to extract and concatenate text recursively
    def recursive_text_extraction(element):
        text = element.text or ""
        for child in element:
            text += recursive_text_extraction(child)
            if child.tail:
                text += child.tail
        return text
    
    # Extract text content from <p> tags within the <body> tag
    paragraphs = []
    for body in root.iter("{https://jats.nlm.nih.gov/ns/archiving/1.3/}body"):
        for p in body.iter("{https://jats.nlm.nih.gov/ns/archiving/1.3/}p"):
            paragraph_text = recursive_text_extraction(p)
            paragraphs.append(paragraph_text)
    
    # Save the text into a file
    import pdb; pdb.set_trace()
    with open(os.path.join(PATH_PREFIX, f"{pmc_id}.txt"), "w") as file:
        for paragraph in paragraphs:
            file.write(paragraph + "\n\n")

def process_pmc_ids(csv_filename):
    df = pd.read_csv(csv_filename, header=None)
    import pdb; pdb.set_trace()
    for index, row in df.iterrows():
        import pdb; pdb.set_trace()
        pmc_id = row[0]  # assuming pmc_id is in the first column
        print(f"Processing PMC ID: {pmc_id}")
        
        xml_text = get_pmc_text(str(pmc_id))
        if xml_text:
            parse_xml(xml_text, str(pmc_id))

# Specify the name of your CSV file here
csv_filename = "sample_pmc_id.csv"
process_pmc_ids(csv_filename)

