WORD_TYPE_LIST = ["Plural Noun", "Person's First Name", "Noun", "Person's Last Name", "Plural Noun", "Place", "Plural Noun", "Place", "Plural Noun", "Noun", "Adjective", "Adjective", "Verb", "Adjective"]
inputList = []

print("#-----MADLIB GENERATOR 9000-----#")
# loop through word type list
for wordType in WORD_TYPE_LIST:
    # get user input, strip whitespace
    userInput = input(wordType + ": ").strip()
    # append input to input list
    inputList.append(userInput)

# create the mega string, use format to insert list items
madlib = """
#-----THE BIG GAME-----#

Hello there, sports {}!
This is {}, talking to you from the press {}
in {} Stadium, where 57,000 cheering {}
have gathered to watch (the) {} {}
take on (the) {} {}.
Even though the {} is shining, it's a/an {}
cold day with the temperature in the {} 20's.
We'll be back for the opening {}-off after a few words from our {} sponsor.
""".format(*inputList)

# print the 
print(madlib)