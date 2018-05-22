# Final-Senior-Year-Project-
My College Final(Senior) Year Project

# Running the site locally

## Requirments

* [Python 3.6.3](https://python.org)
* [Django 1.8.7](https://www.djangoproject.com/)
* [virtualenv](https://virtualenv.pypa.io/en/stable/) or [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.io)
* Celery
* Ngrok
* Redis

## Installation on Linux

* [Follow the guide here](https://help.github.com/articles/fork-a-repo) on how to clone or fork a repo
* [Follow the guide here](http://simononsoftware.com/virtualenv-tutorial/) on how to create virtualenv

* To create a normal virtualenv (example _myvenv_) and activate it (see Code below).

  ```
  sudo apt-get install python-virtualenv
  
  virtualenv --python=python3.6.3 myvenv
  
  source myvenv/bin/activate

  (myvenv) $ pip install -r requirements.txt

  (myvenv) $ python manage.py makemigrations

  (myvenv) $ python manage.py migrate

  (myvenv) $ python manage.py runserver
  ```
* Copy the IP address provided once your server has completed building the site. (It will say something like >> Serving at 127.0.0.1....).
* Open the address in the browser
* Don't forget to Change ALLOWED_HOSTS = ['127.0.0.1'] in settings.py
* `Note`: It is important that when you create your virtualenv, do not create it in the same folder as the code you downloaded.


## Installation on Windows

* [Follow the guide here](https://help.github.com/articles/fork-a-repo) on how to clone or fork a repo
* [Follow the guide here](http://pymote.readthedocs.io/en/latest/install/windows_virtualenv.html) on how to create virtualenv

* To create a normal virtualenv (example _myvenv_) and activate it (see Code below).

  ```
  1. Create main project folder with name of your choice (eg. Final Year Project) and clone (git clone url) the project into that folder.
   
  2. Open the command prompt and navigate the project folder (Final Year Project)
  
  3. virtualenv finalyearproject-env   # Create a virtual environment for the project with it's own packages.
  
  4. finalyearproject-env\Scripts\activate    # Move into the virtual environment folder and activate the environment.
  
  5. cd ..   # move back into main project folder.
  
  6. cd eshopper    # Move into second (eshopper) folder.
  
  7. pip install -r requirements.txt  # install the requirements.

  8. python manage.py migrate   # Migrate the data into the database.

  9. python manage.py runserver   # Run the server.
  
  NOTE: You can use any text editor or IDE of your choice. 
  ```
* Copy the IP address provided once your server has completed building the site. (It will say something like >> Serving at 127.0.0.1....).
* Open the address in the browser
* Don't forget to Change ALLOWED_HOSTS = ['127.0.0.1'] in settings.py
* `Note`: It is important that when you create your virtualenv, do not create it in the same folder as the code you downloaded.





