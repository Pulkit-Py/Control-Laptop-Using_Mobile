from nltk import Chat, reflections
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1",]
    ],
    [
        r"what is your name ?",
        ["My name is Alpha and I'm a chatbot ?",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) your age?",
        ["I'm a computer program dude\nSeriously you are asking me this?",]
        
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*) created ?",
        ["Pulkit Saini created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"are (.*) (happy|sad|felling)?",
        ["i am a machine i have no felling"]
],
[
        r"(thanks|thank you)",
        ["anything for you"]
],
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]
def chatty(queery):
    chat = Chat(pairs, reflections)
    value = chat.converse(queery)
    return value  
