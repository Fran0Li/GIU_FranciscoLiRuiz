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
    global win_open
    if  win_open is not None and win_open.winfo_exists():
        win_open.lift()
        return
    window1 = tk.Toplevel()
    win_open = window1
    window1.title("Análisis númerico")
    window1.geometry("500x500")
    window1.resizable(False, False)
   

ventana.mainloop()