import pyttsx3  #pyttsx3 is a library that converts text --> speech

if __name__ == '__main__':
    engine = pyttsx3.init()
    while(True):
        x = input("What do you want me to say: ")
        
        if x == "exit":
            engine.say("GoodBye my dear Friend")
            engine.runAndWait()
            break

        engine.say(x)           #say() is an inbuilt function in the pyttsx3 , where the system speaks to user.
        engine.runAndWait()      #runAndwait() is a inbuilt function in the pyttsx3 , is a start speech synthesis engine and block application until engine (system) has finished speaking.
        