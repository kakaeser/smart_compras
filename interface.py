from customtkinter import *

class Interface:
    
    
    def login(self):
        ## Inicialização da Janela
        app = CTk()
        app.geometry("500x400")
        app.title("Login")
        set_appearance_mode("dark")

        ## Titulo e texto de login
        titulo = CTkLabel(master=app, text="Economizador de compras", font = ("Montserrat", 20))
        titulo.place(relx = 0.5, rely = 0.2, anchor = "center")
        textin = CTkLabel(master=app, text="Login :", font = ("Montserrat", 12))
        textin.place(relx = 0.4, rely = 0.33, relwidth = 0.25, relheight = 0.08, anchor = "center")
        
       
        ## Espaço de texto de usuário
        user = CTkEntry(master= app, placeholder_text="Usuário")
        user.place(relx = 0.5, rely = 0.4, relwidth = 0.25, relheight = 0.08, anchor="center")
        
        ## Espaço de texto para senha
        password = CTkEntry(master= app, placeholder_text="Senha", show = "*")
        password.place(relx = 0.5, rely = 0.49, relwidth = 0.25, relheight = 0.08, anchor="center")

        ## Erro caso usuario esteja errado
        erro_label = CTkLabel(master=app, text="", text_color="red")
        erro_label.place(relx=0.5, rely=0.65, anchor="center")

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
            if usuario == "Kaeser" and senha == "123456":
                print("Login bem-sucedido!")
                app.destroy()
            else:
                btn.place(relx = 0.5, rely = 0.75, relwidth = 0.2, anchor = "center")
                erro_label.configure(text="Usuário ou senha incorretos!")


        # Botão de mostrar senha
        mostrar = CTkCheckBox(master= app, text="Mostra senha", corner_radius= 4, fg_color="#1bd1a4", checkbox_height= 16, checkbox_width= 16, command= mostraSenha)
        mostrar.place(relx = 0.5, rely = 0.57, relwidth = 0.25, relheight = 0.08, anchor = "center")

        ## Botão de login
        btn = CTkButton(master=app, text="Entrar", corner_radius=32,fg_color="#1bd1a4",hover_color="#118f70", command= validar_userps)
        btn.place(relx = 0.5, rely = 0.65, relwidth = 0.2, anchor = "center")

        ## Switch de tema
        changeTheme = CTkSwitch(master= app, command = Tema, text="Tema claro",progress_color= "#95ada7")
        changeTheme.place(relx = 0.2, rely = 0.9, anchor = "center")

        app.mainloop()  

        

inter = Interface()
inter.login()