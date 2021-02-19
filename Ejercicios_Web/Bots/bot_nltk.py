from nltk.chat.util import Chat, reflections

mis_reflexions = {
"ir": "fui",
"hola": "hey"
}
pares = [
    [
        r"mi nombre es (.*)",
        ["Hola %1, como estas ?", ]
    ],
    [
        r"cual es tu nombre ?",
        ["Mi nombre es Chatbot ?", ]
    ],
    [
        r"como estas ?",
        ["Bien, y tu?", ]
    ],
    [
        r"disculpa (.*)",
        ["No pasa nada", ]
    ],

    [
        r"mal",
        ["no estes mal Dios te ama", ]
    ],

    [
        r"hola|hey|buenas",
        ["Hola", "Que tal", ]
    ],
    [
        r"que (.*) quieres ?",
        ["Nada gracias", ]

    ],
    [
        r"(.*) creado ?",
        ["Fui creado hoy" ]
    ],
    [
        r"finalizar",
        ["Chao", "Fue bueno hablar contigo"]
    ],
]


def chatear():
    print("Hola soy un bot, escribe algo para comenzar")  # mensaje por defecto
    chat = Chat(pares, mis_reflexions)
    chat.converse()


if __name__ == "__main__":
    chatear()