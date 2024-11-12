import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()


# FOR CODES

API_ID = int(getenv("API_ID", "25206101" )) 
API_HASH = getenv("API_HASH", "2135724a8fdecb737f31d22ec8e6894b" ) 
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7919159999" ).split()))
LOGGER = int(getenv("LOGGER", None)) 
OWNER = int(getenv("OWNER_ID", "6062173301" )) 
NAME = getenv("ALIVE_NAME")
OWN_USERNAME= getenv("OWN_USERNAME")
ALIVE_PIC = getenv("ALIVE_PIC") 

# FOR SPAMBOT

TOKEN1 = getenv("TOKEN1", "7759714753:AAFbvUfyUOWiPsB_uoymbf5DYlCADCuIZJo" None) 
TOKEN2 = getenv("TOKEN2", None) 
TOKEN3 = getenv("TOKEN3", None) 
TOKEN4 = getenv("TOKEN4", None) 
TOKEN5 = getenv("TOKEN5", None) 
TOKEN6 = getenv("TOKEN6", None) 
TOKEN7 = getenv("TOKEN7", None) 
TOKEN8 = getenv("TOKEN8", None) 
TOKEN9 = getenv("TOKEN9", None) 
TOKEN10 = getenv("TOKEN10", None) 
