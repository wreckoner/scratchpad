import pytesseract
from pdf2image import convert_from_path
import argparse
import os
import sys

# --- OPTIONAL: TESSERACT PATH ---
# If you get a 'TesseractNotFoundError', uncomment the line below and 
# point it to your tesseract.exe (usually in Program Files)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def validate_pdf(file_path):
    """Checks if the provided file path exists and ends with .pdf."""
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return False
    if not file_path.lower().endswith('.pdf'):
        print(f"Error: The file '{file_path}' is not a valid PDF (missing .pdf extension).")
        return False
    return True

def extract_text_from_scanned_pdf(input_path, output_path, poppler_path=None):
    """Extracts text from a scanned PDF using OCR and saves it to a .txt file."""
    try:
        # If poppler_path is provided, pass it to convert_from_path
        print(f"Processing {input_path}...")
        
        # Convert PDF pages to images for the OCR engine
        pages = convert_from_path(input_path, dpi=300, poppler_path=poppler_path)
        
        full_text = ""

        for i, page in enumerate(pages):
            # Perform OCR on each image page
            page_text = pytesseract.image_to_string(page)
            
            if page_text.strip():
                full_text += f"--- Page {i+1} ---\n"
                full_text += page_text + "\n\n"

        # Write the result to text file
        with open(output_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(full_text)
            
        print(f"Success! Extracted text saved to: {output_path}")

    except Exception as e:
        print(f"An error occurred during processing: {e}")
        if "poppler" in str(e).lower():
            print("\nTip: If you see a Poppler error, ensure the path provided with -p is correct.")

def main():
    parser = argparse.ArgumentParser(description="Extract text from scanned PDF files using OCR.")
    
    # Required arguments
    parser.add_argument("-i", "--input", required=True, help="Path to the input scanned PDF file")
    parser.add_argument("-o", "--output", required=True, help="Path for the output .txt file")
    
    # Optional argument for Poppler path (useful for Windows users)
    parser.add_argument("-p", "--poppler", help="Optional: Path to the poppler bin folder (e.g., C:\\poppler\\bin)")

    args = parser.parse_args()

    if not validate_pdf(args.input):
        sys.exit(1)

    # Run extraction passing the optional poppler path if it was provided
    extract_text_from_scanned_pdf(args.input, args.output, args.poppler)

if __name__ == "__main__":
    main()
