import requests

respuesta = False
preferencia = ""
repeat = True

from programy.clients.embed.datafile import EmbeddedDataFileBot

chatbot = EmbeddedDataFileBot(files={'aiml':['chatbots_aiml']}, defaults=True)

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "34797d00-7314-11ec-9290-114a13be1edab480f598-9c23-4852-b768-05b6893d26b6"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()
    
def answer_preferencia():
    question = input("> ")
    answer = classify(question)
    answerclass = answer["class_name"]
    confidence = answer["confidence"]
    global respuesta
    global preferencia

    if confidence < 75:
        print("Perdona pero no he entendido muy bien sus preferencias, podría especificarme si es carnívoro o vegano?")
    elif answerclass == "vegano":
        print(chatbot.ask_question(answerclass))
        preferencia = "vegano"
        respuesta = True
    elif answerclass == "carnivoro":
        print(chatbot.ask_question(answerclass))
        preferencia = "carnivoro"
        respuesta = True

def answer_pan():
    question = input("> ")
    answer = classify(question)
    answerclass = answer["class_name"]
    confidence = answer["confidence"]
    global respuesta

    if confidence < 75:
        print("Perdona, pero podría repetirme el tipo de pan que quiere? El clásico, brioche o de chapata")
    elif answerclass == "pan_burguer":
        print(chatbot.ask_question(answerclass))
        respuesta = True
    elif answerclass == "pan_brioche":
        print(chatbot.ask_question(answerclass))
        respuesta = True
    elif answerclass == "pan_chapata":
        print(chatbot.ask_question(answerclass))
        respuesta = True

def answer_carne_veg():
    question = input("> ")
    answer = classify(question)
    answerclass = answer["class_name"]
    confidence = answer["confidence"]
    global respuesta

    if confidence < 75:
        print("Perdona, pero podría repetirme el tipo de carne que quiere? Tofu o falafel?")
    elif answerclass == "tofu":
        print(chatbot.ask_question(answerclass))
        respuesta = True
    elif answerclass == "falafel":
        print(chatbot.ask_question(answerclass))
        respuesta = True

def answer_carne_car():
    question = input("> ")
    answer = classify(question)
    answerclass = answer["class_name"]
    confidence = answer["confidence"]
    global respuesta

    if confidence < 75:
        print("Perdona, pero podría repetirme el tipo de carne que quiere? Ternera o pollo?")
    elif answerclass == "ternera":
        print(chatbot.ask_question(answerclass))
        respuesta = True
    elif answerclass == "pollo":
        print(chatbot.ask_question(answerclass))
        respuesta = True


while repeat:

    print("Es usted vegano o tiene alguna preferencia en la comida?")
    respuesta = False
    while respuesta==False:
        answer_preferencia()


    
    respuesta = False
    while respuesta==False:
        answer_pan()


    if(preferencia == "vegano"):
        
        respuesta = False
        while respuesta==False:
            answer_carne_veg()
    elif(preferencia == "carnivoro"):
        
        respuesta = False
        while respuesta==False:
            answer_carne_car()


    repetir = str(input("Quiere hacer otro pedido? s/n:\n"))
    repetir = repetir.lower()
        
    if(repetir=="n" or repetir=="no"):
        print("Ok, adios.")
        repeat = False
    elif(repetir=="s" or repetir=="si" or repetir=="sí"):
        print("Guay!")
    else:
        print("Disculpe las molestias pero ha habido un error en su pedido, inténtelo de nuevo...")
        repeat = False


'''while True:
    answer_question()'''

