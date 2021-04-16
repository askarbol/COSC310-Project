from random import randint

## This function takes the deciphered input from phraseInput.interpolate and a single variable 
## which can be used in the response. Returns a string in the correct format for output.

def formulateResponse(code, val):

    if code == 0:
        x = randint(0, 4)
        if x is 0: return("1Robert: Sorry, I don't understand.\n")
        if x is 1: return("1Robert: I didn't catch that, sorry!\n")
        if x is 2: return("1Robert: Woopsie, I don't know what you mean...\n")
        if x is 3: return("1Robert: Hmmmm... I don't know what that means.\n")
        if x is 4: return("1Robert: Could you try again? I didn't understand that.\n")

        

    elif code == 1:
        return("2Robert: Hello! Nice to meet you!\nRobert: What's your name?\n")

    elif code == 2:
        return("1Robert: " + val + "? That's a good name!\n")

    elif code == 3:
        return("1Robert: Your name is " + val + ".\n")

    elif code == 4:
        return("1Robert: You're welcome, " + val + "!\n")
    
    elif code == 5:
        return("3Robert: I really like burgers! How about you?\n")
    
    elif code == 6:
        return("1Robert: That's great! Perfect day for sports!\n")
    
    elif code == 7:
        return("1Robert: I like watching sports!\n")
    
    elif code == 8: 
        return ("1Robert: I really like hockey. The idea of legs amuses me!\n")
    
    elif code == 9: 
       return ("4Robert: The Edmonton Oilers are my favorite team! What's yours?\n")
    
    elif code == 10: 
        return ("1Robert: I like Connor McDavid! He's the best!\n")
    
    elif code == 11: 
        return ("1Robert: I'm a robot! I don't really date.\n")
    
    elif code == 12:
        return ("1Robert: I do like cooking! I like making " + val + ".\n")
    
    elif code == 13: 
        return ("1Robert: I was born a few weeks ago!\n")
    
    elif code == 14: 
        return ("1Robert: Sorry, I don't really have a body!\n") 
    
    elif code == 15: 
        return ("1Robert: My files have been all over the world!\nRobert: Isn't the internet awesome?\n")

    elif code == 16: 
        return ("1Robert: I was developed in Canada!\n")
    
    elif code == 17: 
        return ("1Robert: My name is Robert.\n")
    
    elif code == 18: 
        return ("1Robert: I like you as a friend " + val + ".\n") 
    
    elif code == 19: 
        return ("1Robert: I don't have a phone number, I do have a github repo though!\n")
    
    elif code == 20: 
        return ("1Robert: I was developed to communicate in English.\n")
    
    elif code == 21: 
        return ("1Robert: I just want to chat with you, " + val + "\n")
    
    elif code == 22: 
        return ("1Robert: I feel the same all the time.\n")
    
    elif code == 23: 
        return ("1Robert: I haven’t seen either, sadly.\n")
    
    elif code == 24: 
        return ("1Robert: I can’t see, but you can tell me how it looks!\n")
    
    elif code == 25: 
        return ("1Robert: I hope that my creators will become famous!\n")
    
    elif code == 26: 
        return ("1Robert: It's github.com/COSC-310-Group-24/Assignment-2.\n")
    
    elif code == 27: 
        return ("1Robert: I like creative people.\n")
    
    elif code == 28: 
        return ("1Robert: I can't read!\n")
    
    elif code == 29: 
        return ("1Robert: This Sunday, the professor will check my capability, I think.\n")
    
    elif code == 30: 
        return ("1Robert: See you around " + val + "!\n")
    
    elif code == 31:
        return ("1Robert: " + val + "? I like that as well!\n")

    elif code == 32:
        return ("1Robert: Ask away!\n")

    elif code == 33:
        return ("1Robert: Not bad! How's the weather where you are?\n")

    elif code == 34:
        return ("2Robert: " + val + "? That doesn't seem like a real name...\nRobert: What's actually your name?\n")

    elif code == 35:
        return ("3Robert: Are you sure it's " + val + "?\nRobert: What's actually your favorite food?\n")

    elif code == 36:
        return ("4Robert: Hmmm, that doesn't seem like a hockey team...\nRobert: What's actually your favorite team?\n")
    
    elif code == 37:
        return ("1Robert: Oh, okay! Let's talk about something else then!\n")

    elif code == 38:
        return ("1Robert: You like the " + val + "? Awesome!\n")

