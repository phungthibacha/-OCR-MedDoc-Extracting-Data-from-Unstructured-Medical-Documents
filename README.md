# Medical Data Extraction from Prescription and Patient Details Documents

This project automates the extraction of essential information from medical documents, including prescriptions and patient details, using Python and computer vision techniques.

## Key Features:
- Seamlessly extracts key data points: Patient names, addresses, prescriptions, medications, dosages, refills, medical problems, vaccinations, and more.
- Handles various document types: Works with both PDFs and images of documents.
- Structures extracted data for further analysis: Organizes extracted information into JSON format for easy integration with other systems.
- Provides clear step-by-step documentation: The "Project: Prescription Document and Patient Details Document Extraction.ipynb" notebook offers a detailed walkthrough of the process.
- Offers a modular and reusable code structure: Uses Python classes for efficient code organization and potential extensions to other document types.

## Solution: Build a Python script to:
- Convert PDFs to images for easier text extraction.
- Preprocess images to improve text clarity with OpenCV.
- Extract text using Pytesseract OCR library.
- Structure extracted data into JSON format with Regular Expressions.

## Getting Started:
Install dependencies:
Bash
pip install -r requirements.txt

## Explore the project:
- Review the code in extractor.ipynb to understand the extraction process.
- Navigate through the data directory to view sample images.
- Refer to parser_generic.py for the class definitions used in the extraction process.
  
## Within the notebook, follow the instructions to:
- Load a PDF or image document.
- Specify the document type (prescription or patient details).
- Execute the extraction process.
- View the extracted data in a structured JSON format.
  
## Benefits:
- Automate medical record data entry: Saves time and resources for healthcare personnel.
- Improves data accuracy: Reduces errors from manual transcription.
- Enhances data accessibility: Structured data format facilitates analysis and integration.
  
## Future Work:
- Enhance accuracy with advanced OCR tools and machine learning techniques.
- Integrate with medical record systems for seamless data transfer.
  
## Contact:
For any inquiries or feedback, please contact Ha at phungthibacha@gmail.com.
