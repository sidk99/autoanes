# AutoAnes Codebase

## PMC Text Extractor

A script  for fetching and extracting text content from articles available in the PubMed Central (PMC) repository. Users need to provide a CSV file containing a list of PMC IDs without column headers. The extracted text content for each article is saved in a separate text file named by its PMC ID.

### Instructions

#### 1. **Preparing Your CSV File**

   - Create a CSV file containing PMC IDs you wish to extract text from.
   - Ensure the CSV doesn’t have a header, and PMC IDs are populated in the first column.

#### 2. **Configuring the Script**

   - Open the `PMC Text Extractor` script.
   - 1) Find the line: 
     ```python
     csv_filename = "your_file.csv"
     ```
   - Replace `"your_file.csv"` with the path and name of your CSV file containing the PMC IDs.
   - 2) Find the line: 
     ```python
     PATH_PREFIX = "/PATH/TO/OUTPUT/FOLDER"

     ```
   - Replace with the path of folder where you want to save text output for each paper.

#### 3. **Running the Script**

   - Setup Python enviroment with 
   ```pip install -r requirements.txt```
   - Run the script in a Python environment. 
   ```python pdf_text_extractor.py```
### Output

- Each output `.txt` file will contain the extracted text content of the corresponding PMC article.
- The file will be named using the PMC ID, TBD: store mapping of ID to name or other readable tag

