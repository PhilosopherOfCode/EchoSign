from PIL import Image
from PIL import ImageTk

import tkinter as tk
from tkinter import ttk

import json

#window
window = tk.Tk()		
window.title('SignoGlove')
window.geometry('700x800')
window.configure(bg='blue')

background_image=tk.PhotoImage(file = "C:\\Users/Emmanuel\\Dropbox/My PC (DESKTOP-3AI9NQB)\\Downloads\\Signo Glove\\Textures\\OIG.png")
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

TTT_Button = tk.PhotoImage(file='C:\\Users\Emmanuel\\Dropbox\\My PC (DESKTOP-3AI9NQB)\\Downloads\\Signo Glove\\Textures\\TTS-removebg-preview_mini.png')
Edit_audio_Btton = tk.PhotoImage(file="C:\\Users\\Emmanuel\\Dropbox\\My PC (DESKTOP-3AI9NQB)\\Downloads\\Signo Glove\\Textures\\AUDIO_Profile-removebg-preview_mini.png")



def Edit_TTS_Profile():
	Edit_audio.pack_forget()
	TTS.pack_forget()
	title_label.pack_forget()
	scale.pack(pady=350)
	title_label.place_forget()
	
	Back.place(x=260, y=5)
 

def Back():
    scale.pack_forget()
    Back.place_forget()
    title_label.place(x=260, y=5)
    title_label.lift()
    
    
    Edit_audio.pack(pady = 50)
    TTS.pack(pady = 20)


# Header
title_label = tk.Label(master = window, text = 'SignoGlove', font = 'SegoeUI 24 bold italic')
title_label.pack(side = 'top', anchor = 'n')

# Buttons

#input_frame = tk.Frame(master = window)
#input_frame.configure(bg = 'blue')
Back = tk.Button(window,text = 'Back', command = Back )
scale = tk.Scale(window,from_ = 0,to = 100, orient = 'horizontal', label = 'Volume', length = 200, width = 20, font = ('Consolas', 15 ) )
Back.configure(height=5,width=20)
Edit_audio = tk.Button(window,text = 'Edit audio profile', command = Edit_TTS_Profile, image= Edit_audio_Btton, compound = 'top', font= ('Comic Sans' , 20))
Edit_audio.pack(pady = 50)

TTS = tk.Button(window,text = 'Text to speech', image= TTT_Button, compound = 'top', font= ('Comic Sans' , 20))

TTS.pack(pady = 20)

#input_frame.pack()

#if Edit_audio 

#run
window.mainloop()
