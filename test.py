import tkinter as tk
from ctypes import windll

root = tk.Tk()
root.title('The Game Corner')

#create label
message = tk.Label(root, text="Hello, World!")
message.pack()
message2 = tk.Label(root, text="Let's play a game!")
message2.pack()

#address the blur
windll.shcore.SetProcessDpiAwareness(1)

#keep window open
root.mainloop()