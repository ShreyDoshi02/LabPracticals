# A... String Operation
# Reverse the given string 
print("Shubham...")
mystr = input("Enter String : ")
print("\nReverese String of ", mystr , " is : ", mystr[::-1])

# Replace some character of the string with another character
modified_str = mystr.replace('N' , 'n')
print("\nOriginal String : ", mystr, "\nModified String : " , modified_str)

# Merge two string
mystr1 = "Earth"
merged_str = mystr1 + " " + mystr
print("\nMerged String : ", merged_str)

# Find whether the character in the given string or not.
if('o' in mystr) :
    print("\nCharacter 'o' is present in given string ", mystr)
else :
    print("\nCharacter 'o' is not present in given string ", mystr)
    
# Split String 
mystr2 = "Hello, Hii, hey"
splited_str = mystr2.split(',')
print("\nSplit String with ',' : ", splited_str)



# B Dictionary Operations:
# Apply "update, delete, clear, popitem, pop, get, keys and values" operation in dictionary
country = {
    "city": "vadodara",
    "population": "5.8M",
}

country.update({"bus": "station"})

for key, value in country.items():
    print(f"{key}: {value}")

del country["population"]
print(country)

key = country.keys()
print(key)
val = country.values()
print(val)

popElement = country.pop("bus")
print(popElement)

popItem = country.popitem()
print(country)

country.update({"Bus": "Station"})
country.update({"city": "Vadodara"})

country.clear()
print(country)

# Create 3 dictionaries and merge them into dictionary

dict1 = {
    "city": "vadodara",
    "population": "8.3M",
}

dict2 = {
    "bus": "station",
    "famous place": "Msu",}

dict3 = dict1 | dict2
print(dict3)