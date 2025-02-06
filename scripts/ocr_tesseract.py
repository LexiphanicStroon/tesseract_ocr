import pytesseract
from pdf2image import convert_from_path
import os

# Set paths
input_path = "data/input/1159013261.pdf"  # Update this to match your PDF file name
output_text_path = "data/output/output.txt"
output_image_dir = "data/output/images/"

# Create output directories if they don't exist
os.makedirs(output_image_dir, exist_ok=True)

# Convert PDF to images
images = convert_from_path(input_path)

# Extract text from each page
extracted_text = ""
for i, image in enumerate(images):
    # Save each image
    image_path = os.path.join(output_image_dir, f"page_{i + 1}.png")
    image.save(image_path, "PNG")

    # Extract text from the image
    text = pytesseract.image_to_string(image)
    extracted_text += f"--- Page {i + 1} ---\n{text}\n"

# Save extracted text to a file
with open(output_text_path, "w") as f:
    f.write(extracted_text)

print(f"OCR completed. Text saved to {output_text_path}")
print(f"Images saved to {output_image_dir}")
