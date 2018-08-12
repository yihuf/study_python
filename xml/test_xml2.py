import xml.dom.minidom

domtree = xml.dom.minidom.parse("test1.xml")


objects = domtree.getElementsByTagName('object')

for object in objects:
    if object.hasAttribute('name'):
        print(object.getAttribute('name'))
