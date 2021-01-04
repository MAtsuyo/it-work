import random
print("carta,forbici,bomba")
computer=random.randint(0,2)
if computer==0: 
    computer="s"
elif computer==1: 
    computer="f"
else: computer="c"
utente=input("Inserisci c per carta, s per sasso ed f per forbice: ")
if utente!="s" and utente!="f" and utente!="c":
    print("La lettera non corrisponde a nulla")
elif utente==computer:
        print("parità!")
elif utente=="s" and computer=="f" or utente=="f" and computer=="c" or utente=="c" and computer=="s":
    print("Hai vinto!")
else:
    print("Ha vinto il computer!")