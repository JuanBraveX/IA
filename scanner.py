import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import numpy as np
import cv2
import re
import pytesseract
from PIL import ImageTk, Image

#Asignamos la ruta donde se encuentra el tesseract
pytesseract.pytesseract.tesseract_cmd=r"C://Program Files//Tesseract-OCR//tesseract.exe"

root = tk.Tk()
root.title("Proyecto OCR - Reconocimiento de textos")
root.geometry('900x700+270+10')
root.resizable(False, False)

root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=4)
root.columnconfigure(2, weight=3)

lbl_titulo = ttk.Label(
    root,
    text='Reconocimiento de textos',
    font=("Helvetica", 14))
lbl_titulo.grid(column=1, row=0)

lbl_subt = ttk.Label(
    root,
    text='Aqui se muestra el texto leído:',
    font=("Arial",10),
    wraplength=350)
lbl_subt.grid(column=1, row=1)

lbl_texto = ttk.Label(
    root,
    text='',
    font=("Arial",10),
    wraplength=350)
lbl_texto.grid(column=1, row=2, ipadx=10, ipady=20)

btn_image = ttk.Button(
    root,
    text='Buscar imagen',
    command=lambda: buscar()
)
btn_image.grid(
    column=1, row=3,
    ipadx=2,
    ipady=2
)

btn_itera = ttk.Button(
    root,
    text='Nueva iteración',
    command=lambda: imagen(ruta, iteraciones)
)  


def buscar():
    path = filedialog.askopenfilename(filetypes=[("Image File",'.jpg')])
    imagen(path, -1)

def imagen(path, num):
    global ruta 
    global iteraciones
    ruta = path
    img = cv2.imread(path)
    ruta2 = path[0:-4]+"_2.jpg"
    btn_itera.grid(column=1, row=4, ipadx=2, ipady=2)
    #Lectura de la imagen
    #Un ciclo hasta que el tesseract identifique alguna letra erosionando
    #y distorsionando la imagen
    text = ""
    kernel = np.ones((7,7),np.uint8)
    while(text == ""):
        if(num > 7):
            return print("Error")
        num += 1
        print(num)
        iteraciones = num
        erosion = cv2.erode(img,kernel,iterations = num)
        distor = cv2.fastNlMeansDenoisingColored(erosion, None, 10, 10, 7, 15)
        #Aplicamos en texto el cambio de imagen a string con tesseract
        text = pytesseract.image_to_string(distor, lang='spa') 

    #Asignamos que el texto solo contendra valores significativos 
    #como letras, numeros, simbolos usados, etc
    text = re.sub('[^A-Za-z0-9" "ñÁÉÍÓÚáéíóú,.]+', ' ', text)
    #Cambiamos de tamaño ambas pestañas y las mostramos
    #img = cv2.resize(img, (400,400))
    #cv2.imshow("Imagen original",img)
    #distor = cv2.resize(distor, (400, 400))
    isWritten = cv2.imwrite(ruta2, distor)
    #cv2.imshow("Imagen modificada", distor)
    #cv2.moveWindow("Imagen original", 50, 50)
    #cv2.moveWindow("Imagen modificada", 900, 50)
    #Imprimimos el texto de la imagen
    lbl_texto['text'] = text
    print(text)
    #Presionar algun boton mientras se selecciona alguna imagen para cerrar
    #cv2.waitKey(0)
    cv2.destroyAllWindows()

#No pude meter imagenes xD siguele intentando jaja
#def mostrar(path1, path2):
    #image1 = Image.open(path1)
    #test = ImageTk.PhotoImage(image1)
    #img_origin = ttk.Label(root,border=0, image=test)
    #img_origin.grid(column=1, row=5)
    #image2 = Image.open(ruta2)
    #test2 = ImageTk.PhotoImage(image2)
    #img_mod = ttk.Label(root, image=test)
    #img_mod.grid(column=1, row=5)
print("Fin")
root.mainloop()