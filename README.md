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

Probably, you have to install additional packages like imutils, sklearn for notebook files.  
If you just want to run flask, installing flask is enough.

```
pip install flask imutils sklearn
```

## Run

```py
# First, run flask app. Default port is 5000.
python model_app.py
```

My explanation is for "localhost:5000".
You can change this address into container URL like https://xxxx.run-asia-northeast1.goorm.io.

```
# send JSON to flask app
curl -X post -d@./jsons/serving-image-5.json -H 'Content-Type: application/json' localhost:5000/test
```

## To do
I will add nginx, WSGI(gunicorn) later.
