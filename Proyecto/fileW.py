import json
def updateValues(dict):
    jsonFile = open("test1.json", "r")
    data = json.load(jsonFile) 
    jsonFile.close() 

    data["e"]= dict['e']
    data["me"]=dict['me']
    data["l"]= dict['l']
    data["v"]= dict['v']
    data["d"]= dict['d']
    data['w']=dict['w']
    data['w2']=dict['w2']
    data['phase']=dict['phase']

 
    jsonFile = open("test1.json", "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()