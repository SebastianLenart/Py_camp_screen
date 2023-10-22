import pytesseract


pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

path_to_image = "C:\\GitHub\\Py_camp_screen\\knowledge\\google.png"
custom_config = r'--oem 3 --psm 6'
print(pytesseract.image_to_string(path_to_image, config=custom_config, lang="eng")) # działa słabooo









































