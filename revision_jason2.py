
print("Traer  JSON and trabajar con  json\n\n")
import json 
from pprint import pprint 

json_example = open("json_example.json").read()
pprint(json_example)

json_python = json.loads(json_example)
int_name = json_python["ietf-interfaces:interface"]["name"]
print(int_name)

print(json.dumps(json_python))

print("\n\n")