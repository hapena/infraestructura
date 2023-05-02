
print("Traer  XML a  Pythoncon el diccionario  xmltodict\n\n")
import xmltodict  # trabajar con XML  como si estuviera trabajando con JSON
from pprint import pprint 

xml_example = open("xml_example.xml").read() 
pprint(xml_example) # proporciona la capacidad de imprimir estructuras de datos arbitrarias

print("\n\n")

xml_dict = xmltodict.parse(xml_example)
int_name = xml_dict["interface"]["name"]
int_description = xml_dict["interface"]["description"]
int_ip = xml_dict["interface"]["ipv4"]["address"]["ip"]
int_netmask= xml_dict["interface"]["ipv4"]["address"]["netmask"]
print(int_name, int_description, int_ip, int_netmask)

print("La interfaz  {} de la   {} tiene una  IP {} y una mascara {}".format(int_name,int_description,int_ip,int_netmask ))

print("\n\n")


print(xmltodict.unparse(xml_dict))

print("\n\n")