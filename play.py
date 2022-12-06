import random

play_again = True

while(play_again):

    random_num = random.randint(0,100)

    nbTry = 5

    for i in range(1,nbTry+1):
        try:
            input_num = int(input("Entrez le nombre mistere, entre 1 a 100: \n"))

            if input_num < random_num:
                print("C'est plus grand")
            elif input_num > random_num:
                print("C'est plus petit")
            else:
                print("Vous avez gagné!!!")
                break
            
            if i == nbTry:
                print("Vous avez perdu")
                print(f"Le nombre etait ({random_num})")
                break
            else:
                print(f"Il vous reste : ({nbTry-i}) chance(s)")
            
        except:
            pass

    try:
        retry = input('Voulez-vous recommencer? "oui" ou "Non" : \n')

        if retry != "oui":
            play_again = False
    except:
        pass
