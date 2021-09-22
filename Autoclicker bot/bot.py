import pyautogui
import time
import keyboard
import win32api
import win32con

# Tile 1 Position: X:  877 Y:  411 RGB: (184, 188, 235)
# Tile 2 Position: X:  767 Y:  404 RGB: (179, 182, 235)
# Tile 3 Position: X:  686 Y:  402 RGB: (0, 0, 0)
# Tile 4 Position: X:  586 Y:  399 RGB: (175, 179, 234)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)    # This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while not keyboard.is_pressed('q'):

    if pyautogui.pixel(877, 411)[0] == 0:
        click(877, 411)
    if pyautogui.pixel(767, 404)[0] == 0:
        click(767, 404)
    if pyautogui.pixel(686, 402)[0] == 0:
        click(686, 402)
    if pyautogui.pixel(586, 399)[0] == 0:
        click(586, 399)
