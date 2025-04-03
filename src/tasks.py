import pyautogui

def perform_task(task_name):
    if task_name == 'screenshot':
        return pyautogui.screenshot()
    elif task_name == 'mouse_move':
        pyautogui.moveTo(100, 200, duration=2)