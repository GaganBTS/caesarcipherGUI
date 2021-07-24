from tkinter import *
from tkinter import messagebox

import pyperclip






alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
  , 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'
  , 'u', 'v', 'w', 'x', 'y', 'z',]

def decoding():
  caesar("decode")
def encoding():
  caesar("encode")
def caesar(cipher_direction):


 try:
     shift_amount = [int(chars) for chars in shift_entry.get()]
 except:
     messagebox.showerror(title="INVALID SHIFT NUMBER",message="please enter valid shift number")
 else:
  start_text = text_entry.get().lower()
  if start_text=="" or shift_entry.get()=="":
      messagebox.showerror(title="INVALID INPUTS",message="PLease fill out every input field validly")

  else:
   shift = shift_amount[0] % 26
   end_text = ""
   if cipher_direction == "decode":
    shift_amount[0] *= -1
   for char in start_text:


    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount[0]
      end_text += alphabet[new_position]
    else:
      end_text += char
   safe_text.insert(0,end_text)
   pyperclip.copy(end_text)
def clearing():
  text_entry.delete(0,END)
  shift_entry.delete(0,END)
  safe_text.delete(0,END)
  text_entry.focus()


































# ------------------------- UI SETUP ---------------- #
window = Tk()
window.title('CAESAR CIPHER')
window.config(padx=30,pady=30,bg='white')

#canvas
canvas = Canvas(height = 300,width=300,highlightthickness=0,bg='white')
caesar_logo = PhotoImage(file ="caesar.png")
canvas.create_image(135,100,image=caesar_logo)
canvas.grid(row=0,column=1)
#labels
text_label = Label(text="Enter your text: ",bg="white")
text_label.grid(row=1,column=0)
shift_label = Label(text="Enter the shift number: ",bg="white")
shift_label.grid(row=2,column=0)
enc_Text = Label(text='Safe text:',bg="white")
enc_Text.grid(row=4,column=0)
#enteries
text_entry = Entry(width=35)
text_entry.grid(row=1,column=1)
text_entry.focus()
shift_entry = Entry(width=35)
shift_entry.grid(row=2,column=1)
safe_text = Entry(width=35)
safe_text.grid(row=4,column=1)
#buttons
encode_btn = Button(text="ENCODE",width=10,bg="white",command=encoding,highlightthickness=0)
encode_btn.grid(row=2,column=2,pady=3)

decode_btn = Button(text="DECODE",width=10,bg="white",command=decoding,highlightthickness=0)
decode_btn.grid(row=3,column=2,pady=3)
clear = Button(text="CLEAR",bg="white",command=clearing)
clear.grid(row=4,column=2,pady=3)

window.mainloop()
