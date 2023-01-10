

# Make Title with input and output value
def makeTitle(unformatedString):
   formatedString =  unformatedString.title()
   return formatedString

# function that format your name into upper case
def formatName(first_name, last_name):
   formated_first =  first_name.upper()
   formated_last =  last_name.upper()
   return f"{formated_first} {formated_last}"

formstedString = makeTitle("Hello To The World")
print(formstedString)
formatedName = formatName("Osama Bin Azam" , "Arain")
print(formatedName)
