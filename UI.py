from tkinter import *
from tkinter import filedialog
from tkinter import font


root=Tk()
root.title('LAALM foundation')
root.iconbitmap(r'C:\Users\saihr\Documents\project\.vscode\icon.ico')
root.geometry("1000x600")




#main frame
my_frame=Frame(root)
my_frame.pack(pady=5)

#scroll bar
text_scroll=Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)



# text box
my_text=Text(my_frame, width=97, height=25, font=("TimesNewRoman",16),selectbackground="yellow", selectforeground="black",undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

#config scrollbar
text_scroll.config(command=my_text.yview)

#menu
my_menu = Menu(root)
root.config(menu=my_menu)


#status bar at bottom
status_bar=Label(root, text='Ready        ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

root.mainloop()