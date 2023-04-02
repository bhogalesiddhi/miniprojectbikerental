from tkinter import *
from PIL import Image , ImageTk

root = Tk()
root.title('View Bikes')
root.geometry("1500x1000")
root.configure(background="lightblue")

heading = Label(root,text ='Choose your Bike',bg='lightblue',font=('Microsoft YaHei UI Light',26,'bold'))
heading.place(x=600,y=30)

pic = PhotoImage(file='downloadimg.gif')
# pic1 = PhotoImage(file='enfield_royal.png')
# pic1 = PhotoImage(file="honda.png")
# pic = PhotoImage(file="activa.png")
enfield_image = Image.open("enfield_royal.png")
enfield_image_resized = enfield_image.resize((400, 250), Image.ANTIALIAS)  # Resizing the image
enfield_photo = ImageTk.PhotoImage(enfield_image_resized)
btn1 = Button(root, image=enfield_photo)


def bike1():
     root.destroy()
     import bike1details

btn1 = Button(root,image=enfield_photo,command=bike1)
btn1.pack(expand=True, fill=BOTH)
btn1.place(x=40,y=100)


btn2 = Button(root,image=pic)
# btn2.pack(expand=True, fill=BOTH)
btn2.place(x=20,y=400)



btn3 = Button(root,image=pic)
btn3.place(x=510,y=100)

btn4 = Button(root,image=pic)
btn4.place(x=510,y=400)

btn5 = Button(root,image=pic)
btn5.place(x=1000,y=100)

btn6 = Button(root,image=pic)
btn6.place(x=1000,y=400)
mainloop()