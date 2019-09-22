import xml.etree.ElementTree as ET

tree = ET.parse('grafo_web.gml')

dataset = tree.getroot()

boundedBy = dataset[0]
dataset.remove(boundedBy)

prefissi = dict()

for feature_member in dataset:
    grafo_web = feature_member[0]
    desvia = grafo_web[3]
    val = desvia.text

    if not val is None:
        p = val.split()[0]

        if p in prefissi:
            prefissi[p] += 1
        else:
            prefissi[p] = 1

        prefisso = ET.Element('prefisso')
        prefisso.text = p
        grafo_web.append(prefisso)

print(prefissi)

dataset.insert(0, boundedBy)

tree.write('output.gml')
