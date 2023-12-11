from tkinter import *
import random
from PIL import ImageTk, Image
import requests
root = Tk()
root.title("poker")
root.geometry("1920x1080")
root.configure(bg="green")
my_frame = Frame(root, bg="green")
my_frame.pack(pady=10)
global noplayers
noplayers = 2
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
    
    global player1, player2, middlecards
    player1 = []
    player2 = []
    middlecards = []
    player1.append(random.choice(deck))
    deck.remove(player1[-1])
    player1.append(random.choice(deck))
    deck.remove(player1[-1])
    player2.append(random.choice(deck))
    deck.remove(player2[-1])
    player2.append(random.choice(deck))
    deck.remove(player2[-1])
    middlecards.append(random.choice(deck))
    deck.remove(middlecards[-1])
    middlecards.append(random.choice(deck))
    deck.remove(middlecards[-1])
    middlecards.append(random.choice(deck))
    deck.remove(middlecards[-1])
    middlecards.append(random.choice(deck))
    deck.remove(middlecards[-1])
    middlecards.append(random.choice(deck))
    deck.remove(middlecards[-1])


    global player1card1_image, player1card2_image, player2card1_image, player2card2_image, middlecard1_image, middlecard2_image, middlecard3_image, middlecard4_image, middlecard5_image
    player1card1_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/" + player1[-1] + ".png"))
    player1card2_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/" + player1[-2] + ".png"))
    player2card1_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/" + player2[-1] + ".png"))
    player2card2_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/" + player2[-2] + ".png"))
    middlecard1_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/card-face-down.png"))
    middlecard2_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/card-face-down.png"))
    middlecard3_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/card-face-down.png"))
    middlecard4_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/card-face-down.png"))
    middlecard5_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/card-face-down.png"))
    middlecard1_label.config(image = middlecard1_image)
    middlecard2_label.config(image = middlecard2_image)
    middlecard3_label.config(image = middlecard3_image)
    middlecard4_label.config(image = middlecard4_image)
    middlecard5_label.config(image = middlecard5_image)

    player1card1_label.config(image = player1card1_image)
    player1card2_label.config(image = player1card2_image)
    player2card1_label.config(image = player2card1_image)
    player2card2_label.config(image = player2card2_image)

    root.title("poker" + str(len(deck)))

def deal():
    player1.append(random.choice(deck))
    deck.remove(player1[-1])
    player1.append(random.choice(deck))
    deck.remove(player1[-1])
    player2.append(random.choice(deck))
    deck.remove(player2[-1])
    player2.append(random.choice(deck))
    deck.remove(player2[-1])
    middlecards.append(random.choice(deck))
    deck.remove(middlecards[-1])
    middlecards.append(random.choice(deck))
    deck.remove(middlecards[-1])
    middlecards.append(random.choice(deck))
    deck.remove(middlecards[-1])
    middlecards.append(random.choice(deck))
    deck.remove(middlecards[-1])
    middlecards.append(random.choice(deck))
    deck.remove(middlecards[-1])
    global player1card1_image, player1card2_image, player2card1_image, player2card2_image, middlecard1_image, middlecard2_image, middlecard3_image, middlecard4_image, middlecard5_image
    player1card1_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/" + player1[-1] + ".png"))
    player1card2_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/" + player1[-2] + ".png"))
    player2card1_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/" + player2[-1] + ".png"))
    player2card2_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/" + player2[-2] + ".png"))
    player1card1_label.config(image = player1card1_image)
    player1card2_label.config(image = player1card2_image)
    player2card1_label.config(image = player2card1_image)
    player2card2_label.config(image = player2card2_image)
    middlecard1_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/card-face-down.png"))
    middlecard2_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/card-face-down.png"))
    middlecard3_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/card-face-down.png"))
    middlecard4_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/card-face-down.png"))
    middlecard5_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/card-face-down.png"))
    middlecard1_label.config(image = middlecard1_image)
    middlecard2_label.config(image = middlecard2_image)
    middlecard3_label.config(image = middlecard3_image)
    middlecard4_label.config(image = middlecard4_image)
    middlecard5_label.config(image = middlecard5_image)
    root.title("poker" + str(len(deck)))

    if len(deck) < 5+(2*noplayers):
        shuffle()

def facedown():
    global player1card1_image, player1card2_image, player2card1_image, player2card2_image
    player1card1_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/card-face-down.png"))
    player1card2_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/card-face-down.png"))
    player2card1_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/card-face-down.png"))
    player2card2_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/card-face-down.png"))
    player1card1_label.config(image = player1card1_image)
    player1card2_label.config(image = player1card2_image)
    player2card1_label.config(image = player2card1_image)
    player2card2_label.config(image = player2card2_image)

def faceup():
    global player1card1_image,player1card2_image, player2card1_image, player2card2_image
    player1card1_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/" + player1[-1] + ".png"))
    player1card2_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/" + player1[-2] + ".png"))
    player2card1_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/" + player2[-1] + ".png"))
    player2card2_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/" + player2[-2] + ".png"))
    player1card1_label.config(image = player1card1_image)
    player1card2_label.config(image = player1card2_image)
    player2card1_label.config(image = player2card1_image)
    player2card2_label.config(image = player2card2_image)

def flop():
    global middlecard1_image, middlecard2_image, middlecard3_image
    middlecard1_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/" + middlecards[-1] + ".png"))
    middlecard2_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/" + middlecards[-2] + ".png"))
    middlecard3_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/" + middlecards[-3] + ".png"))
    middlecard1_label.config(image = middlecard1_image)
    middlecard2_label.config(image = middlecard2_image)
    middlecard3_label.config(image = middlecard3_image)
def turn():
    global middlecard4_image
    middlecard4_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/" + middlecards[-4] + ".png"))
    middlecard4_label.config(image = middlecard4_image)
def river():
    global middlecard5_image
    middlecard5_image = resize_card(Image.open("C:/Users/willi/Downloads/PNG-cards-1.3/" + middlecards[-5] + ".png"))
    middlecard5_label.config(image = middlecard5_image)

player1card1_frame = LabelFrame(my_frame, text = "Player 1", bd = 0)
player1card1_frame.grid(row=0, column=1, pady=50)
player1card2_frame = LabelFrame(my_frame, text = "Player 1", bd = 0)
player1card2_frame.grid(row=0, column=2, pady=50)
player2card1_frame = LabelFrame(my_frame, text = "Player 2", bd = 0)
player2card1_frame.grid(row=2, column=1, pady=100)
player2card2_frame = LabelFrame(my_frame, text = "Player 2", bd = 0)
player2card2_frame.grid(row=2, column=2 , pady=100)

player1card1_label = Label(player1card1_frame, text = "")
player1card1_label.grid(row=0, column=0)
player1card2_label = Label(player1card2_frame, text = "")
player1card2_label.grid(row=0, column=0)
player2card1_label = Label(player2card1_frame, text = "")
player2card1_label.grid(row=0, column=0)
player2card2_label = Label(player2card2_frame, text = "")
player2card2_label.grid(row=0, column=0)


middlecard1_frame = LabelFrame(my_frame, text = "Flop", bd = 0)
middlecard1_frame.grid(row=1, column=0, pady=50)
middlecard2_frame = LabelFrame(my_frame, text = "Flop", bd = 0)
middlecard2_frame.grid(row=1, column=1, pady=50)
middlecard3_frame = LabelFrame(my_frame, text = "Flop", bd = 0)
middlecard3_frame.grid(row=1, column=2, pady=50)
middlecard4_frame = LabelFrame(my_frame, text = "Turn", bd = 0)
middlecard4_frame.grid(row=1, column=3, pady=50)
middlecard5_frame = LabelFrame(my_frame, text = "River", bd = 0)
middlecard5_frame.grid(row=1, column=4, pady=50)

middlecard1_label = Label(middlecard1_frame, text = "")
middlecard1_label.grid(row=0, column=0)
middlecard2_label = Label(middlecard2_frame, text = "")
middlecard2_label.grid(row=0, column=0)
middlecard3_label = Label(middlecard3_frame, text = "")
middlecard3_label.grid(row=0, column=0)
middlecard4_label = Label(middlecard4_frame, text = "")
middlecard4_label.grid(row=0, column=0)
middlecard5_label = Label(middlecard5_frame, text = "")
middlecard5_label.grid(row=0, column=0)


shuffle_button = Button(root, text = "Shuffle", command = shuffle)
shuffle_button.pack(pady=0)
shuffle_button.place(x=50, y=500)

deal_button = Button(root, text = "Deal", command = deal)
deal_button.pack(pady=0)
deal_button.place(x=102, y=500)

facedown_button = Button(root, text = "Facedown", command = facedown)
facedown_button.pack(pady=0)
facedown_button.place(x=140, y=500)

faceup_button = Button(root, text = "Faceup", command = faceup)
faceup_button.pack(pady=0)
faceup_button.place(x=210, y=500)
shuffle()
flop_button = Button(root, text = "Flop", command = flop)
flop_button.pack(pady=0)
flop_button.place(x=265, y=500)

turn_button = Button(root, text = "Turn", command = turn)
turn_button.pack(pady=0)
turn_button.place(x=305, y=500)

river_button = Button(root, text = "River", command = river)
river_button.pack(pady=0)
river_button.place(x=345, y=500)


root.mainloop()
