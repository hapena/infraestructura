import xml.etree.ElementTree as et #implementa una API simple y eficiente para analizar y crear datos XML
import re  # Este módulo proporciona operaciones de coincidencia de expresiones
xml = et.parse ("myfile.xml") #Analiza una sección XML en un árbol de elementos
root = xml.getroot() # Devuelve el elemento raíz de este árbol.


ns = re.match ('{.*}', root.tag) .group (0) #caracteres coinciden con el patrón de expresión regular , devuelve un objeto de coincidencia correspondiente
editconf = root.find ("{}edit-config".format (ns))
defop = editconf.find ("{}default-operation".format (ns)) # Find Buscar una subcadena dentro de una cadena
testop = editconf.find ("{}test-option".format (ns))

print ("La operación predeterminada contiene: {}".format(defop.text))
print ("La opción de prueba contiene: {}".format(testop.text))
