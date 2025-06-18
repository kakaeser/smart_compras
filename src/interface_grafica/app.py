from customtkinter import *
from manipulador_classes.manipulador_user import Manipulador_User
from usuario_classes.usuario import Usuario
from usuario_classes.usuariopremium import UsuarioPremium
from typing import Union
import platform
so = platform.system()

class App:
    def __init__(self) -> None:
        self.menu_aberto = False
        self.config_aberta = False
        self.current_x = 0
        self.sidebar_width = 250
        self.initial_x_pos = -self.sidebar_width 
  ##Mecanica do scroll do mouse  
    def mec_scroll(self,scroll: CTkScrollableFrame, card:CTkFrame, multiplicador:int) -> None:

        def scroll_windows(event) -> None:
            scroll._parent_canvas.yview_scroll(-int(event.delta/(4*multiplicador)), "units")
            
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

        if so == "Windows":
            card.adicional.bind("<MouseWheel>",scroll_windows)
        else:
            card.adicional.bind("<Button-4>", scroll_linux) 
            card.adicional.bind("<Button-5>", scroll_linux)

    def Tema(self, checkbox : CTkCheckBox) -> None:
        if checkbox.get() == 1:
            set_appearance_mode("light")
        else:
            set_appearance_mode("dark")

    def abrir_configs(self, frameconfig : CTkFrame) -> None:
        if self.config_aberta:
            frameconfig.place(relx = self.initial_x_pos)
            self.config_aberta = False
        else:
            frameconfig.place(relx = 0.175)
            self.config_aberta = True

    def close(self, app: CTk) -> None:
        self.fechar_cards()
        app.destroy()

    def logout(self, app:CTk) -> None:
        self.close(app)
        self.login()

    def animacao(self, end_x: int, step: int, barralat: CTkFrame, central: CTkFrame, frameconfig: CTkFrame, app: CTk) -> None:
        if self.menu_aberto and self.current_x > end_x: # Fechando
            self.current_x += step
            if self.current_x < end_x: 
                self.current_x = end_x
                barralat.place(x=self.current_x)
                central.place(relx = 0.5)
                frameconfig.place(relx = self.initial_x_pos)
                self.config_aberta = False
            app.after(10, self.animacao(end_x, step, barralat, central, frameconfig, app)) 
        elif not self.menu_aberto and self.current_x < end_x: # Abrindo
            self.current_x += step
            if self.current_x > end_x: 
                self.current_x = end_x
                barralat.place(x=self.current_x)
                central.place(relx = 0.55)
            app.after(10, self.animacao(end_x, step, barralat, central, frameconfig, app)) 
        else:
            self.menu_aberto = not self.menu_aberto

    def abrir_barralat(self,barralat: CTkFrame, central: CTkFrame, frameconfig: CTkFrame, app: CTk) -> None:
        
        if self.menu_aberto:
            end_x = -self.sidebar_width
        else:
            end_x = 0
        self.current_x = barralat.winfo_x()
        step = 20
        if self.menu_aberto:
            step = -step
        self.animacao(end_x, step, barralat, central, frameconfig, app)

    def cards(self, barra_pesquisa: CTkEntry, erro_label: CTkLabel, erro_imagem: CTkLabel, scroll: CTkScrollableFrame, usuario:Union[Usuario, UsuarioPremium]) -> None:
        if self.lista_compras is None or not self.lista_compras:
            if barra_pesquisa.get() == "":
                erro_label.configure(text="Ainda não temos uma lista ou busca, crie uma lista para aparecer os supermercados!")
                erro_imagem.place(relx= 0.5, rely=0.5, anchor= "center")
        elif sum(self.lista_compras.values()) == 0 and barra_pesquisa.get() == "":
            erro_label.configure(text="Sua lista está vazia, e sua pesquisa também")
            erro_imagem.place(relx= 0.5, rely=0.5, anchor= "center")
        else:
            erro_label.configure(text="")
            erro_imagem.place_forget()
            self.abrir_cards(scroll, usuario)

    def App(self) -> None:
        ## Inicialização do app
        app = CTk()
        app.geometry("1280x720")
        app.title("SmartCompras")
        
        self.logo = self.carregar_icones("logo.png", (128,128))
        self.user = self.carregar_icones("usuario.png", (32,32))
        self.config = self.carregar_icones("config.png", (32,32))
        self.menu = self.carregar_icones("menu.png", (32,32))
        self.tema = self.carregar_icones("tema.png",(16,16))
        self.fechar = self.carregar_icones("fechar.png", (16,16))
        self.sair = self.carregar_icones("logout.png", (16,16))
        self.premium = self.carregar_icones("premium.png", (16,16))
        self.busca = self.carregar_icones("busca.png", (16,16))
        self.busca_fail = self.carregar_icones("busca_fail.png", (48,48))
        self.nova_lista = self.carregar_icones("nova_lista.png", (16,16))
        self.selected1 = self.carregar_icones("selected.png", (32,32))
        self.not_selected1 = self.carregar_icones("not_selected1.png",(32,32))

    
        ## Instanciando o objeto Usuario
        dados = Manipulador_User.carregar_dados(self.nome)
        if len(dados["id"]) == 7:
            usuario = Usuario(dados["nome"] ,dados["email"], dados["senha"], dados["cpf"], dados["cep"] ,dados["id"])
        elif len(dados["id"]) == 8:
            usuario = UsuarioPremium(dados["nome"] ,dados["email"], dados["senha"], dados["cpf"], dados["cep"] ,dados["id"])
        
    
        ##Inicialização da barra horizontal
        barrahori = CTkFrame(master = app, fg_color=("#DDE7E7", "#1B1B1B"), corner_radius=0)
        barrahori.place(relx = 0.5, rely = 0, relwidth = 1, anchor = "center")

        ## Inicialização barra lateral
        barralat = CTkFrame(master = app, fg_color=("#ADB4B4", "#2C2C2C"), corner_radius=0, width=self.sidebar_width)
        barralat.place(x = self.initial_x_pos, rely = 0.5, relheight = 1, anchor = "center")
        
        ## Inicialização Frame central
        central = CTkFrame(master = app, fg_color=("#EDFBFC", "#131313"), corner_radius=0)
        central.place(rely = 0.575, relx= 0.5, relwidth = 0.8, relheight = 0.8, anchor="center")

        ## Inicialização do Frame de configurações
        frameconfig = CTkFrame(master = app, fg_color=("#DDE7E7", "#1B1B1B"), corner_radius=0, height = 120)
        frameconfig.place(relx = 0.175)
        frameconfig.place(relx = self.initial_x_pos,rely = 0.86, anchor="center")
    
        ##Menu barra horizontal
        menuh = CTkButton(master = barrahori, text = "", corner_radius = 48, fg_color = ("#DDE7E7", "#1B1B1B"), hover_color=("#C7C7C7", "#474747"), image= self.menu, command=lambda: self.abrir_barralat(barralat, central,frameconfig, app))
        menuh.place(relx = 0.049, rely = 0.75, relwidth = 0.05,anchor ="center")

        ##Menu barra lateral
        menul = CTkButton(master = barralat, text = "", corner_radius = 48, fg_color = "transparent", hover_color=("#C7C7C7", "#474747"), image= self.menu, command=lambda: self.abrir_barralat(barralat, central,frameconfig,app))
        menul.place(relx = 0.75, rely = 0.07, relwidth = 0.3,anchor ="center")
        
        
        ##Widgets barra horizontal
        titulo = CTkLabel(master = barrahori, image= self.logo, text="")
        titulo.place(relx = 0.95, rely = 0.75, anchor = "center")
        
        users = CTkButton(master = barralat, text = "", corner_radius = 48, fg_color = "transparent", hover_color=("#C7C7C7", "#474747"), image= self.user, command=lambda: self.mostrar_usuario(app ,usuario))
        users.place(relx = 0.75, rely = 0.85, relwidth = 0.3,anchor ="center")

        configs = CTkButton(master = barralat, text = "", corner_radius = 48, fg_color = "transparent", hover_color=("#C7C7C7", "#474747"), image= self.config, command=lambda: self.abrir_configs(frameconfig))
        configs.place(relx = 0.75, rely = 0.95, relwidth = 0.3,anchor ="center")

        ##Widgets do frameconfig
        btnpremium = CTkButton(master = frameconfig, text= "", corner_radius = 0, fg_color = "transparent", hover_color=("#C7C7C7", "#474747"), image = self.premium,text_color=("#808080", "#A0A0A0"), command=lambda: self.assinar_premium(app, usuario))
        if len(usuario.id_user) == 8:
            btnpremium.configure(text = "Cancelar Premium")
        else:
            btnpremium.configure(text = "Assinar Premium")
        btnpremium.place(relx = 0.5, rely = 0.2, relwidth = 1, anchor = "center")

        btnfechar = CTkButton(master = frameconfig, text= "Fechar", command =lambda: self.close(app), corner_radius = 0, fg_color = "transparent", hover_color=("#C7C7C7", "#474747"), image = self.fechar,text_color=("#808080", "#A0A0A0"))
        btnfechar.place(relx = 0.5, rely = 0.4, relwidth = 1, anchor = "center")

        btnlogout = CTkButton(master = frameconfig, text= "Logout", command =lambda: self.logout(app), corner_radius = 0, fg_color = "transparent", hover_color=("#C7C7C7", "#474747"), image = self.sair,text_color=("#808080", "#A0A0A0"))
        btnlogout.place(relx = 0.5, rely = 0.6, relwidth = 1, anchor = "center")

        changeTheme = CTkSwitch(master= frameconfig, command = self.Tema, text="Tema claro",progress_color= "#1299A0")
        changeTheme.place(relx = 0.4, rely = 0.85, anchor = "center")

        temaimage = CTkLabel(master= frameconfig, text="", image = self.tema)
        temaimage.place(relx = 0.75, rely = 0.85, anchor = "center")
        
        
        ##WIdgets do frame central
        
        ##Inicialização do scroll
        scroll = CTkScrollableFrame(master=central, fg_color="transparent", corner_radius=0)
        scroll.place(relx=0.5, rely=0.52,relwidth=1, relheight = 0.9, anchor="center")

        erro_imagem = CTkLabel(master = central, text="", image= self.busca_fail)
        erro_imagem.place(relx= 0.5, rely=0.5, anchor= "center")
        erro_label = CTkLabel(master = central, text = "Ainda não temos uma lista ou busca, crie uma lista para aparecer os supermercados!", text_color=("#979797", "#3F3F3F"),font=("Montserrat", 16, "bold"))
        erro_label.place(relx= 0.5, rely=0.65, anchor="center")
    
        barra_pesquisa = CTkEntry(master= central, placeholder_text="Pesquise: Ex: Frango, Coca-Cola, Sabão", text_color=("#808080", "#A0A0A0"), corner_radius=2, fg_color = "transparent")
        barra_pesquisa.place(relx =0.5, rely=0.028,relwidth = 0.9,relheight = 0.055,anchor="center")
        
        lista = CTkButton(master= central, image= self.nova_lista, text="",corner_radius =0, fg_color=("#ADB4B4", "#2C2C2C"),hover_color=("#C7C7C7", "#474747"), command = lambda: self.abrir_lista(app))
        lista.place(relx= 0.024, rely=0.028, relwidth = 0.05,relheight = 0.055, anchor="center")
        
        buscar = CTkButton(master= central, image=self.busca, text="",corner_radius =0, fg_color=("#ADB4B4", "#2C2C2C"),hover_color=("#C7C7C7", "#474747"), command =lambda: self.cards(barra_pesquisa, erro_label, erro_imagem, scroll, usuario))
        buscar.place(relx= 0.975, rely=0.028, relwidth = 0.05,relheight = 0.055, anchor="center")
        
        
        
        
        app.mainloop()