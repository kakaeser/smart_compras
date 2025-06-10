from customtkinter import *
from PIL import Image

class Cards:
    def __init__(self) -> None:
        self.cards = [] 
        self.current_expanded_card = None
    
    def toggle_card_expansion(self, card: CTkFrame) -> None:
        if not card.winfo_exists():
            return
        
        selected = CTkImage(Image.open("imagens/icones/selected.png"), size = (32,32))
        not_selected = CTkImage(Image.open("imagens/icones/not_selected1.png"), size = (32,32))

        if card.expandido:
            # Colapsar o card
            card.configure(height=card.original_height)
            card.adicional.place_forget() # Esconde o frame de info adicional
            card.btn_abrir_ref.configure(image = not_selected)
            card.expandido = False
            self.current_expanded_card = None
        else:
            
            if self.current_expanded_card and self.current_expanded_card != card:
                self.toggle_card_expansion(self.current_expanded_card) # Recursivamente colapsa o outro

            # Expandir o card
            card.configure(height=card.expanded_height)
            card.adicional.place(relx=0.5, y = 140, relwidth=0.9, relheight=0.8, anchor="n") 
            card.btn_abrir_ref.configure(image = selected)
            card.expandido = True
            self.current_expanded_card = card

        card.master.update_idletasks()
        
    def abrir_cards(self, scroll, usuario) -> None:
        self.fechar_cards()
        not_selected = CTkImage(Image.open("imagens/icones/not_selected1.png"), size = (32,32))
        lista = CTkImage(Image.open("imagens/icones/lista.png"), size = (16,16))
        market = CTkImage(Image.open("imagens/supermercados/market.png"), size = (192,144))
        numero = sum(self.lista_compras.values())
        
        for i in range(20):
            card_height_comprimido = 160
            card_height_expandido = 196 + (numero*30)

            card = CTkFrame(master=scroll, fg_color=("#DDE7E7", "#1B1B1B"), corner_radius=8, height= card_height_comprimido)
            card.pack(pady=6, padx=20, fill = "x")

            card.expandido = False
            card.original_height = card_height_comprimido
            card.expanded_height = card_height_expandido

            imagem = CTkLabel(master= card, text = "", image = market)
            imagem.place(relx = 0.14, y = 50, anchor="center")
            
            nome_mercado= CTkLabel(master= card, text = f"Supermercado {i+1} - R${i+15},00", font=("Montserrat", 28, "bold"))
            nome_mercado.place(relx = 0.475, y = 30, anchor="center")

            if len(usuario.id_user) == 8:
                distancia = CTkLabel(master= card, text = f"Distância = {usuario.calcular_distancia(i*100,0)}m", font=("Montserrat", 22))
                distancia.place(relx = 0.375, y = 60, anchor="center")

            card.adicional = CTkFrame(master=card, fg_color="transparent")
            
            CTkLabel(master=card.adicional, text=" Lista de produtos:", image = lista, font=("Montserrat", 16, "bold"), compound ="left").pack(pady=2, anchor="w")
            for i in range(numero):
                CTkLabel(master=card.adicional, text=f"Produtos {i+1}: R${i+15},00", font=("Montserrat", 16), wraplength=250).pack(pady=2, anchor="w")
                                                                                                                                              
            card.adicional.place_forget()

            btn_abrir= CTkButton(master = card, height= 20, width = 20,text = "", image = not_selected ,command= lambda current_card=card: self.toggle_card_expansion(current_card), fg_color="transparent", hover_color=("#C8CECE", "#141414"))
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
    