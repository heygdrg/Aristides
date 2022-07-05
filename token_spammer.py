import time
import requests
from requests import post
import json
import pystyle
from pystyle import *

System.Size(150, 47)

def imoprts(modules: str) -> None:
    for module in modules.split(' '):
        globals()[module] = __import__(module)
imoprts('requests os pystyle')
banner1 = """











▄▄▌ ▐ ▄▌ ▄▄▄·    .▄▄ ·  ▄▄▄· ▄▄▄· • ▌ ▄ ·. • ▌ ▄ ·. ▄▄▄ .▄▄▄  
██· █▌▐█▐█ ▄█    ▐█ ▀. ▐█ ▄█▐█ ▀█ ·██ ▐███▪·██ ▐███▪▀▄.▀·▀▄ █·
██▪▐█▐▐▌ ██▀·    ▄▀▀▀█▄ ██▀·▄█▀▀█ ▐█ ▌▐▌▐█·▐█ ▌▐▌▐█·▐▀▀▪▄▐▀▀▄ 
▐█▌██▐█▌▐█▪·•    ▐█▄▪▐█▐█▪·•▐█ ▪▐▌██ ██▌▐█▌██ ██▌▐█▌▐█▄▄▌▐█•█▌
 ▀▀▀▀ ▀▪.▀        ▀▀▀▀ .▀    ▀  ▀ ▀▀  █▪▀▀▀▀▀  █▪▀▀▀ ▀▀▀ .▀  ▀

"""
banner2 = """


          .'''''.        ..||..'''''''...
         / ##### \       : ||            ''.
        | ## # ## |      :.||...''''''....  '.
        | #  #  # |        ||             ''''
        | ####### |     .  ||
         \ ##### /     /| < _>
          \ ### /     / |/ < _>
        ..''   ''... /  |  < _>
      .'            /   | /||
      '                 |/ ||
      |   |     '..     |  ||
      |   |     |  '...''  ||
      |  |       |         ||
       \ |       |         ||
       |\|       |         ||
       \|         |        ||
        |         |        ||
        |         |        ||
       |           |       ||
     __|           |__     ||
    /   '.........'   \    ||
     ''''''     ''''''     ##
"""
banner = Add.Add(banner1, banner2)

print(Colorate.Vertical(Colors.green_to_yellow, Center.XCenter(banner + '\n\n')))

token = Write.Input("[?] enter the token ->", Colors.green_to_yellow, interval=0.005)
print()

endpoint = Write.Input("[?] enter the endpoint of the conversation ->", Colors.green_to_yellow, interval=0.005)

content_message = Write.Input("[?] what you wanna say ->", Colors.green_to_yellow, interval=0.005)
print()
number = int(Write.Input("[?] how many time you want to repeat the message ->", Colors.green_to_yellow, interval=0.005))
print()

for i in range(number):
    message = content_message

    post(endpoint, json={'content': message}, headers={'Authorization': token})
    number = Write.Print("[!] Message sent from the token \n", Colors.green_to_yellow, interval=0.005)

print()
Write.Input("The message succesfully sent from the token", Colors.green_to_yellow, interval=0.005)