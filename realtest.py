from copying import recognize_voice
from webbrowser import get
import speech_recognition as sr  #파이썬 패키지를 설치하는 모듈은 pip 
from gtts import gTTS
import os
import time
import playsound
from speech import *
import again

def speak(text): # 말하는 값을 영어로 소리낸다
    tts = gTTS(text=text, lang='en')  #tts에 텍스트값은 텍스트에 넣고 언어는 영어이다
    filename = 'voice.mp3'  #파일네임은 voice로 만들기
    tts.save(filename)   # 위에있는 파일을 저장
    playsound.playsound(filename) # mp3 즉 플레이사운드로 말하기


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source: # 마이크로폰을 소스로 받아들여서
        audio = r.listen(source) # 이게 오디오로 번역 말하는것
        said = " "
        try:     
            said = r.recognize_google(audio) # 말하는걸 구글 api로 인식할수있게 해주고
            print(said) #이걸 인식한걸 str화 시키기
        except sr.UnknownValueError:  #음성인식이 못할수있기에
               speak("hey say again")
    return said  #아무것도 인식된게없으면 다시 said위치로 돌아가라

#def replay():
#    text = recognize_voice()

text = get_audio()

if string_ko == text():
   speak("Say it again") 
elif text != string_ko:
   speak("good job")
    #해결하지못한것 물어보았을때 정확하지않는 경우 다시말해달라 후 정확히 말할때까지 재질문, 모듈화 공부 및 DB  파이썬 copying.py 참고하면 될듯 계속 스타트 스피킹 요지랄함