import http.client

conn = http.client.HTTPSConnection("skyscanner-skyscanner-flight-search-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "8b4f07cab7msh2a9da4d5e3e5911p1e3d99jsn354aceaecdbe",
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
    }

def getPlace():
    conn.request("GET", "/apiservices/autosuggest/v1.0/UK/GBP/en-GB/?query=Stockholm", headers=headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def getFlights():
    conn.request("GET", "/apiservices/browseroutes/v1.0/US/USD/en-US/SFO-sky/ORD-sky/2021-09-01?inboundpartialdate=2021-12-01", headers=headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def getQuotes():
    conn.request("GET", "/apiservices/browsequotes/v1.0/US/USD/en-US/SFO-sky/ORD-sky/2021-09-01?inboundpartialdate=2021-12-01", headers=headers)
    # conn.request("GET", "/apiservices/browsequotes/v1.0/US/USD/en-US/SFO-sky/JFK-sky/2019-09-01?inboundpartialdate=2019-12-01", headers=headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

'''
Main Program
'''
getFlights()
getQuotes()