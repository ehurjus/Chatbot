import requests

respuesta = False
preferencia = ""
repeat = True

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

"""def answer_question():
    question = input("> ")
    answer = classify(question)
    answerclass = answer["class_name"]
    confidence = answer["confidence"]

    if confidence < 75:
        print("No he entendido lo que me has dicho, dime alguna otra cosa!")
    elif answerclass == "nombre":
        print("Muy bonito nombre")
    elif answerclass == "vegano":
        print("Está muy bien entonces usted no consumirá productos animales")
    elif answerclass == "carnivoro":
        print("En ese caso le proporcionaremos productos de origen animal")
    elif answerclass == "pan_burguer":
        print("Se ve que usted va a lo clásico, marchando un pan de hamburguesa")
    elif answerclass == "pan_chapata":
        print("Pues le pondremos un pan de chapata")
    elif answerclass == "pan_brioche":
        print("Uy entonces usted debe de ser muy dulce, marchando el pan brioche")
    elif answerclass == "tofu":
        print("El plato número uno de los veganos eeh, marchando el tofu")
    elif answerclass == "falafel":
        print("Poca gente se lo pide, pero todos terminan repitiendo, tucarne de falafel está apuntada")
    elif answerclass == "ternera":
        print("Qué sería una hamburguesa sin carne de ternera eh...")
    elif answerclass == "pollo":
        print("La nueva moda de pedirse la hamburguesa de pollo, si yo te contara cómo los preparamos fipabas xddd")    """

def answer_nombre():
    question = input("> ")
    answer = classify(question)
    answerclass = answer["class_name"]
    confidence = answer["confidence"]
    global respuesta

    if confidence < 75:
        print("Perdona? Eso es un nombre? Venga, dígame su nombre real...")
    elif answerclass == "nombre":
        print("Muy bonito nombre")
        respuesta = True
    
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
        print("Está muy bien entonces usted no consumirá productos animales")
        preferencia = "vegano"
        respuesta = True
    elif answerclass == "carnivoro":
        print("En ese caso le proporcionaremos productos de origen animal")
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
        print("Se ve que usted va a lo clásico, marchando un pan de hamburguesa")
        respuesta = True
    elif answerclass == "pan_brioche":
        print("Uy entonces usted debe de ser muy dulce, marchando el pan brioche")
        respuesta = True
    elif answerclass == "pan_chapata":
        print("Pues le pondremos un pan de chapata")
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
        print("El plato número uno de los veganos eeh, marchando el tofu")
        respuesta = True
    elif answerclass == "falafel":
        print("Poca gente se lo pide, pero todos terminan repitiendo, tucarne de falafel está apuntada")
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
        print("Qué sería una hamburguesa sin carne de ternera eh...")
        respuesta = True
    elif answerclass == "pollo":
        print("La nueva moda de pedirse la hamburguesa de pollo, si yo te contara cómo los preparamos fipabas xddd")
        respuesta = True


print("¿Cuál es su nombre?")
respuesta = False
while respuesta==False:
    answer_nombre()


while repeat:

    print("Es usted vegano o tiene alguna preferencia en la comida?")
    respuesta = False
    while respuesta==False:
        answer_preferencia()


    print("Qué tipo de pan prefiere usted para la hamburguesa?")
    respuesta = False
    while respuesta==False:
        answer_pan()


    if(preferencia == "vegano"):
        print("Qué tipo de carne vegana prefiere para la hamburguesa?")
        respuesta = False
        while respuesta==False:
            answer_carne_veg()
    elif(preferencia == "carnivoro"):
        print("Qué tipo de carne carnivora prefiere para la hamburguesa?")
        respuesta = False
        while respuesta==False:
            answer_carne_car()


    '''repetir = str(input("Quiere hacer otro pedido? s/n:\n"))
    repetir.lower()
        
    if(repetir=="n" or "no"):
        print("Ok, adios.")
        print(repetir)
        repeat = False
    else:
        print("Guay!")
        print(repetir)'''


'''while True:
    answer_question()'''

