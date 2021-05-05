import speech_recognition as sr
import time
from PIL import Image

def main():

    def sign_language(text):
        text = text.replace(" ", "")
    
        for i in text:
            s = i+".jpg"
            img=Image.open(s)
            img.show()
            time.sleep(2)

            
    print("Welcome to Speech to Sign")

    while True:
        print("To convert press 1")
        print("To exit press 0")
        flag=int(input())
        if flag:
            r = sr.Recognizer()
        
            with sr.Microphone() as source:
        
                audio = r.listen(source)
                text = r.recognize_google(audio)
                print(text)
        
                sign_language(text)
        else:
            print("Thank You")
            exit()
    





