"""
THIS PROJECT IS MADE BY AI DEV SURYA - DEVELOPER SURYANSH
SUBSCRIBE MY YOUTUBE - AI DEV SURYA
FOLLOW MY INSTAGRAM - AI DEV SURYA

Time - 3:57 AM
Date - 6-11-2024
"""

from requests import get
from sys import argv

email_api = "d5c19813e49549489703effca4c553f5"
phone_api = "813cc57f70a84a82a663d5af5bebc62c"

email_url = "https://emailvalidation.abstractapi.com/v1/?api_key="+email_api
phone_url = "https://phonevalidation.abstractapi.com/v1/?api_key="+phone_api

def check_email(email):
    html = get(email_url,params={"email":email})
    if html.json()['is_smtp_valid']['value'] == True:
        return True
    else:
        return False
    # return html.json()

def check_phone(phone):
    html = get(phone_url,params={"phone":phone})
    if html.json()['valid'] == True:
        return True
    else:
        return False
    # return html.json()

if __name__=="__main__":
    try:
        user = argv[1]
    except:
        user = input("Enter here Email or Phone (with country code without +): ")
    if "@" in user:
        print(check_email(user))
    else:
        print(check_phone(user))