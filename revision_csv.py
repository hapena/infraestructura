print("Importamos datos de Archivo csv")
import csv 
from pprint import pprint 

csv_example = open("csv_example.csv").read() 
pprint(csv_example)


print("\n\n")

csv_example = open("csv_example.csv")
csv_python = csv.reader(csv_example, delimiter=',', quotechar=',')


for row in csv_python: 
  print("El {} esta en  {} y tiene una  IP {}".format(row[0], row[2], row[1]))

print("\n\n")