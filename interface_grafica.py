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

        ##Variaveis para a barralateral
        sidebar_width = 250
        initial_x_pos = -sidebar_width 
        menu_aberto = False
        config_aberta = False

        def Tema():
            if changeTheme.get() == 1:
                set_appearance_mode("light")
            else:
                set_appearance_mode("dark")

        #iniciação das imagens
        logo = CTkImage(Image.open("imagens/logo.png"), size =(128,128))
        user = CTkImage(Image.open("imagens/usuario.png"), size = (32,32))
        edit = CTkImage(Image.open("imagens/editar.png"), size = (16,16))
        config = CTkImage(Image.open("imagens/config.png"), size = (32,32))
        menu = CTkImage(Image.open("imagens/menu.png"), size = (32,32))
        tema = CTkImage(Image.open("imagens/tema.png"), size = (16,16))
        
        ## Instanciando o objeto Usuario
        dados = Manipulador_User.carregar_dados(self.nome)
        if len(dados["id"]) == 7:
            usuario = Usuario(dados["nome"] ,dados["email"], dados["senha"], dados["cpf"], dados["cep"] ,dados["id"])
        elif len(dados["id"]) == 8:
            usuario = UsuarioPremium(dados["nome"] ,dados["email"], dados["senha"], dados["cpf"], dados["cep"] ,dados["id"])
        
        def close():
          app.destroy()
        #Inicialização de uma janela que mostra os dados do usuario e pode edita-los
        def mostrar_usuario():
            open_user = CTkToplevel(app)
            open_user.geometry("500x700")
            open_user.title("Usuário")
            entry_vars = {} 
            entries = {} 
            
            erro_label = CTkLabel(master = open_user, text="", text_color="red")
            erro_label.place(relx = 0.5, rely = 0.65, anchor="center")
            
            valores_originais = {
                "nome": usuario.nome,
                "email": usuario.email,
                "senha": usuario.senha,
                "cpf": usuario.cpf,
                "cep": usuario.cep
            }

            def checagem_alterar():
                
                mudanca = False
                for key in valores_originais:
                    current_value = entry_vars[key].get() 
                    if current_value != "" and current_value != valores_originais[key]:
                        mudanca = True
                        break 

                if mudanca:
                    alterar.configure(fg_color="#17C5CE", hover_color="#1299A0", state="normal")
                else:
                    alterar.configure(fg_color="transparent", state="disabled")

            def edicao(campo_widget): 
                campo_widget.configure(state="normal", text_color=("#000000", "#FFFFFF")) 
                checagem_alterar()

            def alterar_dados():
                if len(entry_vars["cpf"].get()) != 11:
                    erro_label.configure(text="CPF inválido")
                    return
                if len(entry_vars["cep"].get()) != 8:
                    erro_label.configure(text="CEP inválido")
                    return
                if entry_vars["nome"].get() != "" and entry_vars["nome"].get() !=valores_originais["nome"]:
                    Manipulador_User.editar_dados(usuario.nome, "nome", entry_vars["nome"].get())
                    usuario.alterar_nome(entry_vars["nome"].get())
                if entry_vars["email"].get() != "" and entry_vars["email"].get() !=valores_originais["email"]:
                    Manipulador_User.editar_dados(usuario.nome, "email", entry_vars["email"].get())
                    usuario.alterar_email(entry_vars["email"].get())
                if entry_vars["senha"].get() != "" and entry_vars["senha"].get() !=valores_originais["senha"]:
                    Manipulador_User.editar_dados(usuario.nome, "senha", entry_vars["senha"].get())
                    usuario.alterar_senha(entry_vars["senha"].get())
                if entry_vars["cpf"].get() != "" and entry_vars["cpf"].get() !=valores_originais["cpf"]:
                    Manipulador_User.editar_dados(usuario.nome, "cpf", entry_vars["cpf"].get())
                    usuario.alterar_cpf(entry_vars["cpf"].get())
                if entry_vars["cep"].get() != "" and entry_vars["cep"].get() !=valores_originais["cep"]:
                    Manipulador_User.editar_dados(usuario.nome, "cep", entry_vars["cep"].get())
                    usuario.alterar_cep(entry_vars["cep"].get())

                open_user.destroy()

            campos_config = {
                "nome": (usuario.nome, 0.2),
                "email": (usuario.email, 0.3),
                "senha": (usuario.senha, 0.4),
                "cpf": (usuario.cpf, 0.5),
                "cep": (usuario.cep, 0.6)
            }

            for key, (placeholder, rely_pos) in campos_config.items():
               
                entry_var = StringVar(master=open_user, value=placeholder)
                entry_vars[key] = entry_var

                entry = CTkEntry(master=open_user, textvariable=entry_var, text_color=("#808080", "#A0A0A0"), corner_radius=2)
                entry.configure(state="disabled") 
                entry.place(relx=0.46, rely=rely_pos, relwidth=0.38, relheight=0.046, anchor="center")
                entries[key] = entry 
                entry_var.trace_add("write", lambda name, index, mode: checagem_alterar())

                btn_editar = CTkButton(master=open_user, command=lambda e=entry: edicao(e), text="", corner_radius=2, fg_color=("#B4B4B4", "#2C2C2C"),hover_color=("#C7C7C7", "#474747"), image = edit)
                btn_editar.place(relx=0.68, rely=rely_pos, relwidth=0.064, relheight=0.046, anchor="center")

            titulo = CTkLabel(master= open_user, text= f"Usuario id: {usuario.id_user}" ,text_color=("#808080", "#A0A0A0"),font = ("Montserrat", 16, "bold"))
            titulo.place(relx=0.43, rely=0.1, anchor="center")

            label1 = CTkLabel(master= open_user, text= "Nome:" ,text_color=("#808080", "#A0A0A0"),font = ("Montserrat", 12))
            label1.place(relx=0.31, rely=0.15, anchor="center")

            label2 = CTkLabel(master= open_user, text= "Email:" ,text_color=("#808080", "#A0A0A0"),font = ("Montserrat", 12))
            label2.place(relx=0.31, rely=0.25, anchor="center")

            label3 = CTkLabel(master= open_user, text= "Senha:" ,text_color=("#808080", "#A0A0A0"),font = ("Montserrat", 12))
            label3.place(relx=0.31, rely=0.35, anchor="center")

            label4 = CTkLabel(master= open_user, text= "CPF:" ,text_color=("#808080", "#A0A0A0"),font = ("Montserrat", 12))
            label4.place(relx=0.3, rely=0.45, anchor="center")

            label5 = CTkLabel(master= open_user, text= "CEP:" ,text_color=("#808080", "#A0A0A0"),font = ("Montserrat", 12))
            label5.place(relx=0.3, rely=0.55, anchor="center")
            
            
            cancelar = CTkButton(master = open_user, text= "Cancelar", command = open_user.destroy, corner_radius = 0, fg_color="transparent",hover_color=("#B4B4B4", "#2C2C2C"), text_color=("#000000", "#FFFFFF"))
            cancelar.place(relx = 0.7, rely = 0.75, anchor = "center")

            alterar = CTkButton(master = open_user, text= "Alterar", corner_radius = 0, command = alterar_dados)
            alterar.place(relx = 0.3, rely = 0.75, anchor = "center")
            checagem_alterar()
        
          
        
        
        
        ##Inicialização da barra horizontal
        barrahori = CTkFrame(master = app, fg_color=("#A5A5A5", "#1B1B1B"), corner_radius=0)
        barrahori.place(relx = 0.5, rely = 0, relwidth = 1, anchor = "center")

         ## Inicialização barra lateral
        barralat = CTkFrame(master = app, fg_color=("#B4B4B4", "#2C2C2C"), corner_radius=0, width=sidebar_width)
        barralat.place(x = initial_x_pos, rely = 0.5, relheight = 1, anchor = "center")

        ## Inicialização Frame central
        central = CTkFrame(master = app, fg_color=("#808080", "#131313"), corner_radius=0)
        central.place(rely = 0.575, relx= 0.5, relwidth = 0.8, relheight = 0.8, anchor="center")

        ## Inicialização do Frame de configurações
        frameconfig = CTkFrame(master = app, fg_color=("#A5A5A5", "#1B1B1B"), corner_radius=0)
        frameconfig.place(relx = 0.175)
        frameconfig.place(relx = initial_x_pos,rely = 0.86, anchor="center")

        

        def abrir_configs():
            nonlocal config_aberta
            if config_aberta:
                frameconfig.place(relx = initial_x_pos)
                config_aberta = False
            else:
                frameconfig.place(relx = 0.175)
                config_aberta = True

        def abrir_barralat():
            nonlocal menu_aberto
            if menu_aberto:
                end_x = -sidebar_width
            else:
                end_x = 0
            current_x = barralat.winfo_x()
            step = 20
            if menu_aberto:
                step = -step
            def animacao():
                nonlocal menu_aberto, current_x, config_aberta
                if menu_aberto and current_x > end_x: # Fechando
                    current_x += step
                    if current_x < end_x: 
                        current_x = end_x
                        barralat.place(x=current_x)
                        central.place(relx = 0.5)
                        frameconfig.place(relx = initial_x_pos)
                        config_aberta = False
                    app.after(10, animacao) 
                elif not menu_aberto and current_x < end_x: # Abrindo
                    current_x += step
                    if current_x > end_x: 
                        current_x = end_x
                        barralat.place(x=current_x)
                        central.place(relx = 0.55)
                    app.after(10, animacao) 
                else:
                    menu_aberto = not menu_aberto
            animacao()
        
        ##Menu barra horizontal
        menuh = CTkButton(master = barrahori, text = "", corner_radius = 48, fg_color = ("#A5A5A5", "#1B1B1B"), hover_color=("#C7C7C7", "#474747"), image= menu, command= abrir_barralat)
        menuh.place(relx = 0.049, rely = 0.75, relwidth = 0.05,anchor ="center")

        ##Menu barra lateral
        menul = CTkButton(master = barralat, text = "", corner_radius = 48, fg_color = "transparent", hover_color=("#C7C7C7", "#474747"), image= menu, command= abrir_barralat)
        menul.place(relx = 0.75, rely = 0.07, relwidth = 0.3,anchor ="center")

        titulo = CTkLabel(master = barrahori, image= logo, text="")
        titulo.place(relx = 0.95, rely = 0.75, anchor = "center")
        
        users = CTkButton(master = barralat, text = "", corner_radius = 48, fg_color = "transparent", hover_color=("#C7C7C7", "#474747"), image= user, command= mostrar_usuario)
        users.place(relx = 0.75, rely = 0.85, relwidth = 0.3,anchor ="center")

        configs = CTkButton(master = barralat, text = "", corner_radius = 48, fg_color = "transparent", hover_color=("#C7C7C7", "#474747"), image= config, command=abrir_configs)
        configs.place(relx = 0.75, rely = 0.95, relwidth = 0.3,anchor ="center")
        
        fechar = CTkButton(master = central, text= "Fechar", command = close, corner_radius = 0)
        fechar.place(relx = 0.5, rely = 0.5, anchor = "center")

        changeTheme = CTkSwitch(master= frameconfig, command = Tema, text="Tema claro",progress_color= "#1299A0")
        changeTheme.place(relx = 0.4, rely = 0.9, anchor = "center")

        temaimage = CTkLabel(master= frameconfig, text="", image = tema)
        temaimage.place(relx = 0.75, rely = 0.9, anchor = "center")

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
        
        #Função que le e mostra os termos de compromisso
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
            
            #Função que faz aparecer a tela de criação de usuario apos o usuario aceitar o termo
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
            
            #Função que ve se o usuario aceitou ou não os termos de compromisso
            def aceitar():
                if mostrar.get() == 1:
                    confirm.configure(fg_color="#17C5CE",hover_color="#1299A0", state ="normal",command= criacao)
                else:
                    confirm.configure(fg_color="transparent", state = "disabled" , command=lambda: None)

            mostrar = CTkCheckBox(master= cadastro, text="Li e concordo com os termos", corner_radius= 4, fg_color="#17C5CE", checkbox_height= 16, checkbox_width= 16, command= aceitar )
            mostrar.place(relx = 0.5, rely = 0.75, relwidth = 0.4, relheight = 0.03, anchor = "center")

        #Seleção de plano premium    
        def premium_select():
            nonlocal select 
            select = True
            normal.destroy()
            premium.destroy()
            termos()
        #Seleção de plano gratuito
        def normal_select():
            nonlocal select 
            select = False
            normal.destroy()
            premium.destroy()
            termos()
        
        #Autentificador de dados coletados, previne email e usuarios repetidos
        def autenticar():
            if user.get() == "" or email.get() == "" or cpf.get() == "" or cep.get() == "" or password.get() == "" or cpassword.get() == "":
                erro_label.configure(text="Você não preencheu todos os campos!!")
                return
            if len(cpf.get()) != 11:
                erro_label.configure(text="CPF inválido")
                return
              
            if len(cep.get()) != 8:
                erro_label.configure(text="CEP inválido")
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

        
        #Selecionador de Planos
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

       



