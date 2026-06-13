#!/bin/python3
# Source - https://stackoverflow.com/a/30221436
# Posted by Dale Moore
# Retrieved 2026-06-12, License - CC BY-SA 3.0

import json
import requests

def getData():
    try:
        response = requests.post("http://192.168.0.129/data")
        print(response.text)
        return response.text
    except:
        return ""
    pass

def main():

    jsonText=getData()
    if(len(jsonText)==0):
        print("error getting data")
        return
    else:
        jsonString=jsonText
    # create a simple JSON array
    #jsonString = '{"key1":"value1","key2":"value2","key3":"value3"}'

    # change the JSON string into a JSON object
    jsonObject = json.loads(jsonString)

    outText=""
    # print the keys and values
    for key in jsonObject:
        value = jsonObject[key]
        if (key=='hour'):
            break
        #print("{}={}&".format(key, value),end='')
        outText+="{}={}&".format(key, value)

    outText=outText[:-1] #cut last ampersand from string
    print("curl -X POST -d '{}' http://192.168.0.101/data".format(outText))
    pass

if __name__ == '__main__':
    getData()
    main()

