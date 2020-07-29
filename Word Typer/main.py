import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak('I am Word Typer')


def main():
    i = 0
    speak('Fill The Following parameters')
    word = input('Choose A Word Or Letter :')
    times = int(input('How Many Times You Want To Print It :'))
    file = input('Choose A File Name  :')

    for i in range(times):
        print(word, end='     ')
    f = open(file, 'w+')
    f.write(times*word)
    speak('Done SIR')


if __name__ == "__main__":
    WishMe()
    main()
