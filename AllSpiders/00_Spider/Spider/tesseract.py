# coding=utf-8

import pytesseract
from PIL import Image

image = Image.open('./images/1233.png')
text = pytesseract.image_to_string(image,lang="chi_sim")
print text