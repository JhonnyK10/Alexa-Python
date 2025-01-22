import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        print('Say that again please...')
        return "None"
    return query

def create_todo_list():
    speak('What do you want to add in your task list?')
    task = recognize_speech()
    with open('todo.txt', 'a') as f:
        f.write(f'{datetime.datetime.now()} - {task}\n')
    speak('Task added to your list.') 

def search_web():
    speak('What do you want me to search?')
    query = recognize_speech()
    url = f'https://www.google.com/search?q={query}'
    webbrowser.open(url)
    speak(f'Here are some results of {query}.')

def tell_time():
    current_time = datetime.datetime.now().strftime('%H:%M')
    speak(f'The time is {current_time}.')

def tell_date():
    today = datetime.datetime.now().strftime('%A, %d %B %Y')
    speak(f'Today is {today}.')

def main():
    speak('Hello! I am your personal assistance. How can I help you today?')
    while True:
        query = recognize_speech().lower()

        if 'create a task list' in query:
            create_todo_list()

        elif 'search on the web' in query:
            search_web()

        elif 'tell me the time' in query:
            tell_time()

        elif 'tell me the date' in query:
            tell_date()

        elif 'stop' in query:
            speak('Good bye! See you soon!')
            break
        else:
            speak('Sorry, I did not understand. Can you repeat please?')

main()