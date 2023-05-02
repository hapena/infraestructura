from netmiko import ConnectHandler


router = {"device_type": "cisco_nxos",
          "host": "sandbox-nxos-1.cisco.com",
          "port": 22, 
          "username": "admin",
          "password": "Admin_1234!"}


net_connect= ConnectHandler(**router)
net_connect.send_config_from_file(config_file="comandos_cli.txt")
interface_cli = net_connect.send_command("show ip interface brief")
print(interface_cli)
net_connect.disconnect() 