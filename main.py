# --- imports ---
from decript import decripts
from encript import encripts
import tkinter as tk
#setup
root = tk.Tk()
root.title("ANOM: Encript / Decript Software")

encriptedMessage=""
encriptedKey=""
decriptedMessage=""
decriptedKey = tk.StringVar()
decriptedKey.set("Randomized Key: not generated")
#functions
def encriptRaise():
  encript_Frame.tkraise()

def decriptRaise():
  decript_Frame.tkraise()

def menuRaise():
  menu_Frame.tkraise()

def consoleInterface():
  whatDo = input("What would you like to do?\n  Encript (e) -> Encript a message using this program\n  Decript (d) -> Decript a message that was encripted\nChoose one: ").lower()
  if whatDo == "encript" or whatDo == "e":
    message = input("\nInput a message to encript: ")
    print("\nEncripting message...")
    contents = encripts(message)
    message = contents[0]
    key = contents[1]
    print("\nHere is the encripted message: {}".format(message))
    print("\nHere is the private key: {}".format(key))
  elif whatDo == "decript" or whatDo == "d":
    message = input("\nInput a message to decript: ")
    key = input("\nInput the private key: ")
    print("\nDecripting message...")
    decripted = decripts(message, key)
    print("\nHere is the decripted message: {}".format(decripted))

def submitEncript():
  global encriptedMessage, encriptedKey
  message = etr_MessageEncript.get("1.0","end-1c")
  etr_MessageEncript.delete("1.0","end")
  contents = encripts(message)
  encriptedMessage = "{}".format(contents[0])
  encriptedKey = contents[1]
  decriptedKey.set("Random Key: {}".format(contents[1]))
  etr_MessageEncript.insert("1.0",encriptedMessage)
  
def dumpEncript():
  if encriptedMessage == "":
    print("Nothing has been encripted yet")
  else:
    print("\nHere is the encripted message: {}".format(encriptedMessage))
    print("\nHere is the random key: {}".format(encriptedKey))

def submitDecript():
  global decriptedMessage
  message = etr_DecriptMessage.get("1.0","end-1c")
  key = etr_DecriptKey.get("1.0","end-1c")
  etr_DecriptMessage.delete("1.0","end")
  decriptedMessage = decripts(message, key)
  etr_DecriptMessage.insert("1.0",decriptedMessage)

def dumpDecript():
  if decriptedMessage == "":
    print("Nothing has been decripted yet")
  else:
    print("\nHere is the decripted message: {}".format(decriptedMessage))

def quit():
  root.destroy()
#tkinter >menu Frame
menu_Frame = tk.Frame(root, highlightbackground="Blue", highlightthickness=3)
menu_Frame.grid(column=0, row=0, sticky="news")

lbl_Menu = tk.Label(menu_Frame, text="Choose one of the options below:", font=("Arial", 20))
lbl_Menu.grid(column=0, row=0, columnspan=2, pady=20, padx=5)

btn_MenuEncript = tk.Button(menu_Frame, text="Encript", command=encriptRaise)
btn_MenuEncript.grid(column=0, row=1, sticky='nesw')

btn_MenuDecript = tk.Button(menu_Frame, text = "Decript", command=decriptRaise)
btn_MenuDecript.grid(column=1, row=1, sticky='nesw')

btn_MenuConsole = tk.Button(menu_Frame, text="Use Console Interface", command=consoleInterface)
btn_MenuConsole.grid(column=0, row=2, columnspan=2, sticky="news")

btn_MenuQuit = tk.Button(menu_Frame, text="Quit", command=quit)
btn_MenuQuit.grid(column=0, row=3, columnspan=2, sticky='nesw')

# >Encription Frame
encript_Frame = tk.Frame(root, highlightbackground="Red", highlightthickness=3)
encript_Frame.grid(column=0, row=0, sticky="news")

lbl_Encript = tk.Label(encript_Frame, text="Encripter", font=("Arial", 10))
lbl_Encript.grid(column=0, row=0, sticky='nesw', columnspan=2, pady=5)

lbl_MessageEncript = tk.Label(encript_Frame, text ="Encript Message:", width=20)
lbl_MessageEncript.grid(row=1, column=0, sticky='nesw', rowspan=2)

etr_MessageEncript = tk.Text(encript_Frame, width=25, height=2)
etr_MessageEncript.grid(row=1, column=1, sticky='nesw')

lbl_KeyEncript = tk.Label(encript_Frame, textvariable=decriptedKey)
lbl_KeyEncript.grid(row=4, column=0, sticky="news", columnspan=2)

btn_EncriptSubmit = tk.Button(encript_Frame, text="Submit", width=52, command=submitEncript)
btn_EncriptSubmit.grid(row=5, column=0, columnspan=2, stick="news")

btn_EncriptGoBack = tk.Button(encript_Frame, text="Go Back", command=menuRaise)
btn_EncriptGoBack.grid(column=0, row=6, sticky="news")

btn_EncriptDump = tk.Button(encript_Frame, text="Dump Into Console", command=dumpEncript)
btn_EncriptDump.grid(column=1, row=6, sticky="news")

# >Decription Frame
decript_Frame = tk.Frame(root, highlightbackground="Brown", highlightthickness=3)
decript_Frame.grid(column=0, row=0, sticky="news")

lbl_Decript = tk.Label(decript_Frame, text="Decript (Don't use [])", font=("Arial", 10))
lbl_Decript.grid(column=0, row=0, columnspan=2, sticky="news", pady=5)

lbl_DecriptMessage = tk.Label(decript_Frame, text="Decript Message:")
lbl_DecriptMessage.grid(row=1, column=0, rowspan=2, sticky="news")

etr_DecriptMessage = tk.Text(decript_Frame, width=25, height=2,)
etr_DecriptMessage.grid(row=1, column=1, sticky="news",  pady=5)

lbl_DecriptKey = tk.Label(decript_Frame, text="Random Key:")
lbl_DecriptKey.grid(row=4, column=0, sticky="news")

etr_DecriptKey= tk.Text(decript_Frame, width=25, height=1)
etr_DecriptKey.grid(column=1, row=4, sticky="news")

btn_DecriptSubmit = tk.Button(decript_Frame, text="Submit", width=52, command=submitDecript)
btn_DecriptSubmit.grid(row=5, column=0, columnspan=2, stick="news")

btn_DecriptGoBack = tk.Button(decript_Frame, text="Go Back", command=menuRaise)
btn_DecriptGoBack.grid(column=0, row=6, sticky="news")

btn_DecriptDump = tk.Button(decript_Frame, text="Dump Into Console", command=dumpDecript)
btn_DecriptDump.grid(column=1, row=6, sticky="news")

menu_Frame.tkraise()

root.mainloop()
#calls
