from tokenize import Token
import requests
import os



TOKEN_KEY = "6579725816:AAHE6KN1Tei0YiaedmFLth-VUPxWez5M7ZY"
chatid = "-4067642204"


def send_image(file_name):
    
    path = os.path.join('tmp',file_name)
    if os.path.isfile(path):
        fil = {'photo':open(path,'rb')}
        if os.path.exists(path):
            resp = requests.post("https://api.telegram.org/bot{0}/sendPhoto?chat_id={1}".format(TOKEN_KEY,chatid),files=fil)
        return resp.status_code
    else:
        return 400

