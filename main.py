import tkinter as tk
from PIL import Image, ImageTk
import pygame as pg

#Variables globales
win_open = None
music_on = False

#Constantes de diseño
WIDTH = 500
HEIGHT = 500
ANI_W = 500
ANI_H = 400
RADIO = 25

ventana = tk.Tk()#Ventana principal

ventana.title("Tkinter_Lab")
ventana.geometry("500x500")
ventana.resizable(False, False)
WIDTH = 500
HEIGHT = 500
#Función de análisis numérico.
def Analisis_num (num):
    if not isinstance (num, int):#Para que el número sea entero
        print("Error, ingrese un número entero.")
        return []
    return Analisis_num_aux(abs(num), 1)#Resuelve el problema de entradas negativas
def Analisis_num_aux (num, divisor):
    if divisor * divisor > num:#Caso base
        return []
    if num % divisor == 0:
        par = (divisor, num // divisor)#Par ordenado a devolver
        return [par] + Analisis_num_aux(num, divisor + 1)#Llamada recursiva
    else:
        return Analisis_num_aux(num, divisor + 1)#Llamada recursiva si no es divisible
    
#Ventana de análisis numérico.
def abrir_analisis_num ():
    global win_open#Llamada a variable global de que no hay ventana abierta
    if  win_open is not None and win_open.winfo_exists():#Revisión de ventana
        win_open.lift()#Tirar ventana hacia delante
        return
    # Creación de primera ventana secundaroa de análisis numérico
    window1 = tk.Toplevel()
    win_open = window1  # Referenciamos la ventana en la variable global para evitar duplicados
    window1.title("Análisis númerico")
    window1.geometry("500x500")
    window1.resizable(False, False)

    # Función para cerrar ventana
    def cerrar_window1():
        global win_open
        win_open = None  # Liberamos la variable global para que se pueda abrir de nuevo después
        window1.destroy() # Destruye el objeto de la ventana de la memoria

    # Canvas
    # Creamos un Canvas para mantener la estética visual del proyecto
    canva2 = tk.Canvas(window1, bg="#B80E0E", width=WIDTH, height=HEIGHT)
    canva2.pack(fill="both", expand=True)

    # Widgets de entrada: Label (instrucción) y Entry (cuadro de texto)
    tk.Label(canva2, text="Ingrese un número entero:").pack(pady=10)
    entrada_text = tk.Entry(canva2)
    entrada_text.pack(pady=5)

    # Label de resultados: Aquí se mostrarán los pares o los errores
    # 'wraplength' permite que el texto largo salte de línea automáticamente
    label_result = tk.Label(canva2, text="Los pares son: ", fg="green", wraplength=350)
    label_result.pack(pady=20)

    # Conexión 
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

    #  Botones de acción
    # 'lambda' para que la función no se ejecute apenas se crea el botón, sino al hacer click
    botonw1 = tk.Button(canva2, text="Calcular pares ordenados", command=lambda: Analisis_connect())
    botonw1.pack(pady=5)

    # Botón para regresar al menú principal llamando a la función de cierre
    botonw1_2 = tk.Button(canva2, text="Volver", command=lambda: cerrar_window1())
    botonw1_2.pack(pady=5)
     
#Ventana de Ficha personal
def ficha_personal ():
    global win_open, music_on#Llamada a variables globales 
    if  win_open is not None and win_open.winfo_exists():#Revisión de ventana
        win_open.lift()#Tirarla hacia adelante
        return
    window2 = tk.Toplevel()#ventana secundaria número 2
    win_open = window2
    window2.title("Ficha personal")
    window2.geometry("700x700")
    window2.resizable(False, False)

    window2.protocol("WM_DELETE_WINDOW", lambda: cerrar_window2())#Para que pare la música si se cierra con X

    pg.mixer.init()
    pg.mixer.music.load("resources/Cancionmp3.mp3")#importación de audio
    def cerrar_window2():
        global win_open, music_on
        win_open = None
        window2.destroy()
        

        pg.mixer.music.stop()  # Detiene la música al cerrar
        music_on = False        # Resetea el estado
        win_open = None
        window2.destroy()   

    canva3 = tk.Canvas(window2, bg="#D69D17", width=700, height=700)
    canva3.pack(fill="both", expand=True)#Para que cubra toda la ventana
    #Etiquetas de la información personal
    tk.Label(canva3, text="MI FICHA PERSONAL", font=("TimesNewRoman", 20, "bold"), bg="#D49D1B").pack(pady=10)
    tk.Label(canva3, text="Nombre: Francisco Li Ruiz", bg="#D69D17", font=("TimesNewRoman", 11)).pack()
    tk.Label(canva3, text="Carné: 2026014113", bg="#D69D17", font=("TimesNewRoman", 11)).pack()
    tk.Label(canva3, text="Edad: 17 años", bg="#D69D17", font=("TimesNewRoman", 11)).pack()
    Biotext="Biografía: Soy estudiante de ingeniería en computadores en el TEC, actualmente vivo en una residencia como a 300 metros de la entrada principal del TEC pero originialmente soy de Barva, Heredia. Me gusta tocar piano, entrenar, disfruto mucho comer de todo y esta es mi primer interfaz gráfica utilizando tkinter."

    lbl_Biotext = tk.Message(canva3, text=Biotext, bg="#D69D17", font=("TimesNewRoman", 11), width=400)

    lbl_Biotext = tk.Message(canva3, text=Biotext, bg="#D69D17", font=("TimesNewRoman", 11), width=400)#Para adaptar el texto a el tamaño deseado

    lbl_Biotext.pack()
    tk.Label(canva3, text="Géneros musicales favoritos: Indie pop, salsa, jazz, piano clásico", bg="#D69D17", font=("TimesNewRoman", 11), width=450).pack()

    #Imagenes pillow

    img_me = Image.open("resources/Me_image.JPEG").resize((170, 170))
    img1 = ImageTk.PhotoImage(img_me)
    label_img1 = tk.Label(canva3, image=img1, bg="#D69D17")
    label_img1.image = img1
    label_img1.place(x=60, y=300)
    tk.Label(canva3, text="Yo", bg="#D69D17", font=("TimesNewRoman", 10, "bold")).place(x=60, y=380)
    img_me = Image.open("resources/Me_image.JPEG").resize((170, 170))#Tamaño de imagen
    img1 = ImageTk.PhotoImage(img_me)
    label_img1 = tk.Label(canva3, image=img1, bg="#D69D17")#Para que aparezca y se vea de acuerdo al fondo del canvas
    label_img1.image = img1#Para que no desaparezca
    label_img1.place(x=60, y=300)#Ubicación de la imágen
    tk.Label(canva3, text="Yo", bg="#D69D17", font=("TimesNewRoman", 10, "bold")).place(x=60, y=380)#Etiqueta que indica de que trata la imágen


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
                pg.mixer.music.load("resources/Cancionmp3.mp3")# Carga el archivo de audio desde la ruta especificada
                pg.mixer.music.play(-1)# Reproduce la música en bucle infinito (-1 = repetir indefinidamente)
                music_on = True# Actualiza el estado de la música a encendida
                music_btn.config(text="Detener", bg="#FF6666")# Cambia el botón para indicar que ahora se puede detener la música
            except:
                print("Error: No se encontró el archivo de audio")
        else:
            pg.mixer.music.stop()# Si la música está sonando, se detiene
            music_on = False#Actualiza estado
            music_btn.config(text="Reproducir", bg="#66FF66")#Botón para que ahora se reproduzca

    music_btn = tk.Button(canva3, text="Reproducir", command=music_control, bg="#66FF66", width=15, cursor="hand2")
    music_btn.place(x=300, y=600)
    tk.Label(canva3,text="Audio de la canción", bg="#D69D17", font=("TimesNewRoman", 10, "bold")).place(x=300, y=570)
    botonw2_1 = tk.Button(canva3,text="Volver", command=lambda: cerrar_window2(), cursor="hand2")
    botonw2_1.place(x=5, y=5)


def abrir_aniwindow():
    global win_open, music_on
    if  win_open is not None and win_open.winfo_exists():
        win_open.lift()
        return
    aniwindow = tk.Toplevel()
    win_open = aniwindow
    aniwindow.title("Animación_de_Esferas")
    aniwindow.geometry(f"{ANI_W}x650") # Dar un poco de espacio a los controles
    aniwindow.resizable(False, False)
    canvas_ani = tk.Canvas(aniwindow, bg="#083E19", width=ANI_W, height=ANI_H)#Canvas utilizando las constantes de animación
    canvas_ani.pack()
    tk.Label(aniwindow, text="Control de  de Velocidad", font=("TimesNewRoman", 12, "bold")).pack(pady=5)#Controlador de velocidad
    val_vel = tk.Scale(aniwindow, from_=1, to=10, orient="horizontal", length=400)#Barra de velociad
    val_vel.set(5) #Asignar valor actual
    val_vel.pack()
    #Función para cerrar la ventana
    def cerrar_aniwindow():
        global win_open
        win_open = None
        aniwindow.destroy()

    btn_volver = tk.Button(aniwindow, text="Volver", command=lambda: cerrar_aniwindow(), cursor="hand2")#Botón para volver a la ventana principal
    btn_volver.pack(pady=10)

    # Creación de  esferas y donde inician
    Es_1 = canvas_ani.create_oval(50, 50, 50 + (RADIO*2), 50 + (RADIO*2), fill="cyan", outline="white")
    # Esfera 2: inicia abajo a la derecha
    Es_2 = canvas_ani.create_oval(ANI_W-100, ANI_H-100, ANI_W-100 + (RADIO*2), ANI_H-100 + (RADIO*2), fill="red", outline="white")
    # Recibe dx y dy de ambas esferas para saber su dirección y velocidad actual
    #Función de rebote
    def animar(dx1, dy1, dx2, dy2): # Recibe dx y dy de ambas esferas para saber su dirección y velocidad actual
        if not aniwindow.winfo_exists():#Verifica si la ventana existe. Si se cerró, detiene la recursión
            return
        # Se divide entre 5 o 4 para evitar que sea muy brusco,(entre menos se divida, más rápido pueden ir)
        v = val_vel.get() / 5
    #Obtener posicion: .coord devuelve una lista [x1, y1, x2, y2]
        # x1, y1 es la esquina superior izquierda; x2, y2 es la inferior derecha del círculo
        c1 = canvas_ani.coords(Es_1)
        c2 = canvas_ani.coords(Es_2)
    #Rebote con paredes esfera 1, solucion para no solo invertir mov
        if c1[0] <= 0:
            dx1 = abs(dx1)    # pared izquierda → empuja hacia la derecha
        if c1[2] >= ANI_W:
            dx1 = -abs(dx1)   # pared derecha → empuja hacia la izquierda
        if c1[1] <= 0:
            dy1 = abs(dy1)    # techo → empuja hacia abajo
        if c1[3] >= ANI_H:
            dy1 = -abs(dy1)   # suelo → empuja hacia arriba
    #Rebote con paredes esfera 2, misma solución para la segunda esfera
        if c2[0] <= 0:
            dx2 = abs(dx2)
        if c2[2] >= ANI_W:
            dx2 = -abs(dx2)
        if c2[1] <= 0:
            dy2 = abs(dy2)
        if c2[3] >= ANI_H:
            dy2 = -abs(dy2)
        #Centro de las esferas
        # (x1 + x2) / 2 es el  centro en X
        # (y1 + y2) / 2 es el centro en Y
        centro1x = (c1[0] + c1[2]) / 2
        centro1y = (c1[1] + c1[3]) / 2
        centro2x = (c2[0] + c2[2]) / 2
        centro2y = (c2[1] + c2[3]) / 2
        #Utilización de Teorema de Pitágoras para hallar al distancia
        # La fórmula es: raíz cuadrada de ( (x2-x1)² + (y2-y1)² )
        dist = ((centro1x - centro2x)**2 + (centro1y - centro2y)**2)**0.5
        # Si la distancia es menor al diámetro (RADIO * 2 = 50), hay colisión
        if dist <= (RADIO * 2):
            # Intercambiamos velocidades: la esfera 1 toma la de la 2 y viceversa
            dx1, dx2 = dx2, dx1
            dy1, dy2 = dy2, dy1
            solapamiento = (RADIO * 2) - dist + 1  # El +1 es para asegurar, es un margen de separación
            
            # Dirección del choque
            # Evitamos división por cero, intentando resolver problema de pared de arriba
            distancia_segura = max(0.1, dist)
            nx = (centro2x - centro1x) / distancia_segura
            ny = (centro2y - centro1y) / distancia_segura

            
            #Separación
            # en dirección opuesta, lo que las despega sin mandarlas fuera
            separacion = solapamiento / 2
            
            canvas_ani.move(Es_1, -nx * separacion, -ny * separacion)
            canvas_ani.move(Es_2, nx * separacion, ny * separacion)
        
    #Movimiento de esferas
    # .move desplaza el objeto la cantidad de píxeles indicada (dx * factor de velocidad)
        canvas_ani.move(Es_1, dx1 * v, dy1 * v)
        canvas_ani.move(Es_2, dx2 * v, dy2 * v)
    #Recursión del movimiento
        # .after espera 20 milisegundos y vuelve a llamar a 'animar'
        # Se pasan los dx y dy actuales (que pudieron cambiar en los IF de arriba)
        aniwindow.after(20, lambda: animar(dx1, dy1, dx2, dy2))
    # Llamada inicial con velocidades distintas para que las esferas no lleven trayectorias idénticas
    animar(6, 4, -4, -6)
   


#Canva y widgets de la ventana principal
canva1 = tk.Canvas(ventana, bg="#209ACA", width=WIDTH, height=HEIGHT)
canva1.pack()

Back_image = Image.open("resources/background.jpg").resize((WIDTH, HEIGHT))
imgB = ImageTk.PhotoImage(Back_image)
label_imgB = tk.Label(canva1, image=imgB, bg="#D69D17")
label_imgB.image = imgB
label_imgB = tk.Label(canva1, image=imgB, width=WIDTH, height=HEIGHT).pack()

labelV1 = tk.Label(ventana, text="Bienvenida a mi interfaz gráfica", font=("TimesNewRoman", 15, "bold"))
labelV1.place(x=100, y=25)

botonV1 = tk.Button(canva1, text="Analisis numérico",  command=lambda: abrir_analisis_num(), cursor="hand2")
botonV1.place(x=300, y=400)

botonV2 = tk.Button(canva1,text="Ficha personal", command=lambda:ficha_personal(),cursor="hand2" )
botonV2.place(x=70, y=400)

botonV3 = tk.Button(canva1,text="Animación", command=lambda:abrir_aniwindow(),cursor="hand2" )
botonV3.place(x=200, y=400)


ventana.mainloop()