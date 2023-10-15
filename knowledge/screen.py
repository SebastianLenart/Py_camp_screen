import pyautogui

pyautogui.screenshot("screenshot.png")
for button in pyautogui.locateAllOnScreen("C://GitHub//Py_camp_screen//target//check.png", confidence=0.5):
    print(button, button[0])
    # click_it = pyautogui.center(button)
    # print(click_it)
