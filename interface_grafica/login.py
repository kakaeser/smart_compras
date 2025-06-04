from customtkinter import *
from banco_dados.manipulador_user import Manipulador_User
from classes.usuario import Usuario
from classes.usuariopremium import UsuarioPremium
from PIL import Image


class Login:

    def __init__(self, senha, nome, email) -> None:
        self.senha = senha
        self.nome = nome
        self.email = email

    def login(self) -> None:
            ## Inicialização da Janela
            app = CTk()
            app.geometry("500x400")
            app.title("Login")

            login = CTkFrame(master = app, fg_color=("#DDE7E7", "#2C2C2C"),width = 500, height = 400)
            login.place(relx = 0.5, rely = 0.5 ,anchor = "center")
            set_appearance_mode("dark")

            ## Titulo e texto de login
            logo = CTkImage(Image.open("imagens/logo.png"), size =(128,128))
            titulo = CTkLabel(master = login, image= logo, text="")
            titulo.place(relx = 0.5, rely = 0.18, anchor = "center")
            
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
            def mostraSenha() -> None:
                if mostrar.get()== 1:
                    password.configure(show = "")
                else:
                    password.configure(show = "*")
            ## Função que determina se o tema é claro ou escuro de acordo com o switch
            def Tema() -> None:
                if changeTheme.get() == 1:
                    set_appearance_mode("light")
                else:
                    set_appearance_mode("dark")

            #Função de validação de usuario e senha
            def validar_userps() -> None:
                nome_email = user.get()
                senha = password.get()
                usuario = Manipulador_User.carregar_dados(nome_email)

                if usuario and usuario["senha"] == senha:
                    self.nome = usuario["nome"]
                    self.email = usuario["email"]
                    self.senha = usuario["senha"]
                    
                    app.destroy()
                    self.App()
                else:
                    btn.place(relx = 0.5, rely = 0.75, relwidth = 0.2, anchor = "center")
                    erro_label.configure(text="Usuário ou senha incorretos!")

            def hover_on(event):
                cadastro.configure(font=("Montserrat", 12, "underline"))

            def hover_off(event):
                cadastro.configure(font=("Montserrat", 12))

            # Botão de mostrar senha
            mostrar = CTkCheckBox(master= login, text="Mostra senha", corner_radius= 4, fg_color="#17C5CE", checkbox_height= 16, checkbox_width= 16, command= mostraSenha)
            mostrar.place(relx = 0.5, rely = 0.57, relwidth = 0.25, relheight = 0.08, anchor = "center")

            cadastro = CTkButton(master=login, text="Criar uma nova conta", font = ("Montserrat", 12), fg_color="transparent",text_color="#807D7D",hover="#6B6B6B", cursor="hand2", command = self.cadastro)
            cadastro.place(relx = 0.5, rely = 0.63, relwidth = 0.3, anchor = "center")
            cadastro.bind("<Enter>", hover_on)
            cadastro.bind("<Leave>", hover_off)


            ## Botão de login
            btn = CTkButton(master=login, text="Entrar", corner_radius=32,fg_color="#17C5CE",hover_color="#1299A0", command= validar_userps)
            btn.place(relx = 0.5, rely = 0.7, relwidth = 0.25, anchor = "center")

            ## Switch de tema
            changeTheme = CTkSwitch(master= login, command = Tema, text="Tema claro",progress_color= "#1299A0")
            changeTheme.place(relx = 0.2, rely = 0.9, anchor = "center")

            app.mainloop()  