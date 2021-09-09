from time import sleep
from pyautogui import press,click
from webbrowser import open
from urllib.parse import quote
from termcolor import colored
from people import people
from utils import *

# Function stolen (but adapted) from pywhatkit https://github.com/Ankit404butfound/PyWhatKit
def instantmsg(phone_no: str, message: str,lastmsg : bool) -> None:
    parsed_message = quote(message)
    open('https://web.whatsapp.com/send?phone=' +
                phone_no + '&text=' + parsed_message,new=0)
    sleep(12)
    #!Pretty adapted to my screen hehe sorry
    click(x=4229, y=1612)
    press('enter')
    if not lastmsg:
        timePrint(colored("Waiting to go again...",'yellow'))
        sleep(1)
        close_tab()


def sendAndLog (to,msg,lastmsg):
    timePrint(colored( "Scheduling " + msg + " to " + to,'white'))
    instantmsg(to,msg,lastmsg)
    timePrint(colored("Sent " + msg + " to " + to,'green'))


def main ():
    from message import message
    print(colored("You have 4 seconds to open your browser!",'magenta'))
    sleep(4)
    for i in range(0,len(people)):
        sendAndLog(people[i],message,i == len(people) - 1)

    print(colored("Done!, sent message to " + str(len(people)) + ' numbers','green'))

if __name__ == '__main__':
    main()