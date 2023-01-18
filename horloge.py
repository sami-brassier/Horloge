import time

def afficher_heure(heure, alarme):
    while True:
        print(f"{heure[0]:02d}:{heure[1]:02d}:{heure[2]:02d}")
        if heure[0] == alarme[0] and heure[1] == alarme[1] and heure[2] == alarme[2]:
            print("Alarme!")
        heure[2] += 1
        if heure[2] == 60:
            heure[2] = 0
            heure[1] += 1
        if heure[1] == 60:
            heure[1] = 0
            heure[0] += 1
        if heure[0] == 24:
            heure[0] = 0
        time.sleep(1)

def regler_heure(nouvelle_heure):
    heure[0] = nouvelle_heure[0]
    heure[1] = nouvelle_heure[1]
    heure[2] = nouvelle_heure[2]

def regler_alarme(nouvelle_alarme):
    alarme[0] = nouvelle_alarme[0]
    alarme[1] = nouvelle_alarme[1]
    alarme[2] = nouvelle_alarme[2]

heure = [16, 30, 0]
alarme = [16, 30, 10]
nouvelle_heure = (16, 30, 5)
nouvelle_alarme = (16, 30, 20)

regler_heure(nouvelle_heure)
regler_alarme(nouvelle_alarme)

afficher_heure(heure, alarme)