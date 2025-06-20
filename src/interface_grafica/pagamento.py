from PIL import Image
from customtkinter import *
import os

class Pagamento:
    def toppix(self, app: CTkToplevel):
        frame_pix = CTkToplevel(app)
        frame_pix.geometry("600x700")
        frame_pix.title("PIX")
        frame_pix.transient(master=app)
        caminho_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        caminho_icones = os.path.join(caminho_base, "..","images", "icones", "pix.png")
        imagem = CTkImage(dark_image= Image.open(caminho_icones),size = (512, 512))
        imagem_pix = CTkLabel(master = frame_pix, text = "", image = imagem)
        imagem_pix.place(relx = 0.5, rely = 0.5, anchor="center")
        
    def forma_pagamento(self, app: CTk, comando:str)-> None:
         def aplicar_comando():
            credito.destroy()
            debito.destroy()
            label.destroy()
            pix.destroy()
            if comando == "termos":
                self.termos(app) 
            else:
                comando()
         def aplicar_pix():
            self.toppix(app)
            credito.destroy()
            debito.destroy()
            label.place(relx = 0.5, rely = 0.5, anchor="center")
            pix.configure(command = aplicar_comando, text ="Continuar")
            

         credito = CTkButton(master= app, text= "Crédito", command= aplicar_comando, corner_radius=32,fg_color="#17C5CE",hover_color="#1299A0")
         credito.place(relx = 0.5, rely = 0.4, anchor="center")

         debito = CTkButton(master= app, text= "Debito", command= aplicar_comando, corner_radius=32,fg_color="#17C5CE",hover_color="#1299A0")
         debito.place(relx = 0.5, rely = 0.5, anchor="center")

         pix = CTkButton(master= app, text= "PIX", command= aplicar_pix, corner_radius=32,fg_color="#17C5CE",hover_color="#1299A0")
         pix.place(relx = 0.5, rely = 0.6, anchor="center")

         label = CTkLabel(master = app, text="Você sabe que não precisa realmente fazer o pix né?? hehehe")
