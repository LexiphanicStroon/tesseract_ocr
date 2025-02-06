import pytesseract
from pdf2image import convert_from_path
import os

# Set paths
input_dir = "data/input/"  # Directory containing PDF files
output_text_dir = "data/output/"  # Directory to save text files
output_image_dir = "data/output/images/"  # Directory to save images

# Create output directories if they don't exist
os.makedirs(output_text_dir, exist_ok=True)
os.makedirs(output_image_dir, exist_ok=True)

# Iterate over all PDF files in the input directory
for pdf_file in os.listdir(input_dir):
    if pdf_file.endswith(".pdf"):
        input_path = os.path.join(input_dir, pdf_file)
        base_name = os.path.splitext(pdf_file)[0]  # File name without extension
        output_text_path = os.path.join(output_text_dir, f"{base_name}.txt")

        # Convert PDF to images
        images = convert_from_path(input_path)

        # Extract text from each page
        extracted_text = ""
        for i, image in enumerate(images):
            # Save each image
            image_path = os.path.join(output_image_dir, f"{base_name}_page_{i + 1}.png")
            image.save(image_path, "PNG")

            # Extract text from the image
            text = pytesseract.image_to_string(image)
            extracted_text += f"--- Page {i + 1} ---\n{text}\n"

        # Save extracted text to a file
        with open(output_text_path, "w") as f:
            f.write(extracted_text)

        print(f"OCR completed for {pdf_file}. Text saved to {output_text_path}")
        print(f"Images saved to {output_image_dir}")
