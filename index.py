from flask import Flask, render_template, request, Response
from werkzeug.utils import secure_filename
import numpy as np
import cv2
import re
import os
import pytesseract
from PIL import ImageTk, Image

#Asignamos la ruta donde se encuentra el tesseract
pytesseract.pytesseract.tesseract_cmd=r"C://Program Files//Tesseract-OCR//tesseract.exe"
UPLOAD_FOLDER = 'C:/xampp 7.0/htdocs/linea-IA/IA/static'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
video = cv2.VideoCapture(0)

@app.route('/')
def upload_file():
   return render_template('home.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
        f = request.files['file']
        #f.save(secure_filename(f.filename))
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        num=-1
        ruta = "C://xampp 7.0//htdocs//linea-IA//IA//static//"+f.filename
        img = cv2.imread(ruta)
        #ruta2 = ruta[0:-4]+"_2.jpg"
        text = ""
        kernel = np.ones((7,7),np.uint8)
        while(text == ""):
            if(num > 7):
                return render_template("imagen.html", ntext='ERROR NO TEXTO', name='Scanner.jpg', tnum=num)
            num += 1
            erosion = cv2.erode(img,kernel,iterations = num)
            distor = cv2.fastNlMeansDenoisingColored(erosion, None, 10, 10, 7, 15)
            #Aplicamos en texto el cambio de imagen a string con tesseract
            text = pytesseract.image_to_string(distor, lang='spa')
        text = re.sub('[^A-Za-z0-9" "ñÁÉÍÓÚáéíóú,.]+', ' ', text)
        cv2.destroyAllWindows()
        return render_template("imagen.html", ntext=text, name=f.filename, tnum=num)

@app.route('/uploader1', methods = ['GET', 'POST'])
def uploader_cam():
   if request.method == 'POST':
        #f = request.form['fname']+'jpg'
        num=-1
        ruta = "C://xampp 7.0//htdocs//linea-IA//IA//static//Scanner.jpg"
        print(ruta)
        img = cv2.imread(ruta)
        #ruta2 = ruta[0:-4]+"_2.jpg"
        text = ""
        kernel = np.ones((7,7),np.uint8)
        while(text == ""):
            if(num > 7):
                return render_template("imagen.html", ntext='ERROR NO TEXTO', name='Scanner.jpg', tnum=num)
            num += 1
            erosion = cv2.erode(img,kernel,iterations = num)
            distor = cv2.fastNlMeansDenoisingColored(erosion, None, 10, 10, 7, 15)
            #Aplicamos en texto el cambio de imagen a string con tesseract
            text = pytesseract.image_to_string(distor, lang='spa')
        text = re.sub('[^A-Za-z0-9" "ñÁÉÍÓÚáéíóú,.]+', ' ', text)
        cv2.destroyAllWindows()
        return render_template("imagen.html", ntext=text, name='Scanner.jpg', tnum=num)

@app.route('/ref', methods = ['GET', 'POST'])
def image():
    if request.method == 'POST':
        fname = request.form['nm']
        num= int(request.form['nu'])
        ruta = "C://xampp 7.0//htdocs//linea-IA//IA//static//"+fname
        img = cv2.imread(ruta)
        #ruta2 = ruta[0:-4]+"_2.jpg"
        text = ""
        kernel = np.ones((7,7),np.uint8)
        while(text == ""):
            if(num > 7):
                    return "Error"
            num += 1
            erosion = cv2.erode(img,kernel,iterations = num)
            distor = cv2.fastNlMeansDenoisingColored(erosion, None, 10, 10, 7, 15)
            #Aplicamos en texto el cambio de imagen a string con tesseract
            text = pytesseract.image_to_string(distor, lang='spa')
        text = re.sub('[^A-Za-z0-9" "ñÁÉÍÓÚáéíóú,.]+', ' ', text)
        cv2.destroyAllWindows()
        return render_template("imagen.html", ntext=text, name=fname, tnum=num)

@app.route('/takeimage', methods = ['POST'])
def takeimage():
    name = request.form['name']
    print(name)
    _, frame = video.read()
    cv2.imwrite('static/'+f'{name}.jpg', frame)
    cv2.destroyAllWindows()
    return Response(status = 200)


def gen():
    """Video streaming generator function."""
    while True:
        rval, frame = video.read()
        cv2.imwrite('static/capture.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('static/capture.jpg', 'rb').read() + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
   app.run(host='0.0.0.0',
            debug=True,
            port=8080)
