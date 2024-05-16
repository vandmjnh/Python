#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print('Thirty' + ' Days' + ' Of' + ' Python')
#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print('Coding' + ' For' + ' All')
#Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
#Print the variable company using print().
print(company)
#Print the length of the company string using len() method and print().
print(len(company))
#Change all the characters to uppercase letters using upper() method.
print(company.upper())
#Change all the characters to lowercase letters using lower() method.
print(company.lower())
#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize(), '\n', company.title(), '\n', company.swapcase())
#Cut(slice) out the first word of Coding For All string.
print(company[company.index(' '):])
#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding'), company.index('Coding'))
#Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))
#Change Python for Everyone to Python for All using the replace method or other methods.
print('Python for Everyone'.replace('Everyone', 'All'))
#Split the string 'Coding For All' using space as the separator (split()).
print(company.split())
#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))
#What is the character at index 0 in the string Coding For All.
print(company[0])
#What is the last index of the string Coding For All.
print(company[-1])
#What character is at index 10 in "Coding For All" string.
print(company[10])
#Create an acronym or an abbreviation for the name 'Python For Everyone'.
name = 'Python For Everyone'
print(name[0] + name[name.find(' ')+1] + name[name.rfind(' ')+1])
#Create an acronym or an abbreviation for the name 'Coding For All'.
print(company[0] + company[company.index(' ')+1] + company[company.index(' ')+1])
#Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))
#Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))
#Use rfind to determine the position of the last occurrence of l in Coding For All People.
print((company+' People').rfind("l"))
#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.find('because'))
#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.rindex('because'))
#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.replace('because because because', ''))
#Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.find('because'))
#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.replace('because because because', ''))
#Does ''Coding For All' start with a substring Coding?
print(company.startswith('Coding'))
#Does 'Coding For All' end with a substring coding?
print(company.endswith('conding'))
#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
print('   Coding For All      '.strip())