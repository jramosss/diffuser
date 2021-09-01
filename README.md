# <center>Whatsapp Diffuser

## Why?:

I wanted to send the same message to many people _(not spamming i swear, please do not use this program to spam)_ that i didnt have registered in my phone contacts, so instead of saving the number one by one and sending the message, i decided to take 2 hours to do the same task but slower, **because once i read**  
![Life saving phrase](https://preview.redd.it/2ialma4xoiv41.jpg?auto=webp&s=85416fd4fc3a4c12394763d4f40708f4e4287b96)

## How?:

Well, in the weird case that you want to do the same as me, follow these steps:

- Make sure to be logged in your whatsapp web account
- `$ python3 -m venv venv; source venv/bin/activate; pip install -r requirements.txt`
- Create a file named people.py and write a list with all the numbers (as strings) of the people you want to send the message to.
- Set the message variable in the main function to the message you want to send
- Run the script using `python main.py`
- Open your browser and click on it

Also, its very possible that the script will click in the wrong place when trying to send the message, so make sure to set the x and y in main.py line 19 to your writing bar in whatsapp web (I wont do a generic version in future commits, sorry).

## FAQ:

(Im lying, at the time im writing this im the only person that used this program).

### Can i get banned for using this?:

Dunno, let me know.

### Why didn`t you use twilio?:

People would have received the message from twilio, then think "who is this?" **block**

### Why does it take so much time?:

I made it in less than 2 hours please don`t ask that much from me.
