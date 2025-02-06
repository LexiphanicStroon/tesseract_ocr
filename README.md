# Tesseract OCR

This project demonstrates a minimal OCR pipeline using Tesseract OCR to process images or PDFs and extract text.

## Example Outputs

This repository includes example outputs for demonstration purposes:

- Extracted text: `data/output/` (e.g., `output.txt` or individual PDF text files)
- Converted images: `data/output/images/`

You can view these outputs without setting up the environment to get an idea of the results.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/LexiphanicStroon/tesseract_ocr/edit/main/README.md
   cd tesseract-ocr-mvp
   ```

2. Install Python and required system packages:

   ```bash
   sudo apt update
   sudo apt install python3 python3-venv python3-pip libtesseract-dev libleptonica-dev tesseract-ocr poppler-utils
   ```

3. Create a virtual environment and install dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install pytesseract pdf2image
   ```

4. Add your input file(s) (PDF or image) to the `data/input/` folder.

## Usage

### Process a Single File
Run the `ocr_tesseract.py` script to process one file:
   ```bash
   python3 scripts/ocr_tesseract.py
   ```
The extracted text will be saved to `data/output/output.txt`.

### Process Multiple Files
Run the `process_multiple_pdfs.py` script to process all PDFs in the `data/input/` directory:
   ```bash
   python3 scripts/process_multiple_pdfs.py
   ```
The extracted text will be saved as separate `.txt` files in `data/output/`.

## Project Structure

```text
tesseract-ocr-mvp/
├── data/
│   ├── input/                # Input files (e.g., PDFs or images)
│   ├── output/               # Extracted text files and images
│       ├── images/           # Generated images from PDF files
├── scripts/                  # Python scripts for OCR
│   ├── ocr_tesseract.py      # Script to process a single file
│   ├── process_multiple_pdfs.py  # Script to process all PDFs in input/
├── README.md                 # Project instructions
├── .gitignore                # Ignored files for GitHub
```

## Notes

- Ensure that `tesseract-ocr` and `poppler-utils` are installed on your system. You can verify it by running:

   ```bash
   tesseract --version
   pdfinfo --version
   ```

- If you face issues with missing dependencies or packages, run the following:

   ```bash
   sudo apt update
   sudo apt --fix-missing install
   ```

