import json
import yaml

with open ('myfile.json', 'r') as json_file:
 ourjson = json.load (json_file)  # load converts a json document to a Python object
 
print("\n\n")
print(ourjson)
print("\n\n")
print (yaml.dump (ourjson)) #  dump acepta un objeto Python y produce un documento YAML.