import json
data=json.load(open("PYTHON\English Thesarus\data.json"))


def indexed(word):
    if word in data:
        print(data[word])
    else:
        print("Please enter a valid word")

word=input("Enter the Word: ")
indexed(word)

