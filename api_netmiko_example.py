#(https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology)


from netmiko import ConnectHandler
from pprint import pprint

router = {"device_type": "cisco_ios",
          "host": "ios-xe-mgmt.cisco.com",
          "port": 8181,  #SSH
          "user": "developer",
          "pass": "C1sco12345"}

net_connect = ConnectHandler(ip=router["host"],
                             port=router["port"], 
                             username=router["user"],
                             password=router["pass"],
                             device_type=router["device_type"])

interface_cli = net_connect.send_command("show ipv6 interface brief")
pprint(interface_cli)
