from app.vision.preprocess import preprocess_image
from app.ocr.extractor import extract_text
from app.input.pdf_handler import pdf_to_image

def process_file(file):
    file.stream.seek(0)

    if file.filename.lower().endswith(".pdf"):
        images = pdf_to_image(file)
        full_text = ""
        
        for image in images:
            text = extract_text(image)
            full_text += text + "\n"
        
        return full_text
    
    image = preprocess_image(file)
    return extract_text(image)