from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('WinChat')

entrenador = ChatterBotCorpusTrainer(chatbot)

entrenador.train('chatterbot.corpus.spanish')

while True:
    solicitud = input('yo: ')
    respuesta = chatbot.get_response(solicitud)
    print('WinChat: ',respuesta)