# Tesseract OCR MVP

This project demonstrates a minimal OCR pipeline using Tesseract OCR to process images or PDFs and extract text.

## Example Outputs

This repository includes example outputs for demonstration purposes:

- Extracted text: `data/output/output.txt`
- Converted images: `data/output/images/`

You can view these outputs without setting up the environment to get an idea of the results achieved using a lightly modified version of OCR.


## Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd tesseract-ocr-mvp
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install pytesseract pdf2image
   sudo apt install tesseract-ocr  # Install Tesseract
   ```

3. Add your input file (PDF or image) to the `data/input/` folder.

## Usage

Run the OCR script:

   ```bash
   python3 scripts/ocr_tesseract.py
   ```

The extracted text will be saved to `data/output/output.txt`.

## Project Structure

```text
tesseract-ocr-mvp/
├── data/
│   ├── input/                # Input files (e.g., PDFs or images)
│   ├── output/               # Extracted text files
├── scripts/                  # Python scripts for OCR
│   └── ocr_tesseract.py      # Main script for Tesseract OCR
├── README.md                 # Project instructions
├── .gitignore                # Ignored files for GitHub
```

## Notes

- Ensure that `tesseract-ocr` is installed on your system. You can verify it by running:

   ```bash
   tesseract --version
   ```

- If you face issues with missing dependencies, ensure the following system packages are installed:

   ```bash
   sudo apt update
   sudo apt install libtesseract-dev libleptonica-dev
   ```
