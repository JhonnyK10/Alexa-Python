import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print('Estou ouvindo...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Reconhecendo...')
        query = r.recognize_google(audio, language='pt-br')
        print(f'Usuario disse: {query}\n')

    except Exception as e:
        print('Diga novamente por favor...')
        return "None"

    return query

def create_todo_list():
    speak('O que você quer adicionar a sua lista de tarefas?')
    task = recognize_speech()
    with open('todo.txt', 'a') as f:
        f.write(f'{datetime.datetime.now()} - {task}\n')
    speak('Tarefa adicionada') 

def search_web():
    speak('O que você gostaria de procurar?')
    query = recognize_speech()
    url = f'https://www.google.com/search?q={query}'
    webbrowser.open(url)
    speak(f'Aqui está os resultados para {query}.')

def set_reminder():
    speak('O que devo lembrá-lo?')
    task = recognize_speech()
    speak('Em quanto tempo?')
    mins = recognize_speech()
    mins = int(mins)
    reminder_time = datetime.datetime.now() + datetime.timedelta(minutes=mins)
    with open('reminders.txt', 'a') as f:
        f.write(f'{reminder_time} - {task}\n')
    speak(f'Lembrete definido para daqui {mins} minutos a partir de agora.')

def main():
    speak('Olá! Eu sou seu assistente pessoal. Em que posso te ajudar?')
    while True:
        query = recognize_speech().lower()

        if 'criar uma lista de tarefas' in query:
            create_todo_list()

        elif 'procure na web' in query:
            search_web()

        elif 'criar lembrete' in query:
            set_reminder()

        elif 'pare' in query or 'sair' in query:
            speak('Até logo!')
            break
        else:
            speak('Desculpe, não entendi. Poderia repetir por favor?')

main()