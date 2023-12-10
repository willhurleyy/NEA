from tkinter import *
import random
from PIL import ImageTk, Image
import requests
from io import BytesIO
root = Tk()
root.title("poker")
root.geometry("800x600")
root.configure(bg="green")

my_frame = Frame(root, bg="green")
my_frame.pack(pady=10)

def resize_card(image):
    new_image = image.resize((150, 218))
    return ImageTk.PhotoImage(new_image)
def shuffle():
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    values = range(2,15)
    global deck
    deck = []
    for suit in suits:
        for value in values:
            deck.append((str(value) +'_of_'+ suit))
    print(deck)
    
    global player1, player2 
    player1 = []
    player2 = []
    player1.append(random.choice(deck))
    deck.remove(player1[-1])
    player2.append(random.choice(deck))
    deck.remove(player2[-1])

    global player1_image, player2_image
    player1_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/" + player1[-1] + ".png"))
    player2_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/" + player2[-1] + ".png"))
    player1_label.config(image = player1_image)
    player2_label.config(image = player2_image)

def deal():
    player1.append(random.choice(deck))
    deck.remove(player1[-1])
    player2.append(random.choice(deck))
    deck.remove(player2[-1])
    print(player1[-1])
    print(player2[-1])
    global player1_image, player2_image
    player1_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/" + player1[-1] + ".png"))
    player2_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/" + player2[-1] + ".png"))
    player1_label.config(image = player1_image)
    player2_label.config(image = player2_image)


player1_frame = LabelFrame(my_frame, text = "Player 1", bd = 0)
player1_frame.grid(row=0, column=0, padx=10)
player2_frame = LabelFrame(my_frame, text = "Player 2", bd = 0)
player2_frame.grid(row=0, column=1, padx=10)

player1_label = Label(player1_frame, text = "")
player1_label.grid(row=0, column=0, padx=10)
player2_label = Label(player2_frame, text = "")
player2_label.grid(row=0, column=0, padx=10)

shuffle_button = Button(root, text = "Shuffle", command = shuffle)
shuffle_button.pack(pady=10)

deal_button = Button(root, text = "Deal", command = deal)
deal_button.pack(pady=10)

shuffle()




root.mainloop()
