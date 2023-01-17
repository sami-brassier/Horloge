import time

def afficher_heure(heure):
    while True:
        print(f"{heure[0]:02d}:{heure[1]:02d}:{heure[2]:02d}")
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

heure = [16, 30, 0]

afficher_heure(heure)