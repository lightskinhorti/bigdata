import pytesseract
from PIL import Image

archivo = Image.open("jpg/Texto.png")
print(pytesseract.image_to_string(archivo))