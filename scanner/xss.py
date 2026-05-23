import requests 

def check_reflected_xss(url):
     payload = "<xss7392>"
     r = requests.get(f"{url}?search={payload}")
     reponse = r.text

     if payload in reponse : 
          print("payload reflété non encodé")
     elif "&lt;xss7392&gt;" in reponse :  
          print("payload reflété et encodé")
     else :     
          print("payload non reflété")

check_reflected_xss("https://0ab200050375f924805af80000b4000a.web-security-academy.net/")