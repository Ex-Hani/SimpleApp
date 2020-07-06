import speech_recognition as sr
import os
import sys
import webbrowser
import pyaudio
import pyttsx3

def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()

talk("Приветствую, жду твоей команды")

def command():
    user_command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Говорите")
        user_command.pause_threshold = 1
        user_command.adjust_for_ambient_noise(source, duration=1)
        audio_command = user_command.listen(source)

    try:
        text_command = user_command.recognize_google(audio_command).lower()
        print("Вы сказали - " + text_command)
    except sr.UnknownValueError:
        talk("Я вас не поняла, прошу повторите")
        text_command = command()
    return  text_command

def makeSomeThing(mark):
    if 'open website' in mark:
        talk("Уже открываю")
        url = 'https://youtube.com'
        webbrowser.open(url)
    elif 'stop' in mark:
        talk("Завершаю сеанс работы")
        sys.exit()

while True:
    makeSomeThing(command())