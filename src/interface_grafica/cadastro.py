from customtkinter import *
from manipulador_classes.manipulador_user import Manipulador_User
import re

class Cadastro:
     def __init__(self):
        self.textin = None
        self.user = None
        self.email_ = None
        self.cep= None
        self.cpf = None
        self.password = None
        self.cpassword = None
        self.select = None
        self.ipix = None
        
          
     def criacao(self, termo: CTkTextbox, mostrar: CTkCheckBox, confirm: CTkButton, app: CTkToplevel) -> None:
        termo.destroy()
        mostrar.destroy()
        confirm.destroy()

        self.textin = CTkLabel(master = app,text="Insira os dados :", font = ("Montserrat", 12))
        self.user = CTkEntry(master = app,placeholder_text= "Nome")
        self.email_ = CTkEntry(master = app,placeholder_text="Email")
        self.cpf = CTkEntry(master = app,placeholder_text="CPF")
        self.cep = CTkEntry(master = app,placeholder_text="CEP")
        self.password = CTkEntry(master = app,placeholder_text="Senha", show = "*")
        self.cpassword = CTkEntry(master = app,placeholder_text="Confirmar Senha", show = "*")
        
        
        self.textin.place(relx = 0.4, rely = 0.33, relwidth = 0.25, relheight = 0.08, anchor = "center")
        self.user.place(relx = 0.5, rely = 0.2, relwidth = 0.5, relheight = 0.08, anchor="center") 
        self.email_.place(relx = 0.5, rely = 0.3, relwidth = 0.5, relheight = 0.08, anchor="center") 
        self.cpf.place(relx = 0.5, rely = 0.4, relwidth = 0.5, relheight = 0.08, anchor="center") 
        self.cep.place(relx = 0.5, rely = 0.5, relwidth = 0.5, relheight = 0.08, anchor="center")
        self.password.place(relx = 0.5, rely = 0.6, relwidth = 0.5, relheight = 0.08, anchor="center")
        self.cpassword.place(relx = 0.5, rely = 0.7, relwidth = 0.5, relheight = 0.08, anchor="center") 
        self.btn.place(relx = 0.5, rely = 0.8, relwidth = 0.25, anchor = "center")
    #Seleção de plano premium    
     def premium_select(self, normal: CTkButton, premium: CTkButton, app : CTkToplevel) -> None: 
        self.select = True
        normal.destroy()
        premium.destroy()
        self.forma_pagamento(app,"termos")

    #Seleção de plano gratuito
     def normal_select(self, normal: CTkButton, premium: CTkButton, app: CTkToplevel) -> None:
        self.select = False
        normal.destroy()
        premium.destroy()
        self.termos(app)
    
     
     def termos(self,app: CTkToplevel) -> None:
            termo = CTkTextbox(master= app)
            pasta_base = os.path.dirname(__file__)
            caminho = os.path.join(pasta_base,".." ,"..", "banco_dados", "termos.txt")
            try:
                with open(caminho, "r", encoding="utf-8") as arquivo:
                    conteudo = arquivo.read()
                    termo.insert("0.0", conteudo)
            except FileNotFoundError:
                termo.insert("0.0", "Arquivo de termos não encontrado.")
            termo.configure(state="disabled")
            termo.place(relx = 0.5, rely = 0.4, relwidth = 0.6 , relheight= 0.6,anchor ="center")
        
            confirm = CTkButton(master=app, text="Continuar", corner_radius=32,fg_color="transparent")
            confirm.place(relx = 0.5, rely = 0.8, relwidth = 0.25, anchor = "center")
            
            
            #Função que ve se o usuario aceitou ou não os termos de compromisso
            def aceitar() -> None:
                if mostrar.get() == 1:
                    confirm.configure(fg_color="#17C5CE",hover_color="#1299A0", state ="normal",command=lambda: self.criacao(termo, mostrar, confirm,app))
                else:
                    confirm.configure(fg_color="transparent", state = "disabled" , command=lambda: None)

            mostrar = CTkCheckBox(master= app, text="Li e concordo com os termos", corner_radius= 4, fg_color="#17C5CE", checkbox_height= 16, checkbox_width= 16, command= aceitar )
            mostrar.place(relx = 0.5, rely = 0.75, relwidth = 0.4, relheight = 0.03, anchor = "center")
     #Autentificador de dados coletados, previne email e usuarios repetidos
     def autenticar(self, erro_label: CTkLabel, app: CTkToplevel) -> None:
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        senha_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$"
        if self.user.get() == "" or self.email_.get() == "" or self.cpf.get() == "" or self.cep.get() == "" or self.password.get() == "" or self.cpassword.get() == "":
            erro_label.configure(text="Você não preencheu todos os campos!!")
            return
        if not self.user.get().isalnum():
            erro_label.configure(text="Nome inválido, não utilize espaços ou caracteres especiais")
            return
        
        if not re.fullmatch(email_regex, self.email_.get()):
            erro_label.configure(text="Email inválido. Verifique o formato (ex: nome@dominio.com).")
            return
        
        if len(self.cpf.get()) != 11 or not self.cpf.get().isdigit():
            erro_label.configure(text="CPF inválido")
            return
        
        cep_limpo = self.cep.get().replace("-", "")
        if not (len(cep_limpo) == 8) or not self.cep.get().isdigit():
            erro_label.configure(text="CEP inválido")
            return
        
        if len(self.password.get()) < 8:
            erro_label.configure(text="Sua senha é muito fraca, coloque pelo menos 8 caracteres")
            return
        
        if not re.search(r"\S", self.password.get()): 
            erro_label.configure(text="Sua senha não deve ter espaços")
            return
        
        if not re.fullmatch(senha_regex, self.password.get()):
            erro_label.configure(text="Sua senha deve ter pelo menos uma letra maiúscula e um número")
            return

        if self.cpassword.get() != self.password.get():
            erro_label.configure(text="Sua senha não é a mesma que você quis confirmar")
            return
            
        sucesso = Manipulador_User.salvar_dados(self.user.get(),self.email_.get(),self.password.get(), self.cpf.get(), self.cep.get(), self.select)
        if not sucesso:
            erro_label.configure(text="Usuário ou email já existem")
            return
        
        self.nome = self.user.get()
        self.email = self.email_.get()
        self.senha = self.password.get()
        app.destroy()

     def cadastro(self, login:CTk) -> None:
        app = CTkToplevel(login)
        app.geometry("500x700")
        app.title("Cadastrar")
        app.transient(master=login)
        
        erro_label = CTkLabel(master=app, text="", text_color="red")
        erro_label.place(relx=0.5, rely=0.85, anchor="center")

        #Selecionador de Planos
        normal = CTkButton(master = app, text = "Plano padrão \n\n R$00,00\n\n ● Calculo de qual\nsupermercado é\nmais economico\n\n ● Pequenas ofertas", fg_color= "transparent", border_color= "#17C5CE", border_width=2, hover_color=("#B4B4B4", "#161616"), text_color=("#000000", "#FFFFFF"),font=("Arial", 16, "bold"), command =lambda: self.normal_select(normal, premium, app))
        normal.place(relx = 0.28, rely = 0.5, relwidth = 0.4 , relheight= 0.6,anchor ="center")

        premium = CTkButton(master = app,text = "Plano Premium \n\n R$12,90\n\n ● Ofertas maiores \n\n ● Calcula o gasto de \ncombustivel\n\n ● Visualização de\nchegada de produtos", fg_color= "transparent", border_color= "#17C5CE", border_width=2, hover_color=("#B4B4B4", "#161616"), text_color=("#000000", "#FFFFFF"),font=("Arial", 16, "bold"), command=lambda: self.premium_select(normal, premium, app))
        premium.place(relx = 0.72, rely = 0.5, relwidth = 0.4 , relheight= 0.6,anchor ="center")

        self.btn = CTkButton(master=app, text="Criar", corner_radius=32,fg_color="#17C5CE",hover_color="#1299A0", command=lambda: self.autenticar(erro_label, app))
        

     def assinar_premium (self, app, usuario)-> None:
        app1 = CTkToplevel(app)
        app1.geometry("500x700")
        app1.title("Plano Premium")
        app1.transient(master=app)

        def edicaop_id():
                Manipulador_User.editar_dados(usuario.nome, "id", usuario.id_user + "P")
                self.fechar_cards()
                app1.destroy()
                app.destroy()
                self.App()

        def edicaon_id():
                novo_id = usuario.id_user[:-1]
                Manipulador_User.editar_dados(usuario.nome, "id", novo_id)
                self.fechar_cards()
                app1.destroy()
                app.destroy()
                self.App()

        def assinar():
            premium.destroy()
            self.forma_pagamento(app1,edicaop_id)

        if len(usuario.id_user) == 7:
            premium = CTkButton(master = app1 ,text = "Plano Premium \n\n R$12,90\n\n ● Ofertas maiores \n\n ● Calcula o gasto de \ncombustivel\n\n ● Visualização de\nchegada de produtos", fg_color= "transparent", border_color= "#17C5CE", border_width=2, hover_color=("#B4B4B4", "#161616"), text_color=("#000000", "#FFFFFF"),font=("Arial", 16, "bold"), command = assinar)
            premium.place(relx = 0.5, rely = 0.5, relwidth = 0.8 , relheight= 0.6,anchor ="center")
        else:
            texto = CTkLabel(master = app1, text= "Tem certeza que quer cancelar seu plano premium?")
            texto.place(relx = 0.5, rely = 0.5, anchor ="center")

            confirmar = CTkButton(master= app1, text="Sim", command = edicaon_id, fg_color="#17C5CE",hover_color="#1299A0")
            confirmar.place(relx=0.35, rely = 0.6, anchor="center")

            cancelar = CTkButton(master = app1, text = "Cancelar",fg_color="transparent",hover_color=("#ADB4B4", "#1B1B1B"), text_color=("#000000", "#FFFFFF"), command= app1.destroy)
            cancelar.place(relx = 0.65, rely = 0.6, anchor = "center")

        app1.mainloop()


    
            