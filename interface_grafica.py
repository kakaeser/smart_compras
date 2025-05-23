from customtkinter import *
from banco_dados.manipulador_user import Manipulador_User
from classes.usuario import Usuario
from classes.usuariopremium import UsuarioPremium
from PIL import Image

class InterfaceGrafica:
    
    def __init__(self):
        self.senha = ""
        self.nome = ""
        self.email = ""
        
        

    def App(self):
        ## Inicialização do app
        app = CTk()
        app.geometry("1280x720")
        app.title("SmartCompras")
        
        ## Instanciando o objeto Usuario
        dados = Manipulador_User.carregar_dados(self.nome)
        if len(dados["id"]) == 7:
            usuario = Usuario(dados["nome"] ,dados["email"], dados["senha"], dados["cpf"], dados["cep"] ,dados["id"])
        elif len(dados["id"]) == 8:
            usuario = UsuarioPremium(dados["nome"] ,dados["email"], dados["senha"], dados["cpf"], dados["cep"] ,dados["id"])
        
        def close():
          app.destroy()
          
          
        def mostrar_usuario():
          open_user = CTkToplevel(app)
          open_user.geometry("500x700")
          open_user.title("Usuário")
          
          fechar1 = CTkButton(master = open_user, text= "Fechar", command = open_user.destroy, corner_radius = 0)
          fechar1.place(relx = 0.5, rely = 0.8, anchor = "center")
          
        
        fechar = CTkButton(master = app, text= "Fechar", command = close, corner_radius = 0)
        fechar.place(relx = 0.5, rely = 0.5, anchor = "center")
        
        logo = CTkImage(Image.open("imagens/logo.png"), size =(120,120))
        if get_appearance_mode() == "Dark":
          user1 = CTkImage(Image.open("imagens/usuario2.png"), size = (30,30))
        else:
          user1 = CTkImage(Image.open("imagens/usuario1.png"), size = (30,30))
        

        ## Inicialização barra lateral
        barralat = CTkFrame(master = app, fg_color="#17C5CE", corner_radius=0)
        barralat.place(relx = 0, rely = 0.5, relheight = 1, anchor = "center")
        
        
        user = CTkButton(master = barralat, text = "", corner_radius = 48, fg_color = "transparent", hover_color="#1299A0", image= user1, command= mostrar_usuario)
        user.place(relx = 0.75, rely = 0.8, relwidth = 0.3,anchor ="center")
        
        app.mainloop()
  
    def cadastro(self):
        cadastro = CTk()
        cadastro.geometry("500x700")
        cadastro.title("Cadastrar")
        select : bool
        

        erro_label = CTkLabel(master=cadastro, text="", text_color="red")
        erro_label.place(relx=0.5, rely=0.85, anchor="center")

        textin = CTkLabel(master=cadastro, text="Insira os dados :", font = ("Montserrat", 12))

        user = CTkEntry(master = cadastro, placeholder_text= "Nome")

        email = CTkEntry(master= cadastro, placeholder_text="Email")

        cpf = CTkEntry(master= cadastro, placeholder_text="CPF")

        cep = CTkEntry(master= cadastro, placeholder_text="CEP")
    
        password = CTkEntry(master= cadastro, placeholder_text="Senha", show = "*")
        
        cpassword = CTkEntry(master= cadastro, placeholder_text="Confirmar Senha", show = "*")
        

        


        def termos():
            termo = CTkTextbox(master= cadastro)
            try:
                with open("banco_dados/termos.txt", "r", encoding="utf-8") as arquivo:
                    conteudo = arquivo.read()
                    termo.insert("0.0", conteudo)
            except FileNotFoundError:
                termo.insert("0.0", "Arquivo de termos não encontrado.")
            termo.configure(state="disabled")
            termo.place(relx = 0.5, rely = 0.4, relwidth = 0.6 , relheight= 0.6,anchor ="center")
            def criacao():
                termo.destroy()
                mostrar.destroy()
                confirm.destroy()
                
                textin.place(relx = 0.4, rely = 0.33, relwidth = 0.25, relheight = 0.08, anchor = "center")
                user.place(relx = 0.5, rely = 0.2, relwidth = 0.5, relheight = 0.08, anchor="center")
                email.place(relx = 0.5, rely = 0.3, relwidth = 0.5, relheight = 0.08, anchor="center")
                cpf.place(relx = 0.5, rely = 0.4, relwidth = 0.5, relheight = 0.08, anchor="center")
                cep.place(relx = 0.5, rely = 0.5, relwidth = 0.5, relheight = 0.08, anchor="center")
                password.place(relx = 0.5, rely = 0.6, relwidth = 0.5, relheight = 0.08, anchor="center")
                cpassword.place(relx = 0.5, rely = 0.7, relwidth = 0.5, relheight = 0.08, anchor="center")
                btn.place(relx = 0.5, rely = 0.8, relwidth = 0.25, anchor = "center")

            confirm = CTkButton(master=cadastro, text="Continuar", corner_radius=32,fg_color="transparent")
            confirm.place(relx = 0.5, rely = 0.8, relwidth = 0.25, anchor = "center")

            def aceitar():
                if mostrar.get() == 1:
                    confirm.configure(fg_color="#17C5CE",hover_color="#1299A0", state ="normal",command= criacao)
                else:
                    confirm.configure(fg_color="transparent", state = "disabled" , command=lambda: None)

            mostrar = CTkCheckBox(master= cadastro, text="Li e concordo com os termos", corner_radius= 4, fg_color="#17C5CE", checkbox_height= 16, checkbox_width= 16, command= aceitar )
            mostrar.place(relx = 0.5, rely = 0.75, relwidth = 0.4, relheight = 0.03, anchor = "center")

            
        def premium_select():
            nonlocal select 
            select = True
            normal.destroy()
            premium.destroy()
            termos()
        
        def normal_select():
            nonlocal select 
            select = False
            normal.destroy()
            premium.destroy()
            termos()

        def autenticar():
            if user.get() == "" or email.get() == "" or cpf.get() == "" or cep.get() == "" or password.get() == "" or cpassword.get() == "":
                erro_label.configure(text="Você não preencheu todos os campos!!")
                return
            

            if cpassword.get() != password.get():
                erro_label.configure(text="Sua senha não é a mesma que você quis confirmar")
                return
                
            sucesso = Manipulador_User.salvar_dados(user.get(),email.get(),password.get(), cpf.get(), cep.get(), select)
            if not sucesso:
                erro_label.configure(text="Usuário ou email já existem")
                return
            
            self.nome = user.get()
            self.email = email.get()
            self.senha = password.get()
            cadastro.destroy()

        

        normal = CTkButton(master = cadastro, text = "Plano padrão \n\n R$00,00\n\n ● Calculo de qual\nsupermercado é\nmais economico\n\n ● Pequenas ofertas", fg_color= "transparent", border_color= "#17C5CE", border_width=2, hover_color=("#B4B4B4", "#2C2C2C"), text_color=("#000000", "#FFFFFF"),font=("Arial", 16, "bold"), command = normal_select)
        normal.place(relx = 0.28, rely = 0.5, relwidth = 0.4 , relheight= 0.6,anchor ="center")

        premium = CTkButton(master = cadastro, text = "Plano Premium \n\n R$12,90\n\n ● Ofertas maiores \n\n ● Calcula o gasto de \ncombustivel\n\n ● Visualização de\nchegada de produtos", fg_color= "transparent", border_color= "#17C5CE", border_width=2, hover_color=("#B4B4B4", "#2C2C2C"), text_color=("#000000", "#FFFFFF"),font=("Arial", 16, "bold"), command= premium_select)
        premium.place(relx = 0.72, rely = 0.5, relwidth = 0.4 , relheight= 0.6,anchor ="center")

        btn = CTkButton(master=cadastro, text="Criar", corner_radius=32,fg_color="#17C5CE",hover_color="#1299A0", command= autenticar)
        

        cadastro.mainloop()

    
    def login(self):
        ## Inicialização da Janela
        login = CTk()
        login.geometry("500x400")
        login.title("Login")
        set_appearance_mode("dark")

        ## Titulo e texto de login
        logo = CTkImage(Image.open("imagens/logo.png"), size =(120,120))
        titulo = CTkLabel(master = login, image= logo, text="")
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
            nome_email = user.get()
            senha = password.get()
            usuario = Manipulador_User.carregar_dados(nome_email)

            if usuario and usuario["senha"] == senha:
                self.nome = usuario["nome"]
                self.email = usuario["email"]
                self.senha = usuario["senha"]
                
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

        login.mainloop()  

       



