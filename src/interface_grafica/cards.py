from customtkinter import *
from usuario_classes.usuario import Usuario
from usuario_classes.usuariopremium import UsuarioPremium
from manipulador_classes.manipulador_sup import Manipulador_Sup
from sup_classes.supermercado import Supermercado
from typing import Union
import random

class Cards:
    def __init__(self) -> None:
        self.cards = [] 
        self.current_expanded_card = None
        
    
    def toggle_card_expansion(self, card: CTkFrame) -> None:
        if not card.winfo_exists():
            return
       
        if card.expandido:
            # Colapsar o card
            card.configure(height=card.original_height)
            card.adicional.place_forget() # Esconde o frame de info adicional
            card.btn_abrir_ref.configure(image = self.not_selected1)
            card.expandido = False
            self.current_expanded_card = None
        else:
            
            if self.current_expanded_card and self.current_expanded_card != card:
                self.toggle_card_expansion(self.current_expanded_card) # Recursivamente colapsa o outro

            # Expandir o card
            card.configure(height=card.expanded_height)
            card.adicional.place(relx=0.5, y = 140, relwidth=0.9, relheight=0.8, anchor="n") 
            card.btn_abrir_ref.configure(image = self.selected1)
            card.expandido = True
            self.current_expanded_card = card

        card.master.update_idletasks()
        
    def abrir_cards(self, scroll:CTkScrollableFrame, usuario:Union[Usuario, UsuarioPremium]) -> None:
        self.fechar_cards()

        self.lista = self.carregar_icones("lista.png", (16,16))
        self.distancia = self.carregar_icones("distancia.png",(16,16))
        
        numero = sum(self.lista_compras.values())
        nomes = Manipulador_Sup.achar_nomes()
        objetos = []

        for nome in nomes:
            dados = Manipulador_Sup.carregar_dados(nome)
            objetos.append(Supermercado(dados))

        objetos.sort(key=lambda sup: sup.preco_final(self.lista_compras))
        
        for inst in objetos:
            card_height_comprimido = 160
            card_height_expandido = 196 + (numero*30)

            card = CTkFrame(master=scroll, fg_color=("#DDE7E7", "#1B1B1B"), corner_radius=8, height= card_height_comprimido)
            card.pack(pady=6, padx=20, fill = "x")

            card.expandido = False
            card.original_height = card_height_comprimido
            card.expanded_height = card_height_expandido

            superlogo = self.carregar_supermercados(inst.imagem, (192,144))

            imagem = CTkLabel(master= card, text = "", image = superlogo)
            imagem.place(relx = 0.14, y = 50, anchor="center")
            
            nome_mercado= CTkLabel(master= card, text = f"{inst.nome} - R${inst.preco_final(self.lista_compras):.2f}", font=("Montserrat", 28, "bold"))
            nome_mercado.place(relx = 0.25, y = 30, anchor="w")

            if len(usuario.id_user) == 8:
                dist = usuario.calcular_distancia(inst.distancia_x,inst.distancia_y)
                distancia = CTkLabel(master= card, text = f" Distância = {dist:.2f}m", font=("Montserrat", 22), compound="left", image = self.distancia)
                if dist >= 1000:
                    dist = dist/1000
                    distancia.configure(text = f"Distância = {dist:.2f}km")
                distancia.place(relx = 0.25, y = 60, anchor="w")

            card.adicional = CTkFrame(master=card, fg_color="transparent")
            
            CTkLabel(master=card.adicional, text=" Lista de produtos:", image = self.lista, font=("Montserrat", 16, "bold"), compound ="left").pack(pady=2, anchor="w")
            for produto_nome, foi_selecionado in self.lista_compras.items():
                if foi_selecionado == 1:
                    CTkLabel(master=card.adicional, text=f"{produto_nome}: R${inst.produtos[produto_nome]}", font=("Montserrat", 16), wraplength=250).pack(pady=2, anchor="w")
                                                                                                                                              
            card.adicional.place_forget()

            btn_abrir= CTkButton(master = card, height= 20, width = 20,text = "", image = self.not_selected1 ,command= lambda current_card=card: self.toggle_card_expansion(current_card), fg_color="transparent", hover_color=("#C8CECE", "#141414"))
            btn_abrir.place(relx = 0.97, y = 30, anchor="center")
            card.btn_abrir_ref = btn_abrir
            
                                                                                                                                           
            
            self.cards.append(card)
            self.mec_scroll(scroll,card, 1)
    
    def fechar_cards(self) -> None:
        for card in self.cards:
            if card.winfo_exists():
                card.destroy()
        self.cards.clear()
        self.current_expanded_card = None