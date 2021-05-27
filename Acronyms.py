# Create Acronyms using Python


user_input = str(input("Enter a Phrase: "))
text = user_input.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)

# An acronym is a short form of a word created by long words or phrases such as NLP for natural language processing
