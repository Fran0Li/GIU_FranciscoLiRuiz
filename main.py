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
     
#Ventana de Ficha personal
def ficha_personal ():
    global win_open, music_on
    if  win_open is not None and win_open.winfo_exists():
        win_open.lift()
        return
    window2 = tk.Toplevel()
    win_open = window2
    window2.title("Ficha personal")
    window2.geometry("700x700")
    window2.resizable(False, False)
    pg.mixer.init()
    pg.mixer.music.load("resources/Cancionmp3.mp3")
    def cerrar_window2():
        global win_open
        win_open = None
        window2.destroy()
    canva3 = tk.Canvas(window2, bg="#D69D17", width=700, height=700)
    canva3.pack(fill="both", expand=True)
    tk.Label(canva3, text="MI FICHA PERSONAL", font=("TimesNewRoman", 20, "bold"), bg="#D49D1B").pack(pady=10)
    tk.Label(canva3, text="Nombre: Francisco Li Ruiz", bg="#D69D17", font=("TimesNewRoman", 11)).pack()
    tk.Label(canva3, text="Carné: 2026014113", bg="#D69D17", font=("TimesNewRoman", 11)).pack()
    tk.Label(canva3, text="Edad: 17 años", bg="#D69D17", font=("TimesNewRoman", 11)).pack()
    Biotext="Biografía: Soy estudiante de ingeniería en computadores en el TEC, actualmente vivo en una residencia como a 300 metros de la entrada principal del TEC pero originialmente soy de Barva, Heredia. Me gusta tocar piano, entrenar, disfruto mucho comer de todo y esta es mi primer interfaz gráfica utilizando tkinter."
    lbl_Biotext = tk.Message(canva3, text=Biotext, bg="#D69D17", font=("TimesNewRoman", 11), width=400)
    lbl_Biotext.pack()
    tk.Label(canva3, text="Géneros musicales favoritos: Indie pop, salsa, jazz, piano clásico", bg="#D69D17", font=("TimesNewRoman", 11), width=450).pack()

    #Imagenes pillow
    img_me = Image.open("resources/Me_image.JPEG").resize((170, 170))
    img1 = ImageTk.PhotoImage(img_me)
    label_img1 = tk.Label(canva3, image=img1, bg="#D69D17")
    label_img1.image = img1
    label_img1.place(x=60, y=300)
    tk.Label(canva3, text="Yo", bg="#D69D17", font=("TimesNewRoman", 10, "bold")).place(x=60, y=380)

    img_lugar = Image.open("resources/Place_image.JPEG").resize((170, 170))
    img2 = ImageTk.PhotoImage(img_lugar)
    label_img2 = tk.Label(canva3, image=img2, bg="#D69D17")
    label_img2.image = img2
    label_img2.place(x=60, y=500) 
    tk.Label(canva3, text="Donde Vivo", bg="#D69D17", font=("TimesNewRoman", 10, "bold")).place(x=60, y=600)

    img_hobby = Image.open("resources/Hobby_img.JPG").resize((170, 170))
    img3 = ImageTk.PhotoImage(img_hobby)
    label_img3 = tk.Label(canva3, image=img3, bg="#D69D17")
    label_img3.image = img3
    label_img3.place(x=500, y=300) 
    tk.Label(canva3, text="Mi hobby", bg="#D69D17", font=("TimesNewRoman", 10, "bold")).place(x=500, y=380)

    img_artist = Image.open("resources/Artist_image.JPG").resize((170, 170))
    img4 = ImageTk.PhotoImage(img_artist)
    label_img4 = tk.Label(canva3, image=img4, bg="#D69D17")
    label_img4.image = img4
    label_img4.place(x=500, y=500) 
    tk.Label(canva3, text="Artista favorito", bg="#D69D17", font=("TimesNewRoman", 10, "bold")).place(x=500, y=600)
    def music_control():
        global music_on
        if music_on == False:
            try:
                pg.mixer.music.load("resources/Cancionmp3.mp3")
                pg.mixer.music.play(-1)
                music_on = True
                music_btn.config(text="Detener", bg="#FF6666")
            except:
                print("Error: No se encontró el archivo de audio")
        else:
            pg.mixer.music.stop()
            music_on = False
            music_btn.config(text="Reproducir", bg="#66FF66")
    music_btn = tk.Button(canva3, text="Reproducir", command=music_control, bg="#66FF66", width=15)
    music_btn.place(x=300, y=600)
    tk.Label(canva3,text="Audio de la canción", bg="#D69D17", font=("TimesNewRoman", 10, "bold")).place(x=300, y=570)
    botonw2_1 = tk.Button(canva3,text="Volver", command=lambda: cerrar_window2())
    botonw2_1.place(x=5, y=5)




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