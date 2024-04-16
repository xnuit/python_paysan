import pyautogui
import time
import random
import tkinter as tk

# Variables pour stocker les coordonnées du rectangle
start_x, start_y, end_x, end_y = None, None, None, None

# Fonction pour capturer le clic initial
def on_click(event):
    global start_x, start_y
    start_x, start_y = event.x, event.y

# Fonction pour capturer le relâchement du clic et définir la région
def on_release(event):
    global end_x, end_y
    end_x, end_y = event.x, event.y
    canvas.create_rectangle(start_x, start_y, end_x, end_y, outline='red', width=5)
    root.quit()

# Créez une fenêtre Tkinter
root = tk.Tk()
root.title("Définir une région")

# Créez un canevas pour l'interaction
canvas = tk.Canvas(root, bg='white', width=1920, height=1080)
canvas.pack()

# Attachez des gestionnaires d'événements pour capturer les clics de souris
canvas.bind("<ButtonPress-1>", on_click)
canvas.bind("<ButtonRelease-1>", on_release)

# Affichez la fenêtre Tkinter
root.mainloop()
# Une fois que la fenêtre est fermée, vous pouvez utiliser les coordonnées start_x, start_y, end_x, end_y
print(f"Coordonnées du coin supérieur gauche : ({start_x}, {start_y})")
print(f"Coordonnées du coin inférieur droit : ({end_x}, {end_y})")

# Calculez la largeur et la hauteur du rectangle
largeur = end_x - start_x
hauteur = end_y - start_y

# Définissez la région de l'écran où vous souhaitez effectuer la recherche
region = (start_x, start_y, largeur, hauteur)

# Effectuez la recherche d'image dans la région spécifiée avec un niveau de confiance
#image_position = pyautogui.locateOnScreen('C:/Users/User/Documents/BotPaysan/ble.png', region=region, confidence=0.9)

#if image_position:
    # Si l'image est trouvée dans la région spécifiée, effectuez des actions sur elle
    #pyautogui.click(image_position)

# Attendre avant de relancer le script
launch_time = random.uniform(3, 5)
time.sleep(launch_time)
n = 0
# Boucle principale pour exécuter les actions en continu
while n <= 10:

    # Génerer un un temps aléatoire
    sleep_time = random.uniform(1, 3)

    # Attendre quelques secondes avant de lancer le script
    time.sleep(sleep_time)

    # Rechercher et obtenir la position de l'image (blé)
    image_position = pyautogui.locateOnScreen('C:/Users/Abric/Documents/BotPaysan/ble.png', region=region, confidence=0.9)

    if image_position:
        # Cliquer sur le blé
        pyautogui.click(image_position)

        # Attendre
        time.sleep(1)

        # Rechercher le bouton à l'écran et obtenez sa position
        bouton_position = pyautogui.locateOnScreen('C:/Users/Abric/Documents/BotPaysan/faucher.png')

        if bouton_position:
            # Cliquer sur le bouton faucher
            pyautogui.click(bouton_position)
        else:    
            print("Bouton non trouvé.")
    else:
        print("Image non trouvée.")

    # attendre la fin de l'animation
sleep_time(10)
    # Incrémenter de 1 par action
n += 1


