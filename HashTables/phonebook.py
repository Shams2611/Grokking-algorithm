"""
Classic example: phone book

Name -> Phone number
"""

phonebook = {}

# add entries
phonebook["jenny"] = "867-5309"
phonebook["bob"] = "555-1234"
phonebook["emergency"] = "911"

# lookup
print(phonebook["jenny"])

# check if exists
if "alice" in phonebook:
    print(phonebook["alice"])
else:
    print("alice not in phonebook")
