from tkinter import *
from PIL import Image,ImageTk
root = Tk()
root.title('Royal Enfield Hunter')
root.geometry("1500x1000")
root.configure(border=4,background='white')

img = (Image.open("jupi.png"))

resized_image = img.resize((450,300),Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
bikename = Label(root,bg='white',text="Specifications of TVS Jupiter",font=('Microsoft YaHei UI Light',27,'bold'))
bikename.place(x=25,y=40)
Label(root,image=new_image,bg='white').place(x=45,y=150)

subhead = Label(root,bg='white',text="TVS Jupiter",font=('Microsoft YaHei UI Light',23,'bold'))
subhead.place(x=550,y=150)


sp1 = Label(root,bg='white',text='Mileage(overall)    -',font=('Microsoft YaHei UI Light',15,))
sp1.place(x=45,y=500)
sp2 = Label(root,bg='white',text='Engine Type         4stroke,CVTi fuel injection ',font=('Microsoft YaHei UI Light',15,))
sp2.place(x=45,y=530)
sp3 = Label(root,bg='white',text='Fuel capacity       6L',font=('Microsoft YaHei UI Light',15,))
sp3.place(x=45,y=560)
sp4 = Label(root,bg='white',text='Max Power           7.88PS @ 7500rpm',font=('Microsoft YaHei UI Light',15,))
sp4.place(x=45,y=590)
sp5 = Label(root,bg='white',text='Front Brake          Drum',font=('Microsoft YaHei UI Light',15,))
sp5.place(x=45,y=620)

sp6 = Label(root,bg='white',text='Displacement             109.7cc',font=('Microsoft YaHei UI Light',15,))
sp6.place(x=550,y=500)
sp7 = Label(root,bg='white',text='Body type                -',font=('Microsoft YaHei UI Light',15,))
sp7.place(x=550,y=530)
sp8 = Label(root,bg='white',text='Speed meter            analog',font=('Microsoft YaHei UI Light',15,))
sp8.place(x=550,y=560)
sp9 = Label(root,bg='white',text='Odometer                 Digital',font=('Microsoft YaHei UI Light',15,))
sp9.place(x=550,y=590)
sp10 = Label(root,bg='white',text='Rear Brake                Drum',font=('Microsoft YaHei UI Light',15,))
sp10.place(x=550,y=620)
mainloop()