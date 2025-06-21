from customtkinter import *
from PIL import Image
import json


class Lista:
    def __init__(self):
        self.lista_compras = {} 
        pasta_base = os.path.dirname(__file__)
        self.caminho_lista = os.path.join(pasta_base,".." ,"..", "banco_dados", "lista_compras.json")

    def hover_on(self, event, botao: CTkLabel) -> None:
        botao.configure(font=("Montserrat", 18, "underline", "bold"))

    def hover_off(self, event, botao:CTkLabel) -> None:
        botao.configure(font=("Montserrat", 18, "bold"))
    
    def expandir_lista(self, categoria:CTkFrame) -> None:
        if categoria.expandido:
            categoria.expandido= False
            categoria.botao_ref.configure(image = self.not_selected2)
            categoria.adicional.pack_forget()
        else:
            categoria.expandido= True
            categoria.botao_ref.configure(image = self.selected2)
            categoria.adicional.pack(anchor="w", padx=20)

        categoria.master.update_idletasks()

    
    def abrir_lista(self, app) -> None:
        app1 = CTkToplevel(app)
        app1.geometry("500x700")
        app1.title("Lista de Compras")
        app1.transient(master=app)

        self.selected2 = self.carregar_icones("selected.png", (16,16))
        self.not_selected2 = self.carregar_icones("not_selected2.png", (16,16))

        with open(self.caminho_lista, "r", encoding="utf-8") as f:
            setores = json.load(f)
        
        variaveis_produtos = {}

        def salvar(identificador) -> None:
            self.lista_compras = {}
            for produto, var in identificador.items():
                self.lista_compras[produto] = var.get()
            
            app1.destroy()


        lista1 = CTkScrollableFrame(master = app1, fg_color="transparent", corner_radius=0)
        lista1.place(relx=0.5, rely=0.475,relwidth=1, relheight = 0.9, anchor="center")

        
        for setor, produtos in setores.items():
            categoria = CTkFrame(master= lista1, fg_color = "transparent")
            categoria.pack(pady=6, padx=(5,20), fill = "x", anchor= "w")

            categoria1 = CTkFrame(master= categoria, fg_color="transparent")
            categoria1.pack(fill="x", anchor="w")

            imagem_categoria = CTkLabel(master= categoria1,text=" " + setor,image = self.not_selected2 ,font=("Montserrat", 18, "bold"), fg_color="transparent",text_color=("#808080", "#A0A0A0"),anchor="w", compound="left", cursor="hand2")
            imagem_categoria.pack(fill="x", anchor="w", pady=10, padx=(0,0))

            imagem_categoria.bind("<Button-1>", lambda event, current_categoria=categoria: self.expandir_lista(current_categoria))
            imagem_categoria.bind("<Enter>", lambda event, lbl=imagem_categoria: self.hover_on(event, lbl))
            imagem_categoria.bind("<Leave>", lambda event, lbl=imagem_categoria: self.hover_off(event, lbl))

            categoria.expandido = False
            categoria.botao_ref = imagem_categoria

            categoria.adicional = CTkFrame(master=categoria, fg_color="transparent")
            for produto in produtos:
                var = IntVar()
                chk = CTkCheckBox(master=categoria.adicional, text=produto, variable=var,fg_color="#17C5CE", checkbox_height= 16, checkbox_width= 16)
                chk.pack(anchor="w", padx=40)
                variaveis_produtos[produto] = var
                
                self.mec_scroll(lista1, categoria, 4)
        
        btn_salvar = CTkButton(master = app1, text= "Salvar", command = lambda: salvar(variaveis_produtos), corner_radius = 0,fg_color="#17C5CE",hover_color="#1299A0")
        btn_salvar.place(relx = 0.35, rely = 0.96, anchor = "center")
        
        cancelar = CTkButton(master = app1, text= "Cancelar", command = app1.destroy, corner_radius = 0,fg_color="transparent",hover_color=("#ADB4B4", "#1B1B1B"), text_color=("#000000", "#FFFFFF"))
        cancelar.place(relx = 0.65, rely = 0.96, anchor = "center")
        
        
