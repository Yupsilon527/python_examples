import difflib
import mysql.connector
    
connection = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

def dictionary_value(name):

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % name)
    return cursor.fetchall()

def dictionary_expressions(initial):

    cursor = connection.cursor()
    cursor.execute("SELECT Expression FROM Dictionary WHERE Expression  LIKE '"+ initial +"%'" )
    return cursor.fetchall()
    

def translate(word):

    results = dictionary_value(word)
    if len(results) == 0:
        
        possible = difflib.get_close_matches(word.lower(),dictionary_expressions(word[0:1]),cutoff=0.8)
        
        if len(possible)>0:
            yn = input("Did you mean %s instead? Y/N " % possible[0]).lower()
            if yn[0]=='y':
                return translate(possible[0])
            elif yn!="n":
                return "Invalid input."  
            else:
                return
        return 
    else:
        return results[0][1]

sInput = input("Translate ")
sOutput = translate(sInput) or translate(sInput.lower()) or translate(sInput.upper()) or ("The word %s does not exist." % sInput)

if isinstance(sOutput,list):
    for item in sOutput:
        print(item)
else:
    print (sOutput)