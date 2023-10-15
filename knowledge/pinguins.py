from os import walk, path
import pyautogui

# pyautogui.screenshot("screenshot.png")


source = path.join("C:\\GitHub\\Py_camp_screen\\target\\pinguins")
for (dirpath, dirnames, filenames) in walk(source):
    # print(dirpath, dirnames, filenames)
    for filename in filenames:
        # print(path.join(source, filename))
        if pyautogui.locateOnScreen(path.join(source, filename), confidence=0.7) is not None:
            print(filename)
