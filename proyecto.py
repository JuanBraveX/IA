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
root.geometry('1100x600+150+10')
root.resizable(False, False)

root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=4)
root.columnconfigure(2, weight=3)

lbl_titulo = ttk.Label(
    root,
    text='Reconocimiento de textos',
    font=("Helvetica", 14))
lbl_titulo.grid(column=1, row=1)

lbl_subt = ttk.Label(
    root,
    text='Aqui se muestra el texto leído:',
    font=("Arial",10),
    wraplength=350)
lbl_subt.grid(column=1, row=2)

lbl_texto = ttk.Label(
    root,
    text='',
    borderwidth=1, relief="solid",
    font=("Arial",10),
    wraplength=350)
lbl_texto.grid(column=1, row=3, ipadx=10, ipady=20)

btn_image = ttk.Button(
    root,
    text='Buscar imagen',
    command=lambda: buscar()
)
btn_image.grid(
    column=1, row=4,
    ipadx=2,
    ipady=2
)

btn_camara = ttk.Button(
    root,
    text='Camara',
    command=lambda: camara()
)
btn_camara.grid(
    column=1, row=5,
    ipadx=2,
    ipady=2
)

btn_itera = ttk.Button(
    root,
    text='Nueva iteración',
    command=lambda: imagen(ruta, iteraciones)
)  

img_origin = ttk.Label(
    root
)

img_mod = ttk.Label(
    root
)

lbl_origin = ttk.Label(
    root,
    text="Imagen Original"
)

lbl_mod = ttk.Label(
    root
)

def camara():
    cap = cv2.VideoCapture(1)  #it can be one also...but generally zero
    while(True):
    # Capture frame-by-frame
        ret, frame = cap.read()
        frame = cv2.resize(frame, (600,400))
        cv2.imshow('Capture', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    path = 'A:/Ing en Sistemas Comp/9no Semestre/Inteligencia Artificial/IA/ProyectoOCR/foto_camara.jpg'
    cv2.imwrite(path, frame)
    cap.release()
    cv2.destroyAllWindows()
    imagen(path, -1)

def buscar():
    path = filedialog.askopenfilename(filetypes=[("Image File",'.jpg')])
    imagen(path, -1)

def imagen(path, num):
    global ruta 
    global iteraciones
    ruta = path
    image1 = Image.open(path).resize((400, 300))
    global test
    test = ImageTk.PhotoImage(image1)
    img_origin['image']=test
    img_origin.grid(column=0, row=3, padx=2, pady=3)
    img = cv2.imread(path)
    ruta2 = ruta[0:-4]+"_2.jpg"
    btn_itera.grid(column=1, row=6, ipadx=2, ipady=2)
    #Un ciclo hasta que el tesseract identifique alguna letra erosionando
    #y distorsionando la imagen
    text = ""
    kernel = np.ones((5,6),np.uint8)
    while(text == ""):
        if(num > 7):
            lbl_texto['text'] = "No pudo identificar ninguna letra o numero, o se hicieron demasiadas iteraciones"
            iteraciones=-1
            return print("Demasiadas iteraciones")
        num += 1
        print(num)
        iteraciones = num
        erosion = cv2.erode(img,kernel,iterations = num)
        distor = cv2.fastNlMeansDenoisingColored(erosion, None, 10, 10, 7, 15)
        #Aplicamos en texto el cambio de imagen a string con tesseract
        text = pytesseract.image_to_string(distor, lang='spa') 

    #Asignamos que el texto solo contendra valores significativos 
    #como letras, numeros, simbolos usados, etc
    text = re.sub('[^A-Za-z0-9" "ñÁÉÍÓÚáéíóú,.\n]+', ' ', text)
    isWritten = cv2.imwrite(ruta2, distor)
    image2 = Image.open(ruta2).resize((400, 300))
    global test2
    test2 = ImageTk.PhotoImage(image2)
    img_mod['image']=test2
    img_mod.grid(column=2, row=3, padx=2, pady=3)
    lbl_texto['text'] = text
    print(text)
    #Mostramos los label que indican el numero de iteraciones
    lbl_origin.grid(column=0, row=4, ipadx=2, ipady=3)
    lbl_mod['text']="Imagen modificada (Iter="+str(iteraciones)+")"
    lbl_mod.grid(column=2, row=4, ipadx=2, ipady=3)
    cv2.destroyAllWindows()
print("Fin")
root.mainloop()
