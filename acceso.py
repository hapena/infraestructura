file = open("devices.txt", "r")
for item in file:
    item=item.strip() # eliminar todos los espacios en blanco iniciales y finales 
    print(item)
file.close() 


