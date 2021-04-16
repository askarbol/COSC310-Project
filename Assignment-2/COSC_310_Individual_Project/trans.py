
#first do this
#pip install googletrans==3.1.0a0

from googletrans import Translator
t = Translator()
def isEng(userInput):
    var = t.translate(userInput)  # checks what langauge the user inputed and translates it to english
    if(var != 'en'):
        userInput = var.text
        return userInput #return the user input back in english
    else:
        return userInput #return the user input back if was english



