# Deep Learning Model Serving Practice

In this repo, I introduce how to serve a simple deep learning model with flask.  
Datasets and AI models are based on https://github.com/zhongli1990/Covid19-X-Rays.

## Environment

I used a GPU container of https://ide.goorm.io/ to implement my code.    
(I think that someone can implement this code without GPU, but I didn't check it.) 
```
┌───────────────────────────────────────────────┐
                                       _       
     __ _  ___   ___  _ __ _ __ ___   (_) ___  
    / _` |/ _ \ / _ \| '__| '_ ` _ \  | |/ _ \ 
   | (_| | (_) | (_) | |  | | | | | |_| | (_) |
    \__, |\___/ \___/|_|  |_| |_| |_(_)_|\___/ 
    |___/                                      
			     🌩 𝘼𝙣𝙮𝙤𝙣𝙚 𝙘𝙖𝙣 𝙙𝙚𝙫𝙚𝙡𝙤𝙥!
└───────────────────────────────────────────────┘
```

For AI model, tensorflow==2.8.0 is required.  
(Other version may show you an error message when you load my model.)      
Probably, you have to install additional packages like imutils, sklearn for notebook files.  
If you just want to run flask, installing flask is enough.  

```
pip install flask imutils sklearn tensorflow==2.8.0
```

## Run

```py
# First, run flask app. Default port is 5000.
python model_app.py
```

My explanation is for "localhost:5000".  
You can change this address into container URL.

```
// send JSON to flask app
curl -X POST -d@./jsons/serving-image-5.json -H "Content-Type: application/json" localhost:5000/test
```
This command returns a json consist of 'instances' and 'label'.   
Currently, this flask app is working on https://flask-wyrca.run.goorm.io/.
You can test it with json files in this repo.  
(just change localhost:5000/test into https://flask-wyrca.run.goorm.io/test)


## Folders and Files
train/ : 200 train images with three labels 'covid', 'normal', 'pneumonia_bac'  
test/ : 27 test images with three labels 'covid', 'normal', 'pneumonia_bac'

app.py : basic template for flask  
model_app.py : our flask app  

model.ipynb : training our AI model and save it in './model/1/'  
json.ipynb : make json files from 27 test images and save it in './jsons/'  
predict.ipynb : load our AI model in './model/1/' and predict test images obtained from json files  

jsons/ : json files obtained from json.ipynb files  
model/1/ : tensorflow weight files obtained from model.ipynb

## AI model

I used MobileNetV3Large API of tensorflow, and add batch_normalization, flatten, dense layer with 3 outputs.
You can see model.summary() below.

```
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 MobilenetV3large (Functiona  (None, 7, 7, 960)        2996352   
 l)                                                              
                                                                 
 batch_normalization (BatchN  (None, 7, 7, 960)        3840      
 ormalization)                                                   
                                                                 
 flatten (Flatten)           (None, 47040)             0         
                                                                 
 dense (Dense)               (None, 3)                 141123    
                                                                 
=================================================================
Total params: 3,141,315
Trainable params: 143,043
Non-trainable params: 2,998,272
_________________________________________________________________
```

## To do  
I will add nginx, WSGI(gunicorn) later.
