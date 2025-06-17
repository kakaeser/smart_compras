from customtkinter import *
from manipulador_classes.manipulador_user import Manipulador_User
import re

class Cadastro:
     
     def forma_pagamento(self, app, comando)-> None:
         def aplicar_comando():
            credito.destroy()
            debito.destroy()
            pix.destroy()
            comando()
            
         credito = CTkButton(master= app, text= "Crédito", command= aplicar_comando, corner_radius=32,fg_color="#17C5CE",hover_color="#1299A0")
         credito.place(relx = 0.5, rely = 0.4, anchor="center")

         debito = CTkButton(master= app, text= "Debito", command= aplicar_comando, corner_radius=32,fg_color="#17C5CE",hover_color="#1299A0")
         debito.place(relx = 0.5, rely = 0.5, anchor="center")

         pix = CTkButton(master= app, text= "PIX", command= aplicar_comando, corner_radius=32,fg_color="#17C5CE",hover_color="#1299A0")
         pix.place(relx = 0.5, rely = 0.6, anchor="center")
     
     def cadastro(self) -> None:
        app = CTk()
        app.geometry("500x700")
        app.title("Cadastrar")

        cadastro = CTkFrame(master = app, fg_color=("#DDE7E7", "#2C2C2C"),width = 500, height = 700 )
        cadastro.place(relx = 0.5, rely = 0.5,anchor = "center")
        select : bool
        

        erro_label = CTkLabel(master=cadastro, text="", text_color="red")
        erro_label.place(relx=0.5, rely=0.85, anchor="center")

        textin = CTkLabel(master=cadastro, text="Insira os dados :", font = ("Montserrat", 12))

        user = CTkEntry(master = cadastro, placeholder_text= "Nome")

        email = CTkEntry(master= cadastro, placeholder_text="Email")

        cpf = CTkEntry(master= cadastro, placeholder_text="CPF")

        cep = CTkEntry(master= cadastro, placeholder_text="CEP")
    
        password = CTkEntry(master= cadastro, placeholder_text="Senha", show = "*")
        
        cpassword = CTkEntry(master= cadastro, placeholder_text="Confirmar Senha", show = "*")
        
        #Função que le e mostra os termos de compromisso
        def termos() -> None:
            termo = CTkTextbox(master= cadastro)
            try:
                with open("../banco_dados/termos.txt", "r", encoding="utf-8") as arquivo:
                    conteudo = arquivo.read()
                    termo.insert("0.0", conteudo)
            except FileNotFoundError:
                termo.insert("0.0", "Arquivo de termos não encontrado.")
            termo.configure(state="disabled")
            termo.place(relx = 0.5, rely = 0.4, relwidth = 0.6 , relheight= 0.6,anchor ="center")
            
            #Função que faz aparecer a tela de criação de usuario apos o usuario aceitar o termo
            def criacao() -> None:
                termo.destroy()
                mostrar.destroy()
                confirm.destroy()
                
                textin.place(relx = 0.4, rely = 0.33, relwidth = 0.25, relheight = 0.08, anchor = "center")
                user.place(relx = 0.5, rely = 0.2, relwidth = 0.5, relheight = 0.08, anchor="center")
                email.place(relx = 0.5, rely = 0.3, relwidth = 0.5, relheight = 0.08, anchor="center")
                cpf.place(relx = 0.5, rely = 0.4, relwidth = 0.5, relheight = 0.08, anchor="center")
                cep.place(relx = 0.5, rely = 0.5, relwidth = 0.5, relheight = 0.08, anchor="center")
                password.place(relx = 0.5, rely = 0.6, relwidth = 0.5, relheight = 0.08, anchor="center")
                cpassword.place(relx = 0.5, rely = 0.7, relwidth = 0.5, relheight = 0.08, anchor="center")
                btn.place(relx = 0.5, rely = 0.8, relwidth = 0.25, anchor = "center")

            confirm = CTkButton(master=cadastro, text="Continuar", corner_radius=32,fg_color="transparent")
            confirm.place(relx = 0.5, rely = 0.8, relwidth = 0.25, anchor = "center")
            
            #Função que ve se o usuario aceitou ou não os termos de compromisso
            def aceitar() -> None:
                if mostrar.get() == 1:
                    confirm.configure(fg_color="#17C5CE",hover_color="#1299A0", state ="normal",command= criacao)
                else:
                    confirm.configure(fg_color="transparent", state = "disabled" , command=lambda: None)

            mostrar = CTkCheckBox(master= cadastro, text="Li e concordo com os termos", corner_radius= 4, fg_color="#17C5CE", checkbox_height= 16, checkbox_width= 16, command= aceitar )
            mostrar.place(relx = 0.5, rely = 0.75, relwidth = 0.4, relheight = 0.03, anchor = "center")

        #Seleção de plano premium    
        def premium_select() -> None:
            nonlocal select 
            select = True
            normal.destroy()
            premium.destroy()
            self.forma_pagamento(app, termos)
        #Seleção de plano gratuito
        def normal_select() -> None:
            nonlocal select 
            select = False
            normal.destroy()
            premium.destroy()
            termos()

        
        #Autentificador de dados coletados, previne email e usuarios repetidos
        def autenticar() -> None:
            email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            senha_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$"
            if user.get() == "" or email.get() == "" or cpf.get() == "" or cep.get() == "" or password.get() == "" or cpassword.get() == "":
                erro_label.configure(text="Você não preencheu todos os campos!!")
                return
            if not user.get().isalnum():
                erro_label.configure(text="Nome inválido, não utilize espaços ou caracteres especiais")
                return
            
            if not re.fullmatch(email_regex, email.get()):
                erro_label.configure(text="Email inválido. Verifique o formato (ex: nome@dominio.com).")
                return
            
            if len(cpf.get()) != 11 or not cpf.get().isdigit():
                erro_label.configure(text="CPF inválido")
                return
            
            cep_limpo = cep.get().replace("-", "")
            if not (len(cep_limpo) == 8) or not cep.get().isdigit():
                erro_label.configure(text="CEP inválido")
                return
            
            if len(password.get()) < 8:
                erro_label.configure(text="Sua senha é muito fraca, coloque pelo menos 8 caracteres")
                return
            
            if not re.search(r"\S", password.get()): 
                erro_label.configure(text="Sua senha não deve ter espaços")
                return
            
            if not re.fullmatch(senha_regex, password.get()):
                erro_label.configure(text="Sua senha deve ter pelo menos uma letra maiúscula e um número")
                return

            if cpassword.get() != password.get():
                erro_label.configure(text="Sua senha não é a mesma que você quis confirmar")
                return
                
            sucesso = Manipulador_User.salvar_dados(user.get(),email.get(),password.get(), cpf.get(), cep.get(), select)
            if not sucesso:
                erro_label.configure(text="Usuário ou email já existem")
                return
            
            self.nome = user.get()
            self.email = email.get()
            self.senha = password.get()
            app.destroy()

        
        #Selecionador de Planos
        normal = CTkButton(master = cadastro, text = "Plano padrão \n\n R$00,00\n\n ● Calculo de qual\nsupermercado é\nmais economico\n\n ● Pequenas ofertas", fg_color= "transparent", border_color= "#17C5CE", border_width=2, hover_color=("#B4B4B4", "#161616"), text_color=("#000000", "#FFFFFF"),font=("Arial", 16, "bold"), command = normal_select)
        normal.place(relx = 0.28, rely = 0.5, relwidth = 0.4 , relheight= 0.6,anchor ="center")

        premium = CTkButton(master = cadastro,text = "Plano Premium \n\n R$12,90\n\n ● Ofertas maiores \n\n ● Calcula o gasto de \ncombustivel\n\n ● Visualização de\nchegada de produtos", fg_color= "transparent", border_color= "#17C5CE", border_width=2, hover_color=("#B4B4B4", "#161616"), text_color=("#000000", "#FFFFFF"),font=("Arial", 16, "bold"), command= premium_select)
        premium.place(relx = 0.72, rely = 0.5, relwidth = 0.4 , relheight= 0.6,anchor ="center")

        btn = CTkButton(master=cadastro, text="Criar", corner_radius=32,fg_color="#17C5CE",hover_color="#1299A0", command= autenticar)
        
        app.mainloop()


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


    
            