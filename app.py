import os
import numpy as np  # used for numerical analysis
from flask import Flask, request, render_template
# Flask-It is our framework which we are going to use to run/serve our application.
# request-for accessing file which was uploaded by the user on our application.
# render_template- used for rendering the html pages
from tensorflow.keras.models import load_model  # to load our trained model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)  # our flask app
if not os.path.exists('uploads'):
    os.makedirs('uploads')

model = load_model(r'C:\Users\Hp\Downloads\ECG-Image-Based-Heartbeat-Classification-for-Arrhythmia-Detection-main\ECG-Image-Based-Heartbeat-Classification-for-Arrhythmia-Detection-main\Flask\ECG.h5')

@app.route("/")  # default route
def about():
    return render_template("about.html")  # rendering html page

@app.route("/about")  # default route
def home():
    return render_template("about.html")  # rendering html page

@app.route("/info")  # default route
def information():
    return render_template("info.html")  # rendering html

@app.route("/upload") #default route
def test():
    return render_template("index6.html")#rendering html page


@app.route("/predict",methods=["GET","POST"]) #route for our prediction
def upload():
    if request.method=='POST':
        f=request.files['file'] #requesting the file
        basepath=os.path.dirname('__file__')#storing the file directory
        filepath=os.path.join(basepath,"uploads",f.filename)#storing the file in uploads folder
        f.save(filepath)#saving the file
        
        img=image.load_img(filepath,target_size=(64,64)) #load and reshaping the image
        x=image.img_to_array(img)#converting image to array
        x=np.expand_dims(x,axis=0)#changing the dimensions of the image
        
        pred=model.predict(x)#predicting classes
        y_pred = np.argmax(pred)
        print("prediction",y_pred)#printing the prediction
    
        index=['Left Bundle Branch Block','Normal','Premature Atrial Contraction',
       'Premature Ventricular Contractions', 'Right Bundle Branch Block','Ventricular Fibrillation']
        result=str(index[y_pred])

        return result#resturing the result
    return None

#port = int(os.getenv("PORT"))
if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)#running our app
    #app.run(host='0.0.0.0', port=8000)
            
            