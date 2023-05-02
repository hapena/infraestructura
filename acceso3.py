file = open ("devices.txt", "a") #  método append que es designado con una a
while True:
    newItem = input("Enter device name: ")
    if newItem == "exit":
        print("All done!")
    break
file.write(newItem + "\n")
file.close()