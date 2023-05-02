
print("Traer archivo yaml \n\n")
import yaml 
from pprint import pprint 

yml_example = open("yaml_example.yaml").read() 
pprint(yml_example)


print("\n\n")

yaml_python = yaml.safe_load(yml_example)
int_name = yaml_python["ietf-interfaces:interface"]["name"]
print(int_name)


print("\n\n")

print(yaml.dump(yaml_python))

print("\n\n")


