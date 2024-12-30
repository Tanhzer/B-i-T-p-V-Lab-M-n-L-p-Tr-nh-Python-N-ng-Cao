import xml.dom.minidom

doc = xml.dom.minidom.parse("sample.xml")

company_name = doc.getElementsByTagName("name")[0].firstChild.data
print(f"Company Name: {company_name}")

staffs = doc.getElementsByTagName("staff")

print("Staff details:")
for staff in staffs:
    staff_name = staff.getElementsByTagName("name")[0].firstChild.data
    staff_salary = staff.getElementsByTagName("salary")[0].firstChild.data
    print(f"Name: {staff_name}, Salary: {staff_salary}")
