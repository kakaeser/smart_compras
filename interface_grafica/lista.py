from customtkinter import *

class Lista:
    def abrir_lista(self, app, marks):
        app1 = CTkToplevel(app)
        app1.geometry("500x700")
        app1.title("Lista de Compras")
        app1.transient(master=app)

        lista1 = CTkScrollableFrame(master = app1, fg_color="transparent", corner_radius=0)
        lista1.place(relx=0.5, rely=0.5,relwidth=1, relheight = 1, anchor="center")
