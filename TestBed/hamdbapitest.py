import requests
import json 

callsign = "w2ofd"

url = "http://api.hamdb.org/" + callsign + "/json/w2amc"

response = requests.get(url)

# Checking if the request was successful (status code 200)
if response.status_code == 200:
    # Parsing the JSON response
    data = json.loads(response.text)
    call =  (data['hamdb']['callsign']['call']) 
    info = "\n Call: " + (data['hamdb']['callsign']['call']) + "\n"
    info += " First Name: " + (data['hamdb']['callsign']['fname']) + "\n"
    info += " Middle Inital: " + (data['hamdb']['callsign']['mi']) + "\n"
    info += " Last Name: " + (data['hamdb']['callsign']['name']) + "\n"
    if (data['hamdb']['callsign']['suffix']):
       info += " Suffix: " + (data['hamdb']['callsign']['suffix']) + "\n"
    info += " Address: " + (data['hamdb']['callsign']['addr1']) + "\n"
    info += " City: " + (data['hamdb']['callsign']['addr2']) + "\n"
    info += " State: " + (data['hamdb']['callsign']['state']) + "\n"
    info += " Zip: " + (data['hamdb']['callsign']['zip']) + "\n"
    info += " Country: " + (data['hamdb']['callsign']['country']) + "\n"
    print(f"The Information For " + call + " Is: ", info)
 
else:
    print("Failed to fetch data. Status code:", response.status_code)