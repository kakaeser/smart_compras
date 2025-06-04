from customtkinter import *
from banco_dados.manipulador_user import Manipulador_User
from classes.usuario import Usuario
from classes.usuariopremium import UsuarioPremium
from PIL import Image

class App:
     
     def App(self) -> None:
        ## Inicialização do app
        app = CTk()
        app.geometry("1280x720")
        app.title("SmartCompras")

        ##Variaveis para a barralateral
        sidebar_width = 250
        initial_x_pos = -sidebar_width 
        menu_aberto = False
        config_aberta = False

        def Tema() -> None:
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
        fechar = CTkImage(Image.open("imagens/fechar.png"), size = (16,16))
        sair = CTkImage(Image.open("imagens/logout.png"), size = (16,16))
        premium = CTkImage(Image.open("imagens/premium.png"), size = (16,16))
        
        ## Instanciando o objeto Usuario
        dados = Manipulador_User.carregar_dados(self.nome)
        if len(dados["id"]) == 7:
            usuario = Usuario(dados["nome"] ,dados["email"], dados["senha"], dados["cpf"], dados["cep"] ,dados["id"])
        elif len(dados["id"]) == 8:
            usuario = UsuarioPremium(dados["nome"] ,dados["email"], dados["senha"], dados["cpf"], dados["cep"] ,dados["id"])
        
        def close() -> None:
          app.destroy()
        #Inicialização de uma janela que mostra os dados do usuario e pode edita-los
        def mostrar_usuario() -> None:
            app1 = CTkToplevel(app)
            app1.geometry("500x700")
            app1.title("Usuário")
            app1.transient(master=app)
            ##Apenas para PC
            #app1.wm_attributes("-toolwindow", True)

            open_user = CTkFrame(master = app1, width = 500, height = 700, fg_color=("#DDE7E7", "#2C2C2C"))
            open_user.place(relx= 0.5, rely = 0.5, anchor = "center")
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

            def checagem_alterar() -> None:
                
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

            def edicao(campo_widget) -> None: 
                campo_widget.configure(state="normal", text_color=("#000000", "#FFFFFF")) 
                checagem_alterar()

            def alterar_dados() -> None:
                if len(entry_vars["cpf"].get()) != 11:
                    erro_label.configure(text="CPF inválido")
                    return
                if len(entry_vars["cep"].get()) != 8 and len(entry_vars["cep"].get()) != 9:
                    erro_label.configure(text="CEP inválido")
                    return
                if entry_vars["nome"].get() != "" and entry_vars["nome"].get() !=valores_originais["nome"]:
                    verificador = Manipulador_User.conferir_dados(entry_vars["nome"].get())
                    if verificador == 1:
                        erro_label.configure(text="Nome de usuario já cadastrado")
                        return
                    else:
                        Manipulador_User.editar_dados(usuario.nome, "nome", entry_vars["nome"].get())
                        usuario.alterar_nome(entry_vars["nome"].get())
                if entry_vars["email"].get() != "" and entry_vars["email"].get() !=valores_originais["email"]:
                    verificador = Manipulador_User.conferir_dados(entry_vars["email"].get())
                    if verificador == 2:
                        erro_label.configure(text="Email já cadastrado")
                        return
                    else:
                        Manipulador_User.editar_dados(usuario.nome, "email", entry_vars["email"].get())
                        usuario.alterar_email(entry_vars["email"].get())
                if entry_vars["senha"].get() != "" and entry_vars["senha"].get() !=valores_originais["senha"]:
                    Manipulador_User.editar_dados(usuario.nome, "senha", entry_vars["senha"].get())
                    usuario.alterar_senha(entry_vars["senha"].get())
                if entry_vars["cpf"].get() != "" and entry_vars["cpf"].get() !=valores_originais["cpf"]:
                    verificador = Manipulador_User.conferir_dados(entry_vars["cpf"].get())
                    if verificador == 3:
                        erro_label.configure(text="CPF já cadastrado")
                        return
                    else:
                        Manipulador_User.editar_dados(usuario.nome, "cpf", entry_vars["cpf"].get())
                        usuario.alterar_cpf(entry_vars["cpf"].get())
                if entry_vars["cep"].get() != "" and entry_vars["cep"].get() !=valores_originais["cep"]:
                    Manipulador_User.editar_dados(usuario.nome, "cep", entry_vars["cep"].get())
                    usuario.alterar_cep(entry_vars["cep"].get())

                app1.destroy()

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
            
            
            cancelar = CTkButton(master = open_user, text= "Cancelar", command = app1.destroy, corner_radius = 0, fg_color="transparent",hover_color=("#B4B4B4", "#2C2C2C"), text_color=("#000000", "#FFFFFF"))
            cancelar.place(relx = 0.7, rely = 0.75, anchor = "center")

            alterar = CTkButton(master = open_user, text= "Alterar", corner_radius = 0, command = alterar_dados)
            alterar.place(relx = 0.3, rely = 0.75, anchor = "center")
            checagem_alterar()
        
          
        
        
        
        ##Inicialização da barra horizontal
        barrahori = CTkFrame(master = app, fg_color=("#DDE7E7", "#1B1B1B"), corner_radius=0)
        barrahori.place(relx = 0.5, rely = 0, relwidth = 1, anchor = "center")

         ## Inicialização barra lateral
        barralat = CTkFrame(master = app, fg_color=("#ADB4B4", "#2C2C2C"), corner_radius=0, width=sidebar_width)
        barralat.place(x = initial_x_pos, rely = 0.5, relheight = 1, anchor = "center")

        ## Inicialização Frame central
        central = CTkFrame(master = app, fg_color=("#EDFBFC", "#131313"), corner_radius=0)
        central.place(rely = 0.575, relx= 0.5, relwidth = 0.8, relheight = 0.8, anchor="center")

        ## Inicialização do Frame de configurações
        frameconfig = CTkFrame(master = app, fg_color=("#DDE7E7", "#1B1B1B"), corner_radius=0, height = 120)
        frameconfig.place(relx = 0.175)
        frameconfig.place(relx = initial_x_pos,rely = 0.86, anchor="center")

        

        def abrir_configs() -> None:
            nonlocal config_aberta
            if config_aberta:
                frameconfig.place(relx = initial_x_pos)
                config_aberta = False
            else:
                frameconfig.place(relx = 0.175)
                config_aberta = True

        def abrir_barralat() -> None:
            nonlocal menu_aberto
            if menu_aberto:
                end_x = -sidebar_width
            else:
                end_x = 0
            current_x = barralat.winfo_x()
            step = 20
            if menu_aberto:
                step = -step
            def animacao() -> None:
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
        def logout() -> None:
            close()
            self.login()
            
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

        btnpremium = CTkButton(master = frameconfig, text= "Assinar Premium", command = close, corner_radius = 0, fg_color = "transparent", hover_color=("#C7C7C7", "#474747"), image = premium,text_color=("#808080", "#A0A0A0"))
        btnpremium.place(relx = 0.5, rely = 0.2, relwidth = 1, anchor = "center")

        btnfechar = CTkButton(master = frameconfig, text= "Fechar", command = close, corner_radius = 0, fg_color = "transparent", hover_color=("#C7C7C7", "#474747"), image = fechar,text_color=("#808080", "#A0A0A0"))
        btnfechar.place(relx = 0.5, rely = 0.4, relwidth = 1, anchor = "center")

        btnlogout = CTkButton(master = frameconfig, text= "Logout", command = logout, corner_radius = 0, fg_color = "transparent", hover_color=("#C7C7C7", "#474747"), image = sair,text_color=("#808080", "#A0A0A0"))
        btnlogout.place(relx = 0.5, rely = 0.6, relwidth = 1, anchor = "center")

        changeTheme = CTkSwitch(master= frameconfig, command = Tema, text="Tema claro",progress_color= "#1299A0")
        changeTheme.place(relx = 0.4, rely = 0.85, anchor = "center")

        temaimage = CTkLabel(master= frameconfig, text="", image = tema)
        temaimage.place(relx = 0.75, rely = 0.85, anchor = "center")

        app.mainloop()