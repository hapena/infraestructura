import json
import yaml

with open ('address_list.json', 'r') as json_file:
 ourjson = json.load (json_file)
 
 
print(ourjson)
print("\ n\ n—")
print (yaml.dump (ourjson))