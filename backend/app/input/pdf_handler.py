import fitz
from PIL import Image
import io

def pdf_to_image(file):
    pdf = fitz.open(stream=file.read(), filetype="pdf")
    images = []

    for page in pdf:
        pix = page.get_pixmap()
        img_bytes = pix.tobytes("png")
        image = Image.open(io.BytesIO(img_bytes))
        images.append(image)
    
    return images   