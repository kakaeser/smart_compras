from customtkinter import *
import json


class Lista:
    def __init__(self):
        self.lista_compras = []
    
    def abrir_lista(self, app, marks):
        app1 = CTkToplevel(app)
        app1.geometry("500x700")
        app1.title("Lista de Compras")
        app1.transient(master=app)
        
        with open("banco_dados/lista_compras.json", "r", encoding="utf-8") as f:
            setores = json.load(f)
        
        variaveis_produtos = {}

        lista1 = CTkScrollableFrame(master = app1, fg_color="transparent", corner_radius=0)
        lista1.place(relx=0.5, rely=0.475,relwidth=1, relheight = 0.9, anchor="center")
        
        for setor, produtos in setores.items():
            categoria = CTkFrame(master= lista1, fg_color = "transparent")
            categoria.pack(pady=6, padx=20, fill = "x")
            CTkLabel(master=categoria, text=setor, font=("Montserrat", 18, "bold")).pack(anchor ="w", pady=10)
            for produto in produtos:
                var = IntVar()
                chk = CTkCheckBox(master=categoria, text=produto, variable=var,fg_color="#17C5CE", checkbox_height= 16, checkbox_width= 16)
                chk.pack(anchor="w", padx=40)
                variaveis_produtos[produto] = var
        
        salvar = CTkButton(master = app1, text= "Salvar", command = app1.destroy, corner_radius = 0,fg_color="#17C5CE",hover_color="#1299A0")
        salvar.place(relx = 0.35, rely = 0.95, anchor = "center")
        
        cancelar = CTkButton(master = app1, text= "Cancelar", command = app1.destroy, corner_radius = 0,fg_color="transparent",hover_color=("#ADB4B4", "#1B1B1B"), text_color=("#000000", "#FFFFFF"))
        cancelar.place(relx = 0.65, rely = 0.95, anchor = "center")
        
        self.mec_scroll(lista1, categoria)
