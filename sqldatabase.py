import sys
sys.path.append("C:\\Users\\karth\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages")


import mysql.connector
# connecting to the database
con=mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database='ardit700_pm1database'
)
#DATABASE AUTOMAICALLY CONVERTS THE INPUT TO LOWERCASE

# accepting the input
word=input('Enter a word: ')

# //creating a cursor object
cursor=con.cursor()
# selecting all from dict where the word(expression) has inlay in it
#string formatting %s replaced by %word
query=cursor.execute("SELECT * FROM Dictionary WHERE Expression='%s'"  % word)
results=cursor.fetchall()
if results:
    i=1
    for result in results:
        print(f'Meaning {i}:  '+ result[1])
        i+=1
else:
    print("No word found. Please enter a valid word")

