from customtkinter import *
from banco_dados.manipulador_user import Manipulador_User
from classes.usuario import Usuario
from classes.usuariopremium import UsuarioPremium
from PIL import Image
import platform
so = platform.system()

class App:
  ##Mecanica do scroll do mouse
    
    def mec_scroll(self,scroll,card) -> None:

        def scroll_windows(event) -> None:
            scroll._parent_canvas.yview_scroll(-int(event.delta/4), "units")
            
        def scroll_linux(event)-> None:
            if event.num == 4:
                scroll._parent_canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                scroll._parent_canvas.yview_scroll(1, "units")

      
        if so == "Windows":
            scroll.bind("<Enter>", lambda e: scroll.bind_all("<MouseWheel>", scroll_windows))
            scroll.bind("<Leave>", lambda e: scroll.unbind_all("<MouseWheel>"))
        else:
            scroll.bind("<Enter>", lambda e: (
                scroll.bind_all("<Button-4>", scroll_linux),
                scroll.bind_all("<Button-5>", scroll_linux)
            ))
            scroll.bind("<Leave>", lambda e: (
                scroll.unbind_all("<Button-4>"),
                scroll.unbind_all("<Button-5>")
            ))
         ## Coisa que faz o scroll funcionar nos frames criados
        if so == "Windows":
                card.bind("<MouseWheel>",scroll_windows)
        else:
            card.bind("<Button-4>", scroll_linux) 
            card.bind("<Button-5>", scroll_linux)


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
        config = CTkImage(Image.open("imagens/config.png"), size = (32,32))
        menu = CTkImage(Image.open("imagens/menu.png"), size = (32,32))
        tema = CTkImage(Image.open("imagens/tema.png"), size = (16,16))
        fechar = CTkImage(Image.open("imagens/fechar.png"), size = (16,16))
        sair = CTkImage(Image.open("imagens/logout.png"), size = (16,16))
        premium = CTkImage(Image.open("imagens/premium.png"), size = (16,16))
        busca = CTkImage(Image.open("imagens/busca.png"), size = (16,16))
        busca_fail = CTkImage(Image.open("imagens/busca_fail.png"), size = (48,48))
        nova_lista = CTkImage(Image.open("imagens/nova_lista.png"), size = (16,16))
        
        ## Instanciando o objeto Usuario
        dados = Manipulador_User.carregar_dados(self.nome)
        if len(dados["id"]) == 7:
            usuario = Usuario(dados["nome"] ,dados["email"], dados["senha"], dados["cpf"], dados["cep"] ,dados["id"])
        elif len(dados["id"]) == 8:
            usuario = UsuarioPremium(dados["nome"] ,dados["email"], dados["senha"], dados["cpf"], dados["cep"] ,dados["id"])
        
        def close() -> None:
            self.fechar_cards()
            app.destroy()
    
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
        menuh = CTkButton(master = barrahori, text = "", corner_radius = 48, fg_color = ("#DDE7E7", "#1B1B1B"), hover_color=("#C7C7C7", "#474747"), image= menu, command= abrir_barralat)
        menuh.place(relx = 0.049, rely = 0.75, relwidth = 0.05,anchor ="center")

        ##Menu barra lateral
        menul = CTkButton(master = barralat, text = "", corner_radius = 48, fg_color = "transparent", hover_color=("#C7C7C7", "#474747"), image= menu, command= abrir_barralat)
        menul.place(relx = 0.75, rely = 0.07, relwidth = 0.3,anchor ="center")
        
        
        ##Widgets barra horizontal
        titulo = CTkLabel(master = barrahori, image= logo, text="")
        titulo.place(relx = 0.95, rely = 0.75, anchor = "center")
        
        users = CTkButton(master = barralat, text = "", corner_radius = 48, fg_color = "transparent", hover_color=("#C7C7C7", "#474747"), image= user, command=lambda: self.mostrar_usuario(app ,usuario))
        users.place(relx = 0.75, rely = 0.85, relwidth = 0.3,anchor ="center")

        configs = CTkButton(master = barralat, text = "", corner_radius = 48, fg_color = "transparent", hover_color=("#C7C7C7", "#474747"), image= config, command=abrir_configs)
        configs.place(relx = 0.75, rely = 0.95, relwidth = 0.3,anchor ="center")

        ##Widgets do frameconfig
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
        
        
        ##WIdgets do frame central
        
        ##Inicialização do scroll
        scroll = CTkScrollableFrame(master=central, fg_color="transparent", corner_radius=0)
        scroll.place(relx=0.5, rely=0.52,relwidth=1, relheight = 0.9, anchor="center")

        erro_imagem = CTkLabel(master = central, text="", image=busca_fail)
        erro_imagem.place(relx= 0.5, rely=0.5, anchor= "center")
        erro_label = CTkLabel(master = central, text = "Ainda não temos uma lista ou busca, crie uma lista para aparecer os supermercados!", text_color=("#979797", "#3F3F3F"),font=("Montserrat", 16, "bold"))
        erro_label.place(relx= 0.5, rely=0.65, anchor="center")

        def cards():
            self.fechar_cards()
            erro_label.configure(text="")
            erro_imagem.configure(image="")
            self.abrir_cards(scroll)
            
            
        
        barra_pesquisa = CTkEntry(master= central, placeholder_text="Pesquise: Ex: Frango, Coca-Cola, Sabão", text_color=("#808080", "#A0A0A0"), corner_radius=2, fg_color = "transparent")
        barra_pesquisa.place(relx =0.5, rely=0.028,relwidth = 0.9,relheight = 0.055,anchor="center")
        
        lista = CTkButton(master= central, image= nova_lista, text="",corner_radius =0, fg_color=("#ADB4B4", "#2C2C2C"),hover_color=("#C7C7C7", "#474747"))
        lista.place(relx= 0.024, rely=0.028, relwidth = 0.05,relheight = 0.055, anchor="center")
        
        buscar = CTkButton(master= central, image=busca, text="",corner_radius =0, fg_color=("#ADB4B4", "#2C2C2C"),hover_color=("#C7C7C7", "#474747"), command = cards)
        buscar.place(relx= 0.975, rely=0.028, relwidth = 0.05,relheight = 0.055, anchor="center")
        
        
        
        
        app.mainloop()