# Apresentando o  valor da multa na janela principal.

import tkinter
import tkinter as tk
import tkinter.messagebox
janela = tkinter.Tk()
janela.geometry('800x600')
janela.title('Leitor de velocidade')

rotulovelocidade = tkinter.Label(janela, text='Insira a velocidade do automovel')
rotulovelocidade.pack()

campovelocidade = tkinter.Entry(janela)
campovelocidade.pack()   
    
    
def multa():
    if int(campovelocidade.get()) <= 80:
        tkinter.messagebox.showinfo('Dentro do limite', 'Não será multado!' )
        rotulocerto = tkinter.Label(janela, text='Não será multado!')
        rotulocerto.pack()
    else:
        tkinter.messagebox.showerror('Ultrapassou o limite', 'Será multado!' )
        rotuloerrado = tkinter.Label(janela, text='Valor da multa:')
        rotuloerrado.pack()
        calcular = (int(campovelocidade.get())-80)*5.00,'reais'
        valor_int = tk.IntVar()
        valor_int.set(calcular)
        rotulovalor = tkinter.Label(janela, textvariable=valor_int)
        rotulovalor.pack()
        
        
    
botao = tkinter.Button(janela, text='Checar multa', command = multa)
botao.pack()
    

janela.mainloop()



# Apresentando o valor da multa no script.

import tkinter
import tkinter.messagebox
janela = tkinter.Tk()
janela.geometry('800x600')
janela.title('Leitor de velocidade')

rotulovelocidade = tkinter.Label(janela, text='Insira a velocidade do automovel')
rotulovelocidade.pack()

campovelocidade = tkinter.Entry(janela)
campovelocidade.pack()   
    
    
def multa():
    if int(campovelocidade.get()) <= 80:
        tkinter.messagebox.showinfo('Dentro do limite', 'Não será multado!' )
        rotulocerto = tkinter.Label(janela, text='Não será multado!')
        rotulocerto.pack()
    else:
        tkinter.messagebox.showerror('Ultrapassou o limite', 'Será multado!' )
        rotuloerrado = tkinter.Label(janela, text='Será multado!')
        rotuloerrado.pack()
        calcular = (int(campovelocidade.get())-80)*5.00
        print(calcular, 'reais')
        
        
    
botao = tkinter.Button(janela, text='Checar multa', command = multa)
botao.pack()
    

janela.mainloop()
