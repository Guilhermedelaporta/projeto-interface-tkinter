import tkinter as tk

root = tk.Tk()  #cria a janela principal do aplicativo (a root window)
root.title("Interface") #define o titulo da janela que aparece na barra superior 
root.geometry("400x300")  # Define o tamanho da janela
root.configure(bg="blue")  # altera a cor de fundo da janela azul 

# Label para texto inicial
label = tk.Label(root, text="Digite seu nome: ", font=("Arial", 14), bg="blue", fg="white") # tk.Label cria um rótulo de texto na interface
label.pack(pady=20)  # pack posiciona o rotulo na janela, pady adiciona um espaço vertical 

# Entrada de texto
entrada = tk.Entry(root, font=("Arial", 14)) # tk.Entry cria um campo de entrada para o usuário digitar
entrada.pack(pady=10)  # pack posiciona o rótulo na janela e pady adiciona espaçamento vertical

# Função para exibir o texto digitado
def exibirTexto(): #função para exibir o texto 
    texto = entrada.get() #Obtem o texto digitado no campo de entrada 
    print(f"Você digitou: {texto}") #mostra o texto no console 

# Função para limpar o campo de entrada
def limparTexto(): #funçao para limpar o texto digitado 
    entrada.delete(0, tk.END) #entrada.delete apaga o campo de entrada(0 apaga do inicio e tk.END até o final)

# Frame para botões
frameBotoes = tk.Frame(root, bg="blue") #tk.Frame cria um container para organizar widgets(neste caso os botoes), root diz que o frame pertence a janela principal
frameBotoes.pack(pady=10) #pack defini o espaçamento vertical 

# Botão "Enviar"
btnEnviar = tk.Button(frameBotoes, text="Enviar", font=("Arial", 14), bg="green", fg="white", command=exibirTexto) # tk.Button cria um botão iterativo, frame botoes: o botao será colocado no frame de botões, o command=exibirTexto especifica a função que será chamada quando o botão for clickado
btnEnviar.pack(side=tk.LEFT, padx=5)

# Botão "Limpar"
btnLimpar = tk.Button(frameBotoes, text="Limpar", font=("Arial", 14), bg="red", fg="white", command=limparTexto)
btnLimpar.pack(side=tk.LEFT, padx=5) #pack posiciona o botao no lado esquerdo do frame, padx adiciona espaçamento horizontal

# Inicia o loop principal
root.mainloop() # inicia o loop de eventos do Tkinter
