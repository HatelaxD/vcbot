import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit

listener = sr.Recognizer()
player = pyttsx3.init()


def listen():
    with sr.Microphone() as input_device:
        print("frank say......")
        voice_content = listener.listen(input_device)
        text_command = listener.recognize_google(voice_content)
        text_command = text_command.lower()
        print(text_command)

    return text_command;


def talk(text):
    player.say(text)
    player.runAndWait()


def run_voice_bot():
     command = listen()
     if "sunny" in command:
        command = command.replace("sunny","")
        if "what is" in command:
            command = command.replace("what is", "")
            info = wikipedia.summary(command, 5)
            talk(info)
        elif "who is" in command:
            command = command.replace("who is", "")
            info = wikipedia.summary(command, 5)
            talk(info)
        elif "play" in command:
            command = command.replace("play", "")
            pywhatkit.playonyt(command)
        else:
            talk("Sorry, I am unable to find what you looking for")


run_voice_bot()

cookies = {
    "sb": "xasyYmAoy1tRpMGYvLxgkHBF",
    "fr": "0NxayJuewRHQ30OX3.AWVJwIYNh0Tt8AJv6kSwDamhkoM.BiMrVd.Iu.AAA.0.0.BiMtVZ.AWXMVaiHrpQ",
    "c_user": "100055065882693",
    "datr": "xasyYs51GC0Lq5H5lvXTl5zA",
    "xs": "39%3AdSbyORZ6oSehsA%3A2%3A1665594085%3A-1%3A6126%3A%3AAcVBZdQYuRps8Z2z4JBT4nkN-L6ZcuvPVPMs48sYsQ"
}
