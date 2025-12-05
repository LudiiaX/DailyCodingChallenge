import re

def convert_list_item(markdown):
    pattern = r"^\s*[0-9]\.\s.+$"


    if re.match(pattern, markdown):
        return "<li>" + re.sub(r"^\s*[0-9]\.\s*", "", markdown) + "</li>"
    else :
        return "Invalid format"
    


print(convert_list_item("1. My item"))
print(convert_list_item(" 1.  Another item"))
print(convert_list_item("1 . invalid item"))
print(convert_list_item("2. list item text"))
print(convert_list_item(". invalid again"))
print(convert_list_item("A. last invalid"))