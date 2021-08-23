import sys
sys.path.append("C:\\Users\\karth\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages")
from difflib import get_close_matches

import mysql.connector
# connecting to the database
con=mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database='ardit700_pm1database'
)
#DATABASE AUTOMAICALLY CONVERTS THE INPUT TO LOWERCASE
while True:
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
            print(f'Meaning {i}:  '+ result[1] + '\n')
            i+=1

    #using difflib to get a close match
    elif(1):
        query=cursor.execute("SELECT Expression FROM Dictionary")
        results=cursor.fetchall()
        templist=[]
        for result, in results:
            templist.append(result)
        
        # expected ans contains the close matches
        expected_ans=get_close_matches(word,templist)
        
        #printing the first element of the expected ans 
        if(len(expected_ans)>0):
            tempans=input(f"Did you mean {expected_ans[0]}(Y/N):?  ")
            if tempans=='Y' or tempans=='y':
                query=cursor.execute("SELECT * FROM Dictionary WHERE Expression='%s'" % expected_ans[0])
                results=cursor.fetchall()
                i=1
                for result in results:                
                    print(f'Meaning {i}:  '+ result[1] + '\n')
                    i+=1     
    #telling the user he enterd the word incoreectly 
    else:
        print("No word found. Please enter a valid word")


    # asking user if he wants to continue
    if(input("Do you want to exit the Thesaurus?  ") in [ 'Y' , 'y' ]):
        break
    else:
        continue
