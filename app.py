import json
from difflib import get_close_matches
data=json.load(open("PYTHON\English Thesarus\data.json"))

#sequence matcher from difflib is a generator and the ratio method gives a number 
#indicating how similar they are

# difflib.get_close_matches('rain',['rainn'])
# ['rainn']
#by def gives 3 values

def indexed(word):
    word=word.lower()
    if word in data:
        mean=(data[word])
        return mean
    elif  word.title() in data:
        mean=(data[word.title()])
        return mean
    elif  word.upper() in data:
        mean=(data[word.upper()])
        return mean
    elif( len(get_close_matches(word,data.keys())) > 0 ):
        ind=input(f"Did you mean {get_close_matches(word,data.keys())[0]} :")
        if ind=='y' or ind=='Y':
            mean=(data[get_close_matches(word,data.keys())[0]])
            return mean
        elif (ind=='n' or ind=='N'):
            print("Please enter a valid word")
        else:
            print("Sorry we couldn't understand you")
        
    else:
        print("Please enter a valid word")

word=input("Enter the Word: ")
mean=indexed(word)
if type(mean)==list:
    for i in mean:
        print(i)


