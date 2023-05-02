
#Primero, debo importar la función  ConnectHandler de Netmiko
from netmiko import ConnectHandler
from pprint import pprint


#defino un diccionario de dispositivo
router = {"device_type": "cisco_ios",
          "host": "sandbox-iosxe-latest-1.cisco.com",
          "port": 22,  #SSH
          "username": "developer",
          "password": "C1sco12345"}
#llamar a ConnectHandler y pasar mi diccionario de dispositivo definido anteriormente:
net_connect = ConnectHandler(ip=router["host"],
                             port=router["port"], 
                             username=router["username"],
                             password=router["password"],
                             device_type=router["device_type"])

#net_connect = ConnectHandler(**router) 
#net_connect2 = ConnectHandler(device_type="cisco_ios", host="192.168.56.101",port: "22", username="cisco", password="cisco123!"") 
#conexión SSH establecida. Puedo verificar esto ejecutando el método
#net_connect.find_prompt()


#enviar comandos por el canal SSH y recibir la salida.
interface_cli = net_connect.send_command("show ip interface brief")
print(interface_cli)
print("\n\n")
interface_cli = net_connect.send_command("show running-config")
print(interface_cli)
print("\n\n")

#creo una lista de comandos de configuración 

config_commands = ["hostname hugo",
                    "exit",]

#Este método ingresará al modo de configuración, ejecutará los comandos y luego saldrá 
interface_cli = net_connect.send_config_set(config_commands)
print(interface_cli)

print("\n\n")

#net_connect.send_config_from_file()
#net_connect.disconnect() 