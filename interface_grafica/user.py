from customtkinter import *
from banco_dados.manipulador_user import Manipulador_User
from PIL import Image

class User():
    #Inicialização de uma janela que mostra os dados do usuario e pode edita-los
  def mostrar_usuario(self,app,usuario) -> None:
    app1 = CTkToplevel(app)
    app1.geometry("500x700")
    app1.title("Usuário")
    app1.transient(master=app)

    edit = CTkImage(Image.open("imagens/icones/editar.png"), size = (16,16))
    verificar = CTkImage(Image.open("imagens/icones/verificar.png"), size = (16,16))

    ##Apenas para Windows
    if os =="Windows":
        app1.wm_attributes("-toolwindow", True)
  
    open_user = CTkFrame(master = app1, width = 500, height = 700, fg_color=("#DDE7E7", "#2C2C2C"))
    open_user.place(relx= 0.5, rely = 0.5, anchor = "center")
    entry_vars = {} 
    entries = {} 
    
    erro_label = CTkLabel(master = open_user, text="", text_color="red")
    erro_label.place(relx = 0.5, rely = 0.65, anchor="center")

    idd = CTkEntry(master=open_user, placeholder_text= usuario.id_user, text_color=("#808080", "#A0A0A0"), corner_radius=2)
    
    valores_originais = {
        "nome": usuario.nome,
        "email": usuario.email,
        "senha": usuario.senha,
        "cpf": usuario.cpf,
        "cep": usuario.cep
    }
  
    def checagem_alterar() -> None:
        
        mudanca = False
        if idd.get() != "":
            mudanca = True
        for key in valores_originais:
            current_value = entry_vars[key].get() 
            if current_value != "" and current_value != valores_originais[key]:
                mudanca = True
                break 
  
        if mudanca:
            alterar.configure(fg_color="#17C5CE", hover_color="#1299A0", state="normal")
        else:
            alterar.configure(fg_color="transparent", state="disabled")
  
    def edicao(campo_widget) -> None: 
        campo_widget.configure(state="normal", text_color=("#000000", "#FFFFFF")) 
        checagem_alterar()
  
    def alterar_dados() -> None:
        if len(idd.get()) != 4:
            erro_label.configure(text="ID inválido, use apenas 4 numeros")
            return
        else:
            idn = usuario.calcular_novo_id(idd.get())
        if len(entry_vars["cpf"].get()) != 11:
            erro_label.configure(text="CPF inválido")
            return
        if len(entry_vars["cep"].get()) != 8 and len(entry_vars["cep"].get()) != 9:
            erro_label.configure(text="CEP inválido")
            return
        if entry_vars["nome"].get() != "" and entry_vars["nome"].get() !=valores_originais["nome"]:
            verificador = Manipulador_User.conferir_dados(entry_vars["nome"].get())
            if verificador == 1:
                erro_label.configure(text="Nome de usuario já cadastrado")
                return
            else:
                Manipulador_User.editar_dados(usuario.nome, "nome", entry_vars["nome"].get())
                usuario.alterar_nome(entry_vars["nome"].get())
        if entry_vars["email"].get() != "" and entry_vars["email"].get() !=valores_originais["email"]:
            verificador = Manipulador_User.conferir_dados(entry_vars["email"].get())
            if verificador == 2:
                erro_label.configure(text="Email já cadastrado")
                return
            else:
                Manipulador_User.editar_dados(usuario.nome, "email", entry_vars["email"].get())
                usuario.alterar_email(entry_vars["email"].get())
        if entry_vars["senha"].get() != "" and entry_vars["senha"].get() !=valores_originais["senha"]:
            Manipulador_User.editar_dados(usuario.nome, "senha", entry_vars["senha"].get())
            usuario.alterar_senha(entry_vars["senha"].get())
        if entry_vars["cpf"].get() != "" and entry_vars["cpf"].get() !=valores_originais["cpf"]:
            verificador = Manipulador_User.conferir_dados(entry_vars["cpf"].get())
            if verificador == 3:
                erro_label.configure(text="CPF já cadastrado")
                return
            else:
                Manipulador_User.editar_dados(usuario.nome, "cpf", entry_vars["cpf"].get())
                usuario.alterar_cpf(entry_vars["cpf"].get())
        if idd.get() != "" and idn != usuario.id_user:
            verificador = Manipulador_User.conferir_dados(idn)
            if verificador == 4:
                erro_label.configure(text="ID já cadastrado")
                return
            else:
                Manipulador_User.editar_dados(usuario.nome, "id_user", idn)
                usuario.alterar_id(idn)

        if entry_vars["cep"].get() != "" and entry_vars["cep"].get() !=valores_originais["cep"]:
            Manipulador_User.editar_dados(usuario.nome, "cep", entry_vars["cep"].get())
            usuario.alterar_cep(entry_vars["cep"].get())
  
        app1.destroy()
  
    campos_config = {
        "nome": (usuario.nome, 0.2),
        "email": (usuario.email, 0.3),
        "senha": (usuario.senha, 0.4),
        "cpf": (usuario.cpf, 0.5),
        "cep": (usuario.cep, 0.6)
    }
  
    for key, (placeholder, rely_pos) in campos_config.items():
       
        entry_var = StringVar(master=open_user, value=placeholder)
        entry_vars[key] = entry_var
  
        entry = CTkEntry(master=open_user, textvariable=entry_var, text_color=("#808080", "#A0A0A0"), corner_radius=2)
        entry.configure(state="disabled") 
        entry.place(relx=0.46, rely=rely_pos, relwidth=0.38, relheight=0.046, anchor="center")
        entries[key] = entry 
        entry_var.trace_add("write", lambda name, index, mode: checagem_alterar())
  
        btn_editar = CTkButton(master=open_user, command=lambda e=entry: edicao(e), text="", corner_radius=2, fg_color=("#ADB4B4", "#1B1B1B"),hover_color=("#C7C7C7", "#474747"), image = edit)
        btn_editar.place(relx=0.68, rely=rely_pos, relwidth=0.064, relheight=0.046, anchor="center")
  
    titulo = CTkLabel(master= open_user, text= f"Usuario id: {usuario.id_user}" ,text_color=("#808080", "#A0A0A0"),font = ("Montserrat", 16, "bold"))
    titulo.place(relx=0.43, rely=0.1, anchor="center")

    def edit_id():
        idd.place(relx=0.43, rely=0.1,relwidth=0.38, relheight=0.046, anchor="center")
        titulo.configure(text="")
        titulo.place(rely=0, relx=0, anchor="center")
        btn_id.configure(image = verificar)
        checagem_alterar()

    btn_id = CTkButton(master=open_user, text="", corner_radius=2, fg_color=("#ADB4B4", "#1B1B1B"),hover_color=("#C7C7C7", "#474747"), image = edit, command = edit_id)
    if len(usuario.id_user) == 8:
        btn_id.place(relx=0.68, rely=0.1,relwidth=0.064, relheight=0.046, anchor="center")

  
    label1 = CTkLabel(master= open_user, text= "Nome:" ,text_color=("#808080", "#A0A0A0"),font = ("Montserrat", 12))
    label1.place(relx=0.31, rely=0.15, anchor="center")
  
    label2 = CTkLabel(master= open_user, text= "Email:" ,text_color=("#808080", "#A0A0A0"),font = ("Montserrat", 12))
    label2.place(relx=0.31, rely=0.25, anchor="center")
  
    label3 = CTkLabel(master= open_user, text= "Senha:" ,text_color=("#808080", "#A0A0A0"),font = ("Montserrat", 12))
    label3.place(relx=0.31, rely=0.35, anchor="center")
  
    label4 = CTkLabel(master= open_user, text= "CPF:" ,text_color=("#808080", "#A0A0A0"),font = ("Montserrat", 12))
    label4.place(relx=0.3, rely=0.45, anchor="center")
  
    label5 = CTkLabel(master= open_user, text= "CEP:" ,text_color=("#808080", "#A0A0A0"),font = ("Montserrat", 12))
    label5.place(relx=0.3, rely=0.55, anchor="center")
    
    
    cancelar = CTkButton(master = open_user, text= "Cancelar", command = app1.destroy, corner_radius = 0, fg_color="transparent",hover_color=("#ADB4B4", "#1B1B1B"), text_color=("#000000", "#FFFFFF"))
    cancelar.place(relx = 0.7, rely = 0.75, anchor = "center")
  
    alterar = CTkButton(master = open_user, text= "Alterar", corner_radius = 0, command = alterar_dados)
    alterar.place(relx = 0.3, rely = 0.75, anchor = "center")
    checagem_alterar()