"""

XML (Extensible Markup Language) es un lenguaje de marcado que se utiliza para almacenar e intercambiar datos estructurados.
Está diseñado para ser legible tanto por humanos como por máquinas. 
XML usa etiquetas para definir elementos y atributos para proporcionar información adicional sobre esos elementos.
"""
import xml.etree.ElementTree as ET
# Parsing the XML = analizar la extructura del XML
tree = ET.parse('Data_xml.xml')
# Obtener the elemento raiz = recuperar el elemento de nivel superior del documento XML
root = tree.getroot()
print(root)
# Iterar sobre los elementos child elements
# un elemento secundario (child element) es un elemento anidado dentro de otro elemento, 
# también conocido como elemento principal.
for child in root:
    print(child.tag, child.attrib)

# encontrar el elemento div en el id id propertyDetailBulletList
div_element = root.find(".//div[@id='propertyDetailBulletList']")
# Imprimir el div element y su children
ET.dump(div_element)

# Encontrar todos los li dentro de div
li_elems = div_element.findall(".//li")
# Extraer el texto en cada li 
li_values = [li.text for li in li_elems]
print(li_values)


ref_div = root.find(".//div[@id='propertyDetailRef']")
ref_text = ref_div.text  # "Ref: 1747204"
print(ref_text)
print(ref_text.split(": ")[1])

# Otro ejemplo
ref_div = root.find(".//div[@id='propertyDetailRef']")
ref_text = ref_div.text  # "Ref: 1747204"
ref_number = ref_text.split(": ")[1]  # "1747204"
print(ref_number,':', ref_text)  # prints "1747204")