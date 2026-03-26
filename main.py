import tkinter as tk
from PIL import Image, ImageTk
import pygame as pg

#Variables globales
win_open = None
music_on = False

#Constantes de diseño
WIDTH = 500
HEIGHT = 500
ANI_W = 800
ANI_H = 500
RADIO = 25

ventana = tk.Tk()#Ventana principal

ventana.title("Tkinter_Lab")
ventana.geometry("500x500")
ventana.resizable(False, False)
WIDTH = 500
HEIGHT = 500
#Función de análisis numérico.
def Analisis_num (num):
    if not isinstance (num, int):
        print("Error, ingrese un número entero.")
        return []
    return Analisis_num_aux(abs(num), 1)
def Analisis_num_aux (num, divisor):
    if divisor * divisor > num:
        return []
    if num % divisor == 0:
        par = (divisor, num // divisor)
        return [par] + Analisis_num_aux(num, divisor + 1)
    else:
        return Analisis_num_aux(num, divisor + 1)
    
#Ventana de análisis numérico.
def abrir_analisis_num ():
    global win_open#Llamada a variable global de que no hay ventana abierta
    if  win_open is not None and win_open.winfo_exists():#Revisión de ventana
        win_open.lift()#Tirar ventana hacia delante
        return
    # 1. CREACIÓN DE LA VENTANA SECUNDARIA (TOPLEVEL)
    window1 = tk.Toplevel()
    win_open = window1  # Referenciamos la ventana en la variable global para evitar duplicados
    window1.title("Análisis númerico")
    window1.geometry("500x500")
    window1.resizable(False, False)

    # 2. FUNCIÓN PARA CERRAR Y LIMPIAR REFERENCIAS
    def cerrar_window1():
        global win_open
        win_open = None  # Liberamos la variable global para que se pueda abrir de nuevo después
        window1.destroy() # Destruye el objeto de la ventana de la memoria

    # 3. INTERFAZ GRÁFICA DENTRO DEL CANVAS
    # Creamos un Canvas para mantener la estética visual del proyecto
    canva2 = tk.Canvas(window1, bg="#F028D2", width=WIDTH, height=HEIGHT)
    canva2.pack(fill="both", expand=True)

    # Widgets de entrada: Label (instrucción) y Entry (cuadro de texto)
    tk.Label(canva2, text="Ingrese un número entero:").pack(pady=10)
    entrada_text = tk.Entry(canva2)
    entrada_text.pack(pady=5)

    # Label de resultados: Aquí se mostrarán los pares o los errores
    # 'wraplength' permite que el texto largo salte de línea automáticamente
    label_result = tk.Label(canva2, text="Los pares son: ", fg="green", wraplength=350)
    label_result.pack(pady=20)

    # 4.CONEXIÓN 
    def Analisis_connect():
        user_text = entrada_text.get()  # Obtenemos lo que el usuario escribió
        
        # Validación de entrada: solo permite números positivos
        if user_text.isdigit():
            valor = int(user_text)
            # Llamamos a la función recursiva 'Analisis_num' definida anteriormente
            resultado = Analisis_num(valor)
            # Actualizamos la UI con el resultado obtenido de la recursión
            label_result.config(text=f"Los pares ordenados son: {resultado}", fg="green")
        else:
            # Manejo de errores visual si el usuario ingresa letras o símbolos
            label_result.config(text="Error, ingrese solo números, y que sean enteros.", fg="red")

    # 5. BOTONES DE ACCIÓN
    # 'lambda' para que la función no se ejecute apenas se crea el botón, sino al hacer click
    botonw1 = tk.Button(canva2, text="Calcular pares ordenados", command=lambda: Analisis_connect())
    botonw1.pack(pady=5)

    # Botón para regresar al menú principal llamando a la función de cierre
    botonw1_2 = tk.Button(canva2, text="Volver", command=lambda: cerrar_window1())
    botonw1_2.pack(pady=5)

    # Mantiene la ventana activa y escuchando eventos (clicks, teclas)
    window1.mainloop()

    
#Ventana de Ficha personal
def ficha_personal():
    # 1. ACCESO A ESTADOS GLOBALES
    # 'win_open' controla si hay ventanas activas y 'music_on' el estado del audio
    global win_open, music_on
    
    # 2. CONTROL DE INSTANCIA (EVITAR DUPLICADOS)
    # Verifica si la variable win_open ya tiene una ventana y si esa ventana aún existe físicamente
    if win_open is not None and win_open.winfo_exists():
        win_open.lift()  # Si ya existe, la trae al frente de la pantalla
        return           # Sale de la función para no crear una segunda ventana igual
    
    # 3. CREACIÓN DE LA VENTANA SECUNDARIA
    window2 = tk.Toplevel()        # Crea una ventana hija de la principal
    win_open = window2             # Guarda esta nueva ventana en la variable global de control
    window2.title("Ficha personal") # Define el título que aparece en la barra superior
    window2.geometry("700x700")   
    window2.resizable(False, False) # Bloquea el cambio de tamaño para no arruinar el diseño
    
    # 4. CONFIGURACIÓN DEL SISTEMA DE AUDIO
    pg.mixer.init()          # Inicializa el módulo de sonido de Pygame
    # Carga el archivo de música 
    pg.mixer.music.load("Cancionmp3.mp3") 
    
    # 5. FUNCIÓN INTERNA DE CIERRE LIMPIO
    def cerrar_window2():
        global win_open
        win_open = None            # Resetea la variable global para permitir abrir ventanas a futuro
        pg.mixer.music.stop()      # Detiene la música inmediatamente para que no siga sonando sola
        window2.destroy()          # Cierra la ventana y libera la memoria RAM
        
    # 6. CREACIÓN DEL CONTENEDOR GRÁFICO (CANVAS)
    # Crea un lienzo de color mostaza (#D69D17) donde se colocarán las fotos y textos
    canva3 = tk.Canvas(window2, bg="#D69D17", width=700, height=700)
    
    # Empaqueta el canvas para que ocupe todo el espacio disponible en la ventana
    canva3.pack(fill="both", expand=True)
    

#Canva y otros widgets de la ventana principal
canva1 = tk.Canvas(ventana, bg="#209ACA", width=WIDTH, height=HEIGHT)
canva1.pack()

Back_image = Image.open("resources/background.jpg").resize((WIDTH, HEIGHT))
imgB = ImageTk.PhotoImage(Back_image)
label_imgB = tk.Label(canva1, image=imgB, bg="#D69D17")
label_imgB.image = imgB
label_imgB = tk.Label(canva1, image=imgB, width=WIDTH, height=HEIGHT).pack()

labelV1 = tk.Label(ventana, text="Bienvenida a mi interfaz gráfica", font=("TimesNewRoman", 15, "bold"))
labelV1.place(x=100, y=25)

botonV1 = tk.Button(canva1, text="Analisis numérico",  command=lambda: abrir_analisis_num())
botonV1.place(x=300, y=400)

botonV2 = tk.Button(canva1,text="Ficha personal", command=lambda:ficha_personal() )
botonV2.place(x=100, y=400)



ventana.mainloop()