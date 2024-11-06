import tkinter as tk
from tkinter import messagebox

def gravar():
    messagebox.showinfo('Boa noite','Boa noite, '+ entryNome.get()+'!+')

janela = tk.Tk()
tela_largura = 800
tela_altura  = 600

janela.geometry(f'{tela_largura}x{tela_altura}')

labelTitulo = tk.Label(janela,text='Meu Programa')
labelTitulo.place(x=350,y=10)

labelNome = tk.Label(janela,text='Digite seu nome')
labelNome.place(x=50,y=100)
entryNome = tk.Entry(janela)
entryNome.place(x=50,y=120,width=300)

labelIdade = tk.Label(janela,text='Digite sua idade')
labelIdade.place(x=50,y=150)
entryIdade = tk.Entry(janela)
entryIdade.place(x=50,y=170,width=50)

buttonGravar = tk.Button(janela,text='Gravar',command=gravar)
buttonGravar.place(x='170',y='250',width=100)


janela.mainloop()

