import requests
import json 

def getcallinfo(callsign) :

    #callsign = "w2ofd"

    url = "http://api.hamdb.org/" + callsign + "/json/w2amc"

    response = requests.get(url)

    # Checking if the request was successful (status code 200)
    if response.status_code == 200:
    
        # Parsing the JSON response
        data = json.loads(response.text)
       # call =  (data['hamdb']['callsign']['call']) 
  
        info = " Call: " + (data['hamdb']['callsign']['call']) 
        info += " | First Name: " + (data['hamdb']['callsign']['fname']) 
        info += " | Middle Inital: " + (data['hamdb']['callsign']['mi'])
        info += " | Last Name: " + (data['hamdb']['callsign']['name'])
        if (data['hamdb']['callsign']['suffix']):
           info += " | Suffix: " + (data['hamdb']['callsign']['suffix'])
        info += " | Address: " + (data['hamdb']['callsign']['addr1'])
        info += " | City: " + (data['hamdb']['callsign']['addr2'])
        info += " | State: " + (data['hamdb']['callsign']['state'])
        info += " | Zip: " + (data['hamdb']['callsign']['zip'])
        info += " | Country: " + (data['hamdb']['callsign']['country'])
        return(info, data)
    else:
        print("Failed to fetch data. Status code:", response.status_code)