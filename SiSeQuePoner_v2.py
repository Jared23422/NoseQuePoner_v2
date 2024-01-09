print(" Hola, a continuacion preguntame palabras que no entiendas en ingles")
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "Una respuesta a una broma",
            "SHEESH": "Ligera desaprobación" ,
            "CREEPY": "Aterrador, siniestro" ,
            "AGGRO": "ponerse agresivo/enojado" ,
            "WDYM": "es una abreviacion de what do you mean que en español seria, que quieres decir"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print (meme_dict[word])
else:
    print ("ni yo se que significa")
word2 = input("Si te queda alguna otra palabra dimela (¡con mayúsculas!): ")
if word2 in meme_dict.keys():
    print (meme_dict[word2])
else:
    print ("ni yo se que significa")
word3 = input("Si te queda alguna otra palabra dimela (¡con mayúsculas!): ")
if word3 in meme_dict.keys():
    print (meme_dict[word3])
else:
    print ("ni yo se que significa")
word4 = input("Si te queda alguna otra palabra dimela (¡con mayúsculas!): ")
if word4 in meme_dict.keys():
    print (meme_dict[word4])
else:
    print ("ni yo se que significa")
word5 = input("Si te queda alguna otra palabra dimela (¡con mayúsculas!): ")
if word5 in meme_dict.keys():
    print (meme_dict[word5])
else:
    print ("ni yo se que significa")
