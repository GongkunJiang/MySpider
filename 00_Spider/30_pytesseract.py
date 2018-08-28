# coding=utf-8
import pytesseract
from PIL import Image
import subprocess

def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)

    # 对图片进行阈值过滤,然后保存
    image = image.point(lambda x: 0 if x<143 else 255)
    image.save(newFilePath)

    # 调用系统的tesseract命令对图片进行OCR识别
    subprocess.call(["tesseract", newFilePath, "30_output"])

    # 打开文件读取结果
    file = open("30_output.txt", 'r')
    print(file.read())
    file.close()
# cleanFile("30_tess2.jpg", "30_text2clean.png")
cleanFile("25_db_code.jpg", "25_db_codeclean.png")
# image = Image.open('30_tesseracttest.jpg')
# text = pytesseract.image_to_string(image)
# print text
# print pytesseract.image_to_string(Image.open('26_ph_code.jpg'))
# print pytesseract.image_to_string(Image.open('25_db_code.jpg'))
# print pytesseract.image_to_string(Image.open('30_text2clean.png'))