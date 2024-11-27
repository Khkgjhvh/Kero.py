from tkinter import*
#_________def__________
def pro_print():
	pro=Tk()
	pro.title('hello')
	pro.geometry('750x1500')
	pro.overrideredirect(True)
	root.withdraw()
	pro.mainloop()
#________def 1________	
	
def pro1_print():
	pro1=Tk()
	pro1.geometry('750x1500')
	pro1.overrideredirect(True)
	pro1=mainloop()
#_________def 2 _______	
def pro2_print():
	pro2=Tk()
	pro2.geometry('750x1500')
	pro2.overrideredirect(True)
	
	pro2.mainloop()
#___________def 3_____

def pro3_print():
	pro3=Tk()
	pro3.geometry('750x1500')
	pro3.overrideredirect(True)
	pro3.mainloop()
	



root= Tk()


root.config(background='#D5DBDB')
#_________label_________


lab=Label(root,text='python',bg='black',fg='white',font=('Courler',15))
lab.pack(fill=X)

frl=Frame(root,bg='whitesmoke',width='650',height='700')
frl.pack(pady=30)


frl1=Frame(root,bg='whitesmoke',width='650',height='700')
frl1.pack(pady=25)

#_________Button______

btn=Button(frl,text='python',width=25,font=('Courler',9),bg='#76D7C4',command=pro_print)
btn.place(x='60',y='30')


btn=Button(frl,text='python1',width=25,font=('Courler',9),bg='#76D7C4',command=pro1_print)
btn.place(x='60',y='150')


btn=Button(frl,text='python2',width=25,font=('Courler',9),bg='#76D7C4',command=pro2_print)
btn.place(x='60',y='250')


btn=Button(frl,text='python3',width=25,font=('Courler',9),bg='#76D7C4',command=pro3_print)
btn.place(x='60',y='350')



root.mainloop()
