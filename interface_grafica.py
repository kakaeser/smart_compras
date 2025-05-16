from customtkinter import *
import json
import os

class Interface:
    
    def __init__(self):
        self.senha = "839238098"
        self.nome = "3123131313"
        
        

    def salvar_dados(self, cpf, cep, email):
        dados_novo_usuario = {
            "nome": self.nome,
            "email": email,
            "cpf": cpf,
            "cep": cep,
            "senha": self.senha
        }

        dados_existentes = []  # Inicializa como lista vazia

        if os.path.exists("usuarios.json"):  # Verifica se o arquivo já existe
            with open("usuarios.json", "r") as arquivo:
                try:
                    dados_existentes = json.load(arquivo)  # Lê os dados do JSON
                    if not isinstance(dados_existentes, list):
                        dados_existentes = []  # Garante que seja uma lista
                except json.JSONDecodeError:
                    dados_existentes = []  # Se houver erro, mantém a lista vazia

        dados_existentes.append(dados_novo_usuario)  # Adiciona o novo usuário à lista

        with open("usuarios.json", "w") as arquivo:  # Salva a lista completa no JSON
            json.dump(dados_existentes, arquivo, indent=4)

    def carregar_dados(self, nome_usuario):
        if os.path.exists("usuarios.json"):
            with open("usuarios.json", "r") as arquivo:
                try:
                    dados = json.load(arquivo)
                    if isinstance(dados, list):  # Garante que seja uma lista
                        for usuario in dados:
                            if usuario.get("nome") == nome_usuario:  # Busca pelo nome
                                self.nome = usuario.get("nome", "")
                                self.senha = usuario.get("senha", "")
                                return  # Sai da função ao encontrar o usuário
                except json.JSONDecodeError:
                    pass  

    def App(self):
        ## Inicialização do app
        app = CTk()
        app.geometry("1280x720")
        

        ## Inicialização barra lateral
        barralat = CTkFrame(master = app, fg_color="#1bd1a4", corner_radius=0)
        barralat.place(relx = 0, rely = 0.5, relheight = 1, anchor = "center")
        app.mainloop()

    def cadastro(self):
        cadastro = CTk()
        cadastro.geometry("500x700")
        cadastro.title("Cadastrar")

        erro_label = CTkLabel(master=cadastro, text="", text_color="red")
        erro_label.place(relx=0.5, rely=0.85, anchor="center")

        textin = CTkLabel(master=cadastro, text="Insira os dados :", font = ("Montserrat", 12))
        textin.place(relx = 0.4, rely = 0.33, relwidth = 0.25, relheight = 0.08, anchor = "center")

        user = CTkEntry(master = cadastro, placeholder_text= "Nome")
        user.place(relx = 0.5, rely = 0.2, relwidth = 0.5, relheight = 0.08, anchor="center")

        email = CTkEntry(master= cadastro, placeholder_text="Email")
        email.place(relx = 0.5, rely = 0.3, relwidth = 0.5, relheight = 0.08, anchor="center")

        cpf = CTkEntry(master= cadastro, placeholder_text="CPF")
        cpf.place(relx = 0.5, rely = 0.4, relwidth = 0.5, relheight = 0.08, anchor="center")

        cep = CTkEntry(master= cadastro, placeholder_text="CEP")
        cep.place(relx = 0.5, rely = 0.5, relwidth = 0.5, relheight = 0.08, anchor="center")


        password = CTkEntry(master= cadastro, placeholder_text="Senha", show = "*")
        password.place(relx = 0.5, rely = 0.6, relwidth = 0.5, relheight = 0.08, anchor="center")

        cpassword = CTkEntry(master= cadastro, placeholder_text="Confirmar Senha", show = "*")
        cpassword.place(relx = 0.5, rely = 0.7, relwidth = 0.5, relheight = 0.08, anchor="center")

        def autenticar():
            if user.get() == "" or email.get() == "" or cpf.get() == "" or cep.get() == "" or password.get() == "" or cpassword.get() == "":
                erro_label.configure(text="Você não preencheu todos os campos!!")
            elif cpassword.get() != password.get():
                erro_label.configure(text="Sua senha não é a mesma que você quis confirmar")
            elif user.get() == self.carregar_dados(user.get()):
                erro_label.configure(text="Já existe um usuário com esse nome")
            else:
                self.nome = user.get()
                self.senha = password.get()
                self.salvar_dados(cpf.get(), cep.get(), email.get())
                cadastro.destroy()

        btn = CTkButton(master=cadastro, text="Criar", corner_radius=32,fg_color="#1bd1a4",hover_color="#118f70", command= autenticar)
        btn.place(relx = 0.5, rely = 0.8, relwidth = 0.25, anchor = "center")

        cadastro.mainloop()

    
    def login(self):
        ## Inicialização da Janela
        login = CTk()
        login.geometry("500x400")
        login.title("Login")
        set_appearance_mode("dark")

        ## Titulo e texto de login
        titulo = CTkLabel(master=login, text="Economizador de compras", font = ("Montserrat", 20))
        titulo.place(relx = 0.5, rely = 0.2, anchor = "center")
        textin = CTkLabel(master=login, text="Login :", font = ("Montserrat", 12))
        textin.place(relx = 0.4, rely = 0.33, relwidth = 0.25, relheight = 0.08, anchor = "center")
        
       
        ## Espaço de texto de usuário
        user = CTkEntry(master= login, placeholder_text="Usuário")
        user.place(relx = 0.5, rely = 0.4, relwidth = 0.25, relheight = 0.08, anchor="center")
        
        ## Espaço de texto para senha
        password = CTkEntry(master= login, placeholder_text="Senha", show = "*")
        password.place(relx = 0.5, rely = 0.49, relwidth = 0.25, relheight = 0.08, anchor="center")

        ## Erro caso usuario esteja errado
        erro_label = CTkLabel(master=login, text="", text_color="red")
        erro_label.place(relx=0.5, rely=0.68, anchor="center")

        ## Função que determina se a senha pode ser vista ou não a partir do botão
        def mostraSenha():
            if mostrar.get()== 1:
                password.configure(show = "")
            else:
                password.configure(show = "*")
        ## Função que determina se o tema é claro ou escuro de acordo com o switch
        def Tema():
            if changeTheme.get() == 1:
                set_appearance_mode("light")
            else:
                set_appearance_mode("dark")

        #Função de validação de usuario e senha
        def validar_userps():
            usuario = user.get()
            senha = password.get()
            self.carregar_dados(usuario)
            if usuario == self.nome and senha == self.senha:
                print("Login bem-sucedido!")
                login.destroy()
                self.App()
            else:
                btn.place(relx = 0.5, rely = 0.75, relwidth = 0.2, anchor = "center")
                erro_label.configure(text="Usuário ou senha incorretos!")

        def hover_on(event):
            cadastro.configure(font=("Montserrat", 12, "underline"))

        def hover_off(event):
            cadastro.configure(font=("Montserrat", 12))

        # Botão de mostrar senha
        mostrar = CTkCheckBox(master= login, text="Mostra senha", corner_radius= 4, fg_color="#1bd1a4", checkbox_height= 16, checkbox_width= 16, command= mostraSenha)
        mostrar.place(relx = 0.5, rely = 0.57, relwidth = 0.25, relheight = 0.08, anchor = "center")

        cadastro = CTkButton(master=login, text="Criar uma nova conta", font = ("Montserrat", 12), fg_color="transparent",text_color="#807D7D",hover="#6B6B6B", cursor="hand2", command = self.cadastro)
        cadastro.place(relx = 0.5, rely = 0.63, relwidth = 0.3, anchor = "center")
        cadastro.bind("<Enter>", hover_on)
        cadastro.bind("<Leave>", hover_off)


        ## Botão de login
        btn = CTkButton(master=login, text="Entrar", corner_radius=32,fg_color="#1bd1a4",hover_color="#118f70", command= validar_userps)
        btn.place(relx = 0.5, rely = 0.7, relwidth = 0.25, anchor = "center")

        ## Switch de tema
        changeTheme = CTkSwitch(master= login, command = Tema, text="Tema claro",progress_color= "#95ada7")
        changeTheme.place(relx = 0.2, rely = 0.9, anchor = "center")

        login.mainloop()  

       
inter = Interface()
inter.login()


