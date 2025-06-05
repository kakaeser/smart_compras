from customtkinter import *
from banco_dados.manipulador_user import Manipulador_User
from classes.usuario import Usuario
from classes.usuariopremium import UsuarioPremium
from PIL import Image

class Cards:
    def __init__(self) -> None:
        self.cards = [] 
        
    def abrir_cards(self, scroll) -> None:
        self.cards = [] 
        for i in range(20):
            card = CTkFrame(master=scroll, fg_color=("#DDE7E7", "#1B1B1B"), corner_radius=8)
            card.pack(pady=6, padx=20, fill = "x")
            
            nome_mercado= CTkLabel(master= card, text = f"Supermercado {i+1}", font=("Montserrat", 16, "bold"))
            nome_mercado.place(relx = 0.2, rely = 0.3, anchor="center")
            
            btn_abrir= CTkButton(master = card, text = "Abrir")
            btn_abrir.place(relx = 0.9, rely = 0.3, anchor="center")
            
            preco = CTkLabel(master= card, text = "R$00,00", font=("Montserrat", 14, "bold"))
            preco.place(relx = 0.2, rely = 0.6, anchor="center")
            
            
            self.cards.append(card)
            self.mec_scroll(scroll,card)
    
    def fechar_cards(self) -> None:
        for card in self.cards:
            if card.winfo_exists():
                card.destroy()
        self.cards.clear()
    