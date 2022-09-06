import cv2 as cv
import numpy as np
import pyautogui
import pydirectinput
import time
from win32gui import FindWindow, GetWindowRect, GetWindowText, GetForegroundWindow

window = FindWindow(None, "Tower of Fantasy  ")
approve_img = cv.imread('approve.PNG', 0)
template = cv.imread('frontier.PNG', 0)
jump_img = cv.imread('jump.PNG', 0)
box_img = cv.imread('box.PNG', 0)
end_img = cv.imread('end.PNG', 0)
fail_img = cv.imread('fail.PNG', 0)
percent = 0.7

def click(temp, x, y):
    pydirectinput.keyDown('alt')
    pyautogui.moveTo(temp[0]+x, temp[1]+y)
    pydirectinput.click()
    pydirectinput.keyUp('alt')

while(True):
    flag=False
    if(GetWindowText(GetForegroundWindow())!='Tower of Fantasy  '):
        continue
    time.sleep(1)
    window_rect = GetWindowRect(window)
    click(window_rect, 1140, 60)
    time.sleep(1)
    click(window_rect, 150, 410)
    time.sleep(1)

    try:
        screenshot = pyautogui.screenshot(region=(window_rect[0],window_rect[1],1296,759))
    except:
        continue
    open_cv_image = np.array(screenshot)
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    img_gray = cv.cvtColor(open_cv_image, cv.COLOR_BGR2GRAY)
    res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
    loc = np.where(res >= percent)
    if (np.size(loc)>0):
        click(window_rect, loc[1][0] + 36, loc[0][0] + 380)
    else:
        pyautogui.moveTo(window_rect[0] + 1000, window_rect[1] + 400)
        pyautogui.mouseDown()
        pyautogui.move(-200, 0, duration=1)
        pyautogui.mouseUp()
        click(window_rect, 1025, 575)
    time.sleep(1.5)
    click(window_rect, 1025, 575)
    time.sleep(1.5)
    click(window_rect, 825, 400)
    while (True):
        time.sleep(3)
        screen = pyautogui.screenshot(region=(window_rect[0], window_rect[1], 1296, 759))
        open_cv_img = np.array(screen)
        open_cv_img = open_cv_img[:, :, ::-1].copy()
        img_gray = cv.cvtColor(open_cv_img, cv.COLOR_BGR2GRAY)
        result_appr = cv.matchTemplate(img_gray, approve_img, cv.TM_CCOEFF_NORMED)
        result_jump = cv.matchTemplate(img_gray, jump_img, cv.TM_CCOEFF_NORMED)
        loc1 = np.where(result_appr >= percent)
        loc2 = np.where(result_jump >= percent)
        if (np.size(loc2) > 0):
            break
        elif (np.size(loc1) > 0):
            click(window_rect, 580, 610)
            click(window_rect, 750, 520)
    time.sleep(10)
    count = 0
    while (True):
        time.sleep(1)
        screen = pyautogui.screenshot(region=(window_rect[0], window_rect[1], 1296, 759))
        open_cv_img = np.array(screen)
        open_cv_img = open_cv_img[:, :, ::-1].copy()
        img_gray = cv.cvtColor(open_cv_img, cv.COLOR_BGR2GRAY)
        result_box = cv.matchTemplate(img_gray, box_img, cv.TM_CCOEFF_NORMED)
        loc3 = np.where(result_box >= percent)
        if (np.size(loc3) > 0):
            count += 1
        if (count>=10):
            click(window_rect, 775, 645)
            break
    time.sleep(60)
    for i in range(0, 60):
        time.sleep(1)
        screen = pyautogui.screenshot(region=(window_rect[0], window_rect[1], 1296, 759))
        open_cv_img = np.array(screen)
        open_cv_img = open_cv_img[:, :, ::-1].copy()
        img_gray = cv.cvtColor(open_cv_img, cv.COLOR_BGR2GRAY)
        result_fail = cv.matchTemplate(img_gray, fail_img, cv.TM_CCOEFF_NORMED)
        locFail = np.where(result_fail >= percent)
        if (np.size(locFail) > 0):
            click(window_rect, 640, 650)
            flag = True
            break
    if (flag):
        time.sleep(90)
        continue
    time.sleep(180)
    while (True):
        time.sleep(1.5)
        screen = pyautogui.screenshot(region=(window_rect[0], window_rect[1], 1296, 759))
        open_cv_img = np.array(screen)
        open_cv_img = open_cv_img[:, :, ::-1].copy()
        img_gray = cv.cvtColor(open_cv_img, cv.COLOR_BGR2GRAY)
        result_end = cv.matchTemplate(img_gray, end_img, cv.TM_CCOEFF_NORMED)
        loc4 = np.where(result_end >= percent)
        if (np.size(loc4) > 0):
            click(window_rect, 640, 650)
            time.sleep(1)
            click(window_rect, 640, 650)
            time.sleep(1)
            click(window_rect, 640, 650)
            time.sleep(1)
            click(window_rect, 175, 75)
            time.sleep(1)
            click(window_rect, 831, 411)
            time.sleep(30)
            break