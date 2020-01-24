import json
import difflib
dictionarydata = json.load(open("data.json"))

def translate(word):

    word = word.lower()
    
    if word.title() in dictionarydata:
        return translate(word.title())
    if word.upper() in dictionarydata:
        return translate(word.upper())
    elif not word in dictionarydata:
        possible = difflib.get_close_matches(word,dictionarydata.keys(),cutoff=0.8)
        
        if len(possible)>0:
            yn = input("Did you mean %s instead? Y/N " % possible[0]).lower()
            if yn[0]=='y':
                return translate(possible[0])
            elif yn!="n":
                return "Invalid input."  
            else:
                return "The word %s does not exist." % word
        return "The word %s does not exist." % word
    else:
        return dictionarydata[word]

output = translate(input("Translate "))

if isinstance(output,list):
    for item in output:
        print(item)