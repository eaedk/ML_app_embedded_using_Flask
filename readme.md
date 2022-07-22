# Description
This [repository](https://github.com/eaedk/ML_app_embeded_using_Flask) is a starter code to present to help you to embed your machine learning model into a Flask app.

# Structure
## File: app.py
This file must contain the Flask app. You will define the page endpoints, the logic that will be executed on each page of the Flask app and the html template to use for each endpoint.

## File: utils.py
This file must contain the functions or/and classes you have written to do preprocessing, feature engineering, post-processing, etc. You must copy and paste it into the file and import in functions and classes into the file `app.py` to use it to allow your ml models to work correctly.

## Folder: ml
This folder must contain your ml models objects saved as files, also your transformation pipelines objects saved as files.

## Folder: venv
This file contain the virtual environment, every package you install to build you Flask app will be automatically saved into.

## Folder: templates
This folder must contain the web page templates, the html files. You will define the appearance of the parts of your Flask app using web technologies `(html)`.

## Folder: statics
This folder must contain the static files your templates will loads, like images, templates' css,js, etc.

# How to use this repository
## Import the repo
Clone or download the repo on your local machine.
## Setup the environment
1. Install Python 3 on your system. 
2. Being in the repository, activate the virtual environment : 

this command line will work in linux
```console
source venv/bin/activate
```        

this command line will work in windows
```console
venv\Scripts\activate
```           

## Run the Flask app

```console
python app.py

* Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 616-705-964
```

If there is an error, replace `python3` by `python`.

If everything is ok go to your browser at, http://127.0.0.1:5000 you will see you blank homepage you must design and fill.
You can go to the example page to have a look at a small form doing nothing special: http://127.0.0.1:5000/example .


# Resources
Here are some ressources you would read to have a good understanding of Flask :
- [Getting started with Flask](https://dev.to/nagatodev/getting-started-with-flask-1kn1)
- [Video: Flask tutorial](https://www.youtube.com/watch?v=Kja_28SNIow)