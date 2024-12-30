import xml.dom.minidom

try:
    doc = xml.dom.minidom.parse("sample.xml")
    
    elements = doc.getElementsByTagName("*")
    
    print("Tên của các phần tử trong file sample.xml:")
    for element in elements:
        print(element.tagName)
except Exception as e:
    print(f"Lỗi xảy ra: {e}")
