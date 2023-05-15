#----------------------------------------------------------librerias
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
import pymysql
#----------------------------------------------------------variables
global id_seleccionado, guardar, cliente, buscar
cliente = 0
guardar = "sin valor"
buscar = "sin valor"
dni_1 = 0
codigo_1 = 0
#----------------------------------------------------------ventana uno
def fun_ventana_uno():
    global ventana_uno
    #------------------------------------------------------ventana
    ventana_uno=Tk()
    ventana_uno.title("Ventana 1")
    w = 400
    h = 220
    ws = ventana_uno.winfo_screenwidth()
    hs = ventana_uno.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    ventana_uno.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def de_v1_is():
        ventana_uno.destroy()
        fun_iniciar_sesion()
    #------------------------------------------------------imagenes
    img_net = Image.open("Imágenes/net.gif")
    resized = img_net.resize((250, 125))
    img_net = ImageTk.PhotoImage(resized)
    label_imagen = Label(ventana_uno, image=img_net)
    label_imagen.pack()
    label_imagen.place(x=70 ,y=5)
    #------------------------------------------------------botones
    Btn_registrarse = Button(ventana_uno,text="registrarse", command=ventana_registrarse, bg="#1a2d99", fg="white")
    Btn_registrarse.pack()
    Btn_registrarse.place(x=200,y=160)

    Btn_iniciar_sesion = Button(ventana_uno,text="inciar ssion", command=de_v1_is, bg="#5ab507", fg="white")
    Btn_iniciar_sesion.pack()
    Btn_iniciar_sesion.place(x=100,y=160)
    #------------------------------------------------------mainloop
    mainloop()
#----------------------------------------------------------iniciar secion
def fun_iniciar_sesion():
    global ventana_iniciar_sesion
    global entry_usuario
    global entry_contraseña
    global inicio_de_sesion
    #------------------------------------------------------ventana
    ventana_iniciar_sesion=Tk()
    ventana_iniciar_sesion.title("iniciar sesion")
    w = 200
    h = 220
    ws = ventana_iniciar_sesion.winfo_screenwidth()
    hs = ventana_iniciar_sesion.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    ventana_iniciar_sesion.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def loguearse():
        if entry_usuario.get() == "":
            messagebox.showinfo("Faltan Datos","Ingrese Usuario")
            entry_usuario.focus()
            inicio_de_sesion()
            return
        e_u = entry_usuario.get()
        if entry_contraseña.get() == "":
            messagebox.showinfo("Faltan Datos","Ingrese Contraseña")
            entry_contraseña.focus()
            return
        else:
            conexion = pymysql.connect(host="localhost", user="root", passwd="", db="sistemaclientes")
            fcursor = conexion.cursor()

            fcursor.execute("SELECT * FROM inicio_sesion WHERE usuario='"+ usuario.get() +"' and contrasena='"+ contrasena.get()+"'")

            if fcursor.fetchall():
                de_is_m()
            else:
                messagebox.showerror("no se encontro", "no se encontro el usuario")
            conexion.close()
    #------------------------------------------------------imagen
    img_net = Image.open("Imágenes/login.png")
    resized = img_net.resize((100, 100))
    img_net = ImageTk.PhotoImage(resized)
    label_imagen = Label(ventana_iniciar_sesion, image=img_net)
    label_imagen.pack()
    label_imagen.place(x=50,y=7)
    #------------------------------------------------------entrys 
    usuario = StringVar()
    entry_usuario = Entry(ventana_iniciar_sesion, textvariable=usuario)
    entry_usuario.pack()
    entry_usuario.place(x=71,y=100)
    
    contrasena = StringVar()
    entry_contraseña = Entry(ventana_iniciar_sesion, show="*", textvariable=contrasena)
    entry_contraseña.pack()
    entry_contraseña.place(x=71,y=140)
    #------------------------------------------------------botones
    Btn_iniciar_sesion = Button(ventana_iniciar_sesion,text="iniciar sesion", command=loguearse, height= 1, width= 9, bg="#1a2d99", fg="white")
    Btn_iniciar_sesion.pack()
    Btn_iniciar_sesion.place(x=20,y=180)

    Btn_cambiar_ventana2 = Button(ventana_iniciar_sesion,text="Salir", command=de_v2_v1, height= 1, width= 7, bg="red", fg="white")
    Btn_cambiar_ventana2.pack()
    Btn_cambiar_ventana2.place(x=120,y=180)
    #------------------------------------------------------labels
    lbl_usuario = Label(ventana_iniciar_sesion,text="Usuario:")
    lbl_usuario.pack()
    lbl_usuario.place(x=20,y=100)

    lbl_usuario = Label(ventana_iniciar_sesion,text="Contraseña:")
    lbl_usuario.pack()
    lbl_usuario.place(x=2,y=140)
    #------------------------------------------------------mainloop
    mainloop()
#----------------------------------------------------------ventana tres 
def fun_menu():
    global menu
    #------------------------------------------------------ventana
    menu=Tk()
    menu.title("Ventana 3")
    w = 650
    h = 260
    ws = menu.winfo_screenwidth()
    hs = menu.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    menu.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #------------------------------------------------------botones
    Btn_Clientes = Button(menu, text="Clientes", bg="#1a2d99", height=1, width=15, command=de_v3_vc, fg="white")
    Btn_Clientes.pack()
    Btn_Clientes.place(x=10,y=10)

    Btn_Clientes = Button(menu, text="Libros", bg="#1a2d99", height=1, width=15,command=de_v3_vl , fg="white")
    Btn_Clientes.pack()
    Btn_Clientes.place(x=200,y=10)

    Btn_Clientes = Button(menu, text="Alquiler", bg="#1a2d99", height=1, width=15, fg="white")
    Btn_Clientes.pack()
    Btn_Clientes.place(x=400,y=10)

    Btn_Clientes = Button(menu, text="Adminis", bg="#1a2d99", height=1, width=15, fg="white")
    Btn_Clientes.pack()
    Btn_Clientes.place(x=10,y=100)

    Btn_Clientes = Button(menu, text="Salir", bg="#ff0000", command=salir, height=1, width=15, fg="white")
    Btn_Clientes.pack()
    Btn_Clientes.place(x=200,y=100)
    #------------------------------------------------------mainloop
    mainloop()
#----------------------------------------------------------ventana clientes
def fun_ventana_cliente():
    #------------------------------------------------------ventana
    ventana_cliente=Tk()
    ventana_cliente.title("Clientes")
    w = 735
    h = 600
    ws = ventana_cliente.winfo_screenwidth()
    hs = ventana_cliente.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    ventana_cliente.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #------------------------------------------------------definir
    def cancelar():
        global guardar 
        guardar = "nuevo"
        Btn_nuevo.configure(state=NORMAL)
        Btn_modificar.configure(state=NORMAL)
        Btn_eliminar.configure(state=NORMAL)
        Btn_guardar.configure(state=DISABLED)
        Btn_cancelar.configure(state=NORMAL)
        
        entry_apellido.configure(state=DISABLED)
        entry_nombre.configure(state=DISABLED)
        entry_dni.configure(state=DISABLED)
        cmbx_socio.configure(state=DISABLED)

        apellido.set("")
        nombre.set("")
        dni.set("")
        id.set("")
        cmbx_socio.set("seleccione")
        desabilitar_buscar()
    
    def desabilitar_buscar(): 
        global guardar 
        guardar = "sin valor"
        entry_buscar_apellido.configure(state=DISABLED)
        entry_buscar_dni.configure(state=DISABLED)
        cmbx_socio_f.configure(state=DISABLED)

        buscar_apellido.set("")
        buscar_dni.set("")
        cmbx_socio_f.set("seleccione")

    def buscar():
        entry_buscar_apellido.configure(state=NORMAL)
        entry_buscar_dni.configure(state=NORMAL)
        cmbx_socio_f.configure(state=NORMAL)
        cmbx_socio_f.configure(state="readonly")

        Btn_limpiar.configure(state=NORMAL)

    def nuevo():
        global guardar
        guardar = "nuevo"
        print(guardar)
        entry_apellido.configure(state=NORMAL)
        entry_nombre.configure(state=NORMAL)
        entry_dni.configure(state=NORMAL)
        cmbx_socio.configure(state=NORMAL)

        Btn_guardar.configure(state=NORMAL)
        
    def guardar():
        print("funciona")
        global guardar 
        conexion = pymysql.connect(host="localhost", user="root", passwd="", db="sistemaclientes")
        fcursor = conexion.cursor()
        if guardar == "nuevo":
            if entry_apellido.get() == "":
                messagebox.showinfo("Faltan Datos","Ingrese apellido")
                entry_apellido.focus()
                return
            if entry_nombre.get() == "":
                messagebox.showinfo("Faltan Datos","Ingrese nombre")
                entry_nombre.focus()
                return
            if entry_dni.get() == "":
                messagebox.showinfo("Faltan Datos","Ingrese dni")
                entry_dni.focus()
                return
            if cmbx_socio.get() == "seleccione":
                messagebox.showinfo("Faltan Datos","¿usted es socio?")
                return
            sql = "INSERT INTO clientes (apellido, nombre, dni, socio) VALUES ('{0}', '{1}', '{2}', '{3}')".format(apellido.get(), nombre.get(), dni.get(), cmbx_socio.get())
            fcursor.execute(sql)
            conexion.commit()
            conexion.close()
            cargar_grilla()
            messagebox.showinfo("exito", "Cliente Creado exitosamente")
            guardar = "sin valor"

        if guardar == "modificar":
            global id_seleccionado
            sql = "UPDATE clientes SET apellido='{0}', nombre='{1}', dni='{2}', socio='{3}'  WHERE id_cliente = '{4}'".format(apellido.get(), nombre.get(), dni.get(), cmbx_socio.get(), id_seleccionado)
            fcursor.execute(sql)
            conexion.commit()
            cargar_grilla()
            messagebox.showinfo("Modificar", "Registro Modificado")
            id_seleccionado = -1
            cancelar()
            guardar = "sin valor"
        
        if dni_1 != entry_dni.get():
            fcursor.execute("SELECT * FROM clientes WHERE DNI='"+ dni.get()+"'")
            if fcursor.fetchall():
                messagebox.showwarning("Aviso","Usuario Ya Registrado 'Verificar Numero De DNI' 111")
                entry_dni.focus()
            else:
                print(id_seleccionado, " id seleccionado")
                conexion = pymysql.connect(host="localhost", user="root", passwd="", db="sistemaclientes")
                fcursor = conexion.cursor()
                sql= "UPDATE clientes SET apellido='{0}', nombre='{1}', dni='{2}', socio='{3}'  WHERE id_cliente = '{4}'".format(apellido.get(), nombre.get(), dni.get(), cmbx_socio.get(), id_seleccionado)
                fcursor.execute(sql)
                conexion.commit()
                cargar_grilla()
                messagebox.showinfo("Modificar","Registro Modificado!!")
                id_seleccionado = -1
                cancelar()

    def cargar_grilla():
        conexion = pymysql.connect(host="localhost", user="root", passwd="", db="sistemaclientes")
        fcursor = conexion.cursor()
        fcursor.execute("SELECT * FROM clientes")

        for item in grid.get_children():
            grid.delete(item)

        for row in fcursor:
            grid.insert("", 0, text=row[0], values=(row[1], row[2], row[3], row[4]))
        conexion.close()

    def modificar():
        global guardar , id_seleccionado, dni_1
        dni_1 = entry_dni.get()
        guardar = "modificar"
        print(guardar)
        selected = grid.focus()
        id_seleccionado = grid.item(selected, 'text')

        entry_apellido.configure(state=NORMAL)
        entry_nombre.configure(state=NORMAL)
        entry_dni.configure(state=NORMAL)
        cmbx_socio.configure(state=NORMAL)

        Btn_guardar.configure(state=NORMAL)

        if id_seleccionado == '':
            messagebox.showwarning("Modificar", "debe seleccionar un cliente para ser modificado")
            return

        Btn_guardar.configure(stat=NORMAL)

        #nuevo()
        valores = grid.item(selected, 'values')

        apellido2 = valores[0]
        nombre2 = valores[1]
        dni2 = valores[2]
        socio2 = valores[3] 

        id.set(id_seleccionado)
        apellido.set(apellido2)
        nombre.set(nombre2)
        dni.set(dni2)
        cmbx_socio.set(socio2)

    def eliminar():
        selected = grid.focus()
        id_seleccionado = grid.item(selected, 'text')
        print(id_seleccionado)

        if id_seleccionado == "":
            messagebox.showwarning("Eliminar", "¿Deseas eliminar el estudiante seleccionado?")
        else:
            print("SE CUMPLE")
            valores = grid.item(selected, 'values')
            dato = valores[0] + " " + valores[1] + ", DNI: " + valores[2]
            respuesta = messagebox.askquestion("Eliminar","¿desea eliminar el estudiante seleccionado?\n"+  dato)

            if respuesta == messagebox.YES:
                conexion = pymysql.connect(host="localhost", user="root", passwd="", db="sistemaclientes")
                fcursor=conexion.cursor()

                sql= "DELETE FROM clientes WHERE id_cliente = {0}".format(id_seleccionado)
                fcursor.execute(sql)
                conexion.commit()
                cargar_grilla()

    def de_vc_v3():
        ventana_cliente.destroy()
        fun_menu()

    def limpiar():
        buscar_apellido.set("")
        buscar_dni.set("")
        cmbx_socio_f.set("Seleccione")
    #------------------------------------------------------tabla
    grid = ttk.Treeview(ventana_cliente, columns=("col1", "col2", "col3", "col4"))

    grid.column("#0", width=50)
    grid.column("col1", width=140, anchor=CENTER)
    grid.column("col2", width=140, anchor=CENTER)
    grid.column("col3", width=140, anchor=CENTER)
    grid.column("col4", width=140, anchor=CENTER)

    grid.heading("#0", text="ID", anchor=CENTER)
    grid.heading("col1", text="Apellido", anchor=CENTER)
    grid.heading("col2", text="Nombre", anchor=CENTER)
    grid.heading("col3", text="DNI", anchor=CENTER)
    grid.heading("col4", text="Socio", anchor=CENTER)

    grid.pack()
    grid.place(x=10, y=130, width=715, height=350)
    #------------------------------------------------------labelframes 
    labelframe = ttk.LabelFrame(ventana_cliente, width=715, height=80, text="Consultas")
    labelframe.pack()
    labelframe.place(x=10,y=500)

    labelframe = ttk.LabelFrame(ventana_cliente, width=715, height=90)
    labelframe.pack()
    labelframe.place(x=10,y=35)
    #------------------------------------------------------botones
    Btn_nuevo = Button(ventana_cliente, text="Nuevo", height= 1, width= 15, bg="#1a2d99", fg="white", command=nuevo)
    Btn_nuevo.pack()
    Btn_nuevo.place(x=10,y=10)

    Btn_modificar = Button(ventana_cliente, text="Modificar", height= 1, width= 15, bg="#1a2d99", fg="white", command=modificar)
    Btn_modificar.pack()
    Btn_modificar.place(x=130,y=10)

    Btn_eliminar = Button(ventana_cliente, text="Eliminar", height= 1, width= 15, bg="#ff0200", fg="white", command=eliminar)
    Btn_eliminar.pack()
    Btn_eliminar.place(x=250,y=10)

    Btn_guardar = Button(ventana_cliente, text="Guardar", height= 1, width= 15, bg="#5ab507", fg="white", command=guardar)
    Btn_guardar.pack()
    Btn_guardar.place(x=370,y=10)

    Btn_cancelar = Button(ventana_cliente, text="Cancelar", height= 1, width= 15, bg="#ff0200", fg="white", command=cancelar)
    Btn_cancelar.pack()
    Btn_cancelar.place(x=490,y=10)

    Btn_salir = Button(ventana_cliente, text="Salir", height= 1, width= 15, bg="#ff0000", fg="white", command=de_vc_v3)
    Btn_salir.pack()
    Btn_salir.place(x=610,y=10)

    Btn_buscar = Button(ventana_cliente, text="Buscar", height= 1, width= 15, bg="#1a2d99", fg="white", command=buscar)
    Btn_buscar.pack()
    Btn_buscar.place(x=470,y=540)

    Btn_limpiar = Button(ventana_cliente, text="Limpiar", height= 1, width= 15, bg="#1a2d99", fg="white", command=limpiar)
    Btn_limpiar.pack()
    Btn_limpiar.place(x=600,y=540)
    #------------------------------------------------------labels
    lbl_id = Label(ventana_cliente, text="ID")
    lbl_id.pack()
    lbl_id.place(x=40,y=55)

    lbl_apellido = Label(ventana_cliente, text="Apellido")
    lbl_apellido.pack()
    lbl_apellido.place(x=170,y=55)

    lbl_nombre = Label(ventana_cliente, text="Nombre")
    lbl_nombre.pack()
    lbl_nombre.place(x=300,y=55)

    lbl_dni = Label(ventana_cliente, text="DNI")
    lbl_dni.pack()
    lbl_dni.place(x=430,y=55)

    lbl_socio= Label(ventana_cliente, text="Socio")
    lbl_socio.pack()
    lbl_socio.place(x=560,y=55)
    #------------------------------------------------------entys
    id = StringVar()
    entry_id = Entry(ventana_cliente, state=DISABLED, textvariable=id)
    entry_id.pack()
    entry_id.place(x=20,y=75)

    apellido = StringVar()
    entry_apellido = Entry(ventana_cliente, textvariable=apellido)
    entry_apellido.pack()
    entry_apellido.place(x=150,y=75)

    nombre = StringVar()
    entry_nombre = Entry(ventana_cliente, textvariable=nombre)
    entry_nombre.pack()
    entry_nombre.place(x=280,y=75)

    dni = StringVar()
    entry_dni = Entry(ventana_cliente, textvariable=dni)
    entry_dni.pack()
    entry_dni.place(x=410,y=75)
    
    buscar_apellido = StringVar()
    entry_buscar_apellido = Entry(ventana_cliente, textvariable=buscar_apellido)
    entry_buscar_apellido.pack()
    entry_buscar_apellido.place(x=20,y=540)

    buscar_dni = StringVar()
    entry_buscar_dni = Entry(ventana_cliente, textvariable=buscar_dni)
    entry_buscar_dni.pack()
    entry_buscar_dni.place(x=170,y=540)
    #------------------------------------------------------combo box
    socio = ["Si", "No"]
    cmbx_socio = ttk.Combobox(ventana_cliente, value = socio, state = "readonly")
    cmbx_socio.set("Seleccione")
    cmbx_socio.pack()
    cmbx_socio.place(x=540,y=75)

    socio_f = ["Si", "No"]
    cmbx_socio_f = ttk.Combobox(ventana_cliente, value = socio_f, state = "readonly")
    cmbx_socio_f.set("Seleccione")
    cmbx_socio_f.pack()
    cmbx_socio_f.place(x=320,y=540)
    #------------------------------------------------------mainloop
    cancelar()
    cargar_grilla()
    desabilitar_buscar()
    mainloop()
#----------------------------------------------------------ventana libros
def fun_ventana_libros():
    ventana_libros=Tk()
    ventana_libros.title("Libros")
    w = 1000
    h = 600
    ws = ventana_libros.winfo_screenwidth()
    hs = ventana_libros.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    ventana_libros.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def cancelar():
        global guardar 
        guardar = "nuevo"
        Btn_nuevo.configure(state=NORMAL)
        Btn_modificar.configure(state=NORMAL)
        Btn_eliminar.configure(state=NORMAL)
        Btn_guardar.configure(state=DISABLED)
        Btn_cancelar.configure(state=NORMAL)
        
        entry_codigo.configure(state=DISABLED)
        entry_titulo.configure(state=DISABLED)
        entry_autor.configure(state=DISABLED)
        entry_precio.configure(state=DISABLED)
        cmbx_estado.configure(state=DISABLED)
        cmbx_genero.configure(state=DISABLED)

        codigo.set("")
        titulo.set("")
        autor.set("")
        id.set("")
        precio.set("")
        cmbx_estado.set("seleccione")
        cmbx_genero.set("seleccione")
        desabilitar_buscar()
    
    def desabilitar_buscar(): 
        global guardar 
        guardar = "sin valor"
        entry_buscar_codigo.configure(state=DISABLED)
        entry_buscar_titulo.configure(state=DISABLED)
        entry_buscar_autor.configure(state=DISABLED)
        cmbx_genero_f.configure(state=DISABLED)

        buscar_codigo.set("")
        buscar_titulo.set("")
        buscar_autor.set("")
        cmbx_genero_f.set("seleccione")
        cmbx_estado_f.set("seleccione")

    def buscar():
        entry_buscar_codigo.configure(state=NORMAL)
        entry_buscar_titulo.configure(state=NORMAL)
        entry_buscar_autor.configure(state=NORMAL)
        cmbx_genero_f.configure(state=NORMAL)
        cmbx_estado_f.configure(state=NORMAL)

        Btn_limpiar.configure(state=NORMAL)

    def nuevo():
        global guardar
        guardar = "nuevo"
        print(guardar)
        entry_codigo.configure(state=NORMAL)
        entry_titulo.configure(state=NORMAL)
        entry_autor.configure(state=NORMAL)
        entry_precio.configure(state=NORMAL)
        cmbx_genero.configure(state=NORMAL)
        cmbx_estado.configure(state=NORMAL)

        cmbx_genero.configure(state="readonly")
        cmbx_estado.configure(state="readonly")

        Btn_guardar.configure(state=NORMAL)
        
    def guardar():
        print("funciona")
        global guardar 
        conexion = pymysql.connect(host="localhost", user="root", passwd="", db="sistemaclientes")
        fcursor = conexion.cursor()
        if guardar == "nuevo":
            if entry_codigo.get() == "":
                messagebox.showinfo("Faltan Datos","Ingrese apellido")
                entry_codigo.focus()
                return
            if entry_titulo.get() == "":
                messagebox.showinfo("Faltan Datos","Ingrese nombre")
                entry_titulo.focus()
                return
            if entry_autor.get() == "":
                messagebox.showinfo("Faltan Datos","Ingrese dni")
                entry_autor.focus()
                return
            if entry_precio.get() == "":
                messagebox.showinfo("Faltan Datos","Ingrese dni")
                entry_precio.focus()
                return
            if cmbx_genero.get() == "seleccione":
                messagebox.showinfo("Faltan Datos","¿usted es socio?")
                return
            if cmbx_estado.get() == "seleccione":
                messagebox.showinfo("Faltan Datos","¿usted es socio?")
                return
            sql = "INSERT INTO libros (codigo, titulo, autor, genero, precio, estado) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(codigo.get(), titulo.get(), autor.get(), cmbx_genero.get(), precio.get(), cmbx_estado.get())
            fcursor.execute(sql)
            conexion.commit()
            conexion.close()
            cargar_grilla()
            messagebox.showinfo("exito", "Libro Cargado exitosamente")
            guardar = "sin valor"

        if guardar == "modificar":
            global id_seleccionado
            sql = "UPDATE libros SET codigo='{0}', titulo='{1}', autor='{2}', precio='{3}', genero='{4}', estado='{5}'  WHERE id= '{6}'".format(codigo.get(), titulo.get(), autor.get(), precio.get(), cmbx_genero.get(), cmbx_estado.get(), id_seleccionado)
            fcursor.execute(sql)
            conexion.commit()
            cargar_grilla()
            messagebox.showinfo("Modificar", "Registro Modificado")
            id_seleccionado = -1
            cancelar()
            guardar = "sin valor"
        
        if codigo_1 != entry_autor.get():
            fcursor.execute("SELECT * FROM libros WHERE codigo='"+ autor.get()+"'")
            if fcursor.fetchall():
                messagebox.showwarning("Aviso","Usuario Ya Registrado 'Verificar Numero De DNI' 111")
                entry_autor.focus()
            else:
                print(id_seleccionado, " id seleccionado")
                conexion = pymysql.connect(host="localhost", user="root", passwd="", db="sistemaclientes")
                fcursor = conexion.cursor()
                sql= "UPDATE estudiantes SET codigo='{0}', titulo='{1}', autor='{2}', precio='{3}', genero='{4}', estado='{5}'  WHERE id_cliente = '{4}'".format(codigo.get(), titulo.get(), autor.get(), cmbx_genero.get(), cmbx_estado.get(), id_seleccionado)
                fcursor.execute(sql)
                conexion.commit()
                cargar_grilla()
                messagebox.showinfo("Modificar","Registro Modificado!!")
                id_seleccionado = -1
                cancelar()

    def cargar_grilla():
        conexion = pymysql.connect(host="localhost", user="root", passwd="", db="sistemaclientes")
        fcursor = conexion.cursor()
        fcursor.execute("SELECT * FROM libros")

        for item in grid.get_children():
            grid.delete(item)

        for row in fcursor:
            grid.insert("", 0, text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6]))
        conexion.close()

    def modificar():
        global guardar , id_seleccionado, dni_1
        dni_1 = entry_autor.get()
        guardar = "modificar"
        print(guardar)
        selected = grid.focus()
        id_seleccionado = grid.item(selected, 'text')

        entry_codigo.configure(state=NORMAL)
        entry_titulo.configure(state=NORMAL)
        entry_autor.configure(state=NORMAL)
        entry_precio.configure(state=NORMAL)
        cmbx_genero.configure(state=NORMAL)
        cmbx_estado.configure(state=NORMAL)

        Btn_guardar.configure(state=NORMAL)

        if id_seleccionado == '':
            messagebox.showwarning("Modificar", "debe seleccionar un libro para ser modificado")
            return

        Btn_guardar.configure(stat=NORMAL)
        valores = grid.item(selected, 'values')

        codigo2 = valores[0]
        titulo2 = valores[1]
        autor2 = valores[2]
        precio2 = valores[3]
        genero2 = valores[4] 

        id.set(id_seleccionado)
        codigo.set(codigo2)
        titulo.set(titulo2)
        autor.set(autor2)
        precio.set(precio2)
        cmbx_genero.set(genero2)

    def eliminar():
        selected = grid.focus()
        id_seleccionado = grid.item(selected, 'text')
        print(id_seleccionado)

        if id_seleccionado == "":
            messagebox.showwarning("Eliminar", "¿Deseas eliminar el estudiante seleccionado?")
        else:
            print("SE CUMPLE")
            valores = grid.item(selected, 'values')
            dato =", codigo: " + valores[0] + ", titulo: " + valores[1] + ", autor: " + valores[2]
            respuesta = messagebox.askquestion("Eliminar","¿desea eliminar el libro seleccionado?\n"+  dato)

            if respuesta == messagebox.YES:
                conexion = pymysql.connect(host="localhost", user="root", passwd="", db="sistemaclientes")
                fcursor=conexion.cursor()

                sql= "DELETE FROM libros WHERE id = {0}".format(id_seleccionado)
                fcursor.execute(sql)
                conexion.commit()
                cargar_grilla()

    def de_vc_v3():
        ventana_libros.destroy()
        fun_menu()

    def limpiar():
        buscar_codigo.set("")
        buscar_titulo.set("")
        buscar_autor.set("")
        cmbx_genero_f.set("Seleccione")
        cmbx_estado_f.set("Seleccione")

    grid = ttk.Treeview(ventana_libros, columns=("col1", "col2", "col3", "col4", "col5", "col6"))

    grid.column("#0", width=50)
    grid.column("col1", width=140, anchor=CENTER)
    grid.column("col2", width=140, anchor=CENTER)
    grid.column("col3", width=140, anchor=CENTER)
    grid.column("col4", width=140, anchor=CENTER)
    grid.column("col5", width=140, anchor=CENTER)
    grid.column("col6", width=140, anchor=CENTER)

    grid.heading("#0", text="ID", anchor=CENTER)
    grid.heading("col1", text="codigo", anchor=CENTER)
    grid.heading("col2", text="titulo", anchor=CENTER)
    grid.heading("col3", text="autor", anchor=CENTER)
    grid.heading("col4", text="genero", anchor=CENTER)
    grid.heading("col5", text="precio", anchor=CENTER)
    grid.heading("col6", text="estado", anchor=CENTER)

    grid.pack()
    grid.place(x=10, y=130, width=980, height=350)
    #------------------------------------------------------labelframes 
    labelframe = ttk.LabelFrame(ventana_libros, width=980, height=80, text="Consultas")
    labelframe.pack()
    labelframe.place(x=10,y=500)

    labelframe = ttk.LabelFrame(ventana_libros, width=980, height=90)
    labelframe.pack()
    labelframe.place(x=10,y=35)
    #------------------------------------------------------botones
    Btn_nuevo = Button(ventana_libros, text="Nuevo", height= 1, width= 15, bg="#1a2d99", fg="white", command=nuevo)
    Btn_nuevo.pack()
    Btn_nuevo.place(x=10,y=10)

    Btn_modificar = Button(ventana_libros, text="Modificar", height= 1, width= 15, bg="#1a2d99", fg="white", command=modificar)
    Btn_modificar.pack()
    Btn_modificar.place(x=130,y=10)

    Btn_eliminar = Button(ventana_libros, text="Eliminar", height= 1, width= 15, bg="#ff0200", fg="white", command=eliminar)
    Btn_eliminar.pack()
    Btn_eliminar.place(x=250,y=10)

    Btn_guardar = Button(ventana_libros, text="Guardar", height= 1, width= 15, bg="#5ab507", fg="white", command=guardar)
    Btn_guardar.pack()
    Btn_guardar.place(x=370,y=10)

    Btn_cancelar = Button(ventana_libros, text="Cancelar", height= 1, width= 15, bg="#ff0200", fg="white", command=cancelar)
    Btn_cancelar.pack()
    Btn_cancelar.place(x=490,y=10)

    Btn_salir = Button(ventana_libros, text="Salir", height= 1, width= 15, bg="#ff0000", fg="white", command=de_vc_v3)
    Btn_salir.pack()
    Btn_salir.place(x=610,y=10)

    Btn_buscar = Button(ventana_libros, text="Buscar", height= 1, width= 15, bg="#1a2d99", fg="white", command=buscar)
    Btn_buscar.pack()
    Btn_buscar.place(x=750,y=540)

    Btn_limpiar = Button(ventana_libros, text="Limpiar", height= 1, width= 15, bg="#1a2d99", fg="white", command=limpiar)
    Btn_limpiar.pack()
    Btn_limpiar.place(x=870,y=540)
    #------------------------------------------------------labels
    lbl_id = Label(ventana_libros, text="ID")
    lbl_id.pack()
    lbl_id.place(x=40,y=55)

    lbl_codigo = Label(ventana_libros, text="Codigo")
    lbl_codigo.pack()
    lbl_codigo.place(x=170,y=55)

    lbl_titulo = Label(ventana_libros, text="titulo")
    lbl_titulo.pack()
    lbl_titulo.place(x=300,y=55)

    lbl_autor = Label(ventana_libros, text="autor")
    lbl_autor.pack()
    lbl_autor.place(x=430,y=55)

    lbl_precio= Label(ventana_libros, text="precio")
    lbl_precio.pack()
    lbl_precio.place(x=730,y=55)

    lbl_genero= Label(ventana_libros, text="genero")
    lbl_genero.pack()
    lbl_genero.place(x=570,y=55)

    lbl_estado= Label(ventana_libros, text="estado")
    lbl_estado.pack()
    lbl_estado.place(x=850,y=55)

    lbl_codigo_f = Label(ventana_libros, text="Codigo")
    lbl_codigo_f.pack()
    lbl_codigo_f.place(x=40,y=515)

    lbl_titulo = Label(ventana_libros, text="titulo")
    lbl_titulo.pack()
    lbl_titulo.place(x=200,y=515)

    lbl_autor = Label(ventana_libros, text="autor")
    lbl_autor.pack()
    lbl_autor.place(x=350,y=515)

    lbl_genero_f= Label(ventana_libros, text="genero")
    lbl_genero_f.pack()
    lbl_genero_f.place(x=480,y=515)

    lbl_estado_f= Label(ventana_libros, text="estado")
    lbl_estado_f.pack()
    lbl_estado_f.place(x=630,y=515)
    #------------------------------------------------------entys
    id = StringVar()
    entry_id = Entry(ventana_libros, state=DISABLED, textvariable=id)
    entry_id.pack()
    entry_id.place(x=20,y=75)

    codigo = StringVar()
    entry_codigo = Entry(ventana_libros, textvariable=codigo)
    entry_codigo.pack()
    entry_codigo.place(x=150,y=75)

    titulo = StringVar()
    entry_titulo = Entry(ventana_libros, textvariable=titulo)
    entry_titulo.pack()
    entry_titulo.place(x=280,y=75)

    autor = StringVar()
    entry_autor = Entry(ventana_libros, textvariable=autor)
    entry_autor.pack()
    entry_autor.place(x=410,y=75)

    precio = StringVar()
    entry_precio = Entry(ventana_libros, textvariable=precio)
    entry_precio.pack()
    entry_precio.place(x=690,y=75)
    
    buscar_codigo = StringVar()
    entry_buscar_codigo = Entry(ventana_libros, textvariable=buscar_codigo)
    entry_buscar_codigo.pack()
    entry_buscar_codigo.place(x=20,y=540)

    buscar_titulo = StringVar()
    entry_buscar_titulo = Entry(ventana_libros, textvariable=buscar_titulo)
    entry_buscar_titulo.pack()
    entry_buscar_titulo.place(x=170,y=540)

    buscar_autor = StringVar()
    entry_buscar_autor = Entry(ventana_libros, textvariable=buscar_autor)
    entry_buscar_autor.pack()
    entry_buscar_autor.place(x=310,y=540)
    #------------------------------------------------------combo box
    genero = ["accion", "comedia", "drama"]
    cmbx_genero = ttk.Combobox(ventana_libros, value = genero, state = "readonly")
    cmbx_genero.set("Seleccione")
    cmbx_genero.pack()
    cmbx_genero.place(x=540,y=75)

    estado = ["disponible", "baja", "reservado"]
    cmbx_estado = ttk.Combobox(ventana_libros, value = estado, state = "readonly")
    cmbx_estado.set("Seleccione")
    cmbx_estado.pack()
    cmbx_estado.place(x=820,y=75)

    genero_f = ["accion", "comedia", "drama"]
    cmbx_genero_f = ttk.Combobox(ventana_libros, value = genero_f, state = "readonly")
    cmbx_genero_f.set("Seleccione")
    cmbx_genero_f.pack()
    cmbx_genero_f.place(x=450,y=540)

    estado_f = ["disponible", "baja", "reservado"]
    cmbx_estado_f = ttk.Combobox(ventana_libros, value = estado_f, state = "readonly")
    cmbx_estado_f.set("Seleccione")
    cmbx_estado_f.pack()
    cmbx_estado_f.place(x=600,y=540)
    #------------------------------------------------------mainloop
    cancelar()
    cargar_grilla()
    desabilitar_buscar()
    mainloop()
#----------------------------------------------------------crear usuarios
def ventana_registrarse():
    ventana_uno.destroy()
    global ventanasesion
    ventanasesion = Tk()
    #---------------------------------------
    w = 270
    h  = 200
    ws = ventanasesion.winfo_screenwidth()
    hs = ventanasesion.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    ventanasesion.geometry('%dx%d+%d+%d' % (w, h, x, y))
    ventanasesion.title("Inicio")

    def registrar():
        conexion = pymysql.connect(host="localhost", user="root", passwd="", db="sistemaclientes")
        fcursor = conexion.cursor()
        sql = "INSERT INTO inicio_sesion (usuario, contrasena, correo) VALUES ('{0}', '{1}', '{2}')".format(entry_usuario.get(), entry_contrasena.get(), entry_correo.get())
        fcursor.execute(sql)
        conexion.commit()
        conexion.close()
        messagebox.showinfo("exito", "Cuenta Creada exitosamente")

    lbl_nombre = Label(text="Nombre")
    lbl_nombre.pack()
    lbl_nombre.place(x=15, y=10)

    lbl_contraseña = Label(text="Contraseña")
    lbl_contraseña.pack()
    lbl_contraseña.place(x=15, y=50)

    lbl_correo = Label(text="Correo")
    lbl_correo.pack()
    lbl_correo.place(x=15, y=90)

    usuario = StringVar()
    entry_usuario = Entry(ventanasesion, textvariable=usuario)
    entry_usuario.pack()
    entry_usuario.place(x=100, y=10, width=150, height=25)

    contrasena = StringVar()
    entry_contrasena = Entry(ventanasesion, textvariable=contrasena, show="*")
    entry_contrasena.pack()
    entry_contrasena.place(x=100, y=50, width=150, height=25)

    correo = StringVar()
    entry_correo = Entry(ventanasesion, textvariable=correo)
    entry_correo.pack()
    entry_correo.place(x=100, y=90, width=150, height=25)

    btn_crear_usuario = Button(ventanasesion, text="Crear usuario",command=registrar, width=25, height=1, bg="#1a2d99", fg="white")
    btn_crear_usuario.pack
    btn_crear_usuario.place(x=30,y=130)

    btn_salir = Button(ventanasesion, text="Salir",command=de_is_v1, width=20, height=1, bg="#ff0200", fg="white")
    btn_salir.pack
    btn_salir.place(x=45,y=160)
    mainloop()
#----------------------------------------------------------de v3 a vc
def de_v3_vc():
    menu.destroy()
    fun_ventana_cliente()
#----------------------------------------------------------de v3 a vl
def de_v3_vl():
    menu.destroy()
    fun_ventana_libros()
#----------------------------------------------------------faltan datos ventana 2
def de_is_m():
    ventana_iniciar_sesion.destroy()
    fun_menu()
#----------------------------------------------------------de v1 a v2
def de_is_v1():
    ventanasesion.destroy()
    fun_ventana_uno()
#----------------------------------------------------------de v2 a v1
def de_v2_v1():
    ventana_iniciar_sesion.destroy()
    fun_ventana_uno()
#----------------------------------------------------------salir 
def salir():
    menu.destroy()
    fun_iniciar_sesion()
#----------------------------------------------------------llamar funcion 
#fun_ventana_cliente()
fun_ventana_uno()
#fun_menu()
#fun_ventana_libros()