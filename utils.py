from datetime import datetime
from platform import system
from pyautogui import hotkey,press
from time import sleep

def timePrint (msg):
    now = datetime.now().time()
    print(now,msg)

def close_tab(wait_time: int = 3) -> None:
    sleep(wait_time)
    if system().lower() in ("windows", "linux"):
        hotkey("ctrl", "w")
    elif system().lower() in "darwin":
        hotkey("command", "w")
    else:
        raise Warning(f"{system().lower()} not supported!")
    press("enter")