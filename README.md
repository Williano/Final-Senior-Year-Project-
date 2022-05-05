# E-Shopper
A Multi-lingual E-Commerce website built with Django and Python.


## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Features](#features)
* [Technologies](#technologies)
* [Setup](#setup)
* [Status](#status)
* [Contact](#contact)
* [License](#license)
* [Contributing](#contributing)


## General info
A multi-lingual E-Commerce website I built with Python and Django for my final(senior) year project. It supports 10 international languages and has a lot of features a standard online shop needs.

## Screenshots

Home Page
:-------------------------:
![HomePage](https://user-images.githubusercontent.com/19711677/86519243-7a55af00-bdfe-11ea-8a43-a9850710bd82.JPG)


Language Dropdown Page
:-------------------------:
![HomePage language dropdown](https://user-images.githubusercontent.com/19711677/86519338-79714d00-bdff-11ea-8780-a09ec73ef9d4.JPG)


 Shop Owner Dashboard Page
:-------------------------:
![Shop Owner or Manger Page with Google Analytics](https://user-images.githubusercontent.com/19711677/86519242-79bd1880-bdfe-11ea-8681-a613f0e77faf.JPG)


Customer Dashboard Page
:-------------------------:
![customer dashboard](https://user-images.githubusercontent.com/19711677/86519241-79bd1880-bdfe-11ea-946c-27d0adf8745b.JPG)


Live Chat Support           
:-------------------------:
![live chat support](https://user-images.githubusercontent.com/19711677/86519249-7b86dc00-bdfe-11ea-8809-cb1e7c304637.JPG)

 
Product List Page       |  Product Detail Page
:-------------------------:|:-------------------------:
![shop](https://user-images.githubusercontent.com/19711677/86519337-79714d00-bdff-11ea-88a0-4001d8ab386a.JPG) | ![Product Detail Page](https://user-images.githubusercontent.com/19711677/86519245-7aee4580-bdfe-11ea-802f-154ad56b80ff.JPG)

Checkout Page 
:-------------------------:
![Checkout page](https://user-images.githubusercontent.com/19711677/86519248-7b86dc00-bdfe-11ea-9df0-4b1113de6938.JPG)


PayPal Payment Page
:-------------------------:
![Payment Page](https://user-images.githubusercontent.com/19711677/86519247-7b86dc00-bdfe-11ea-81f5-6a32aa760d7d.JPG)

## Features

* Multi-language support (10 international language)
* PayPal payment
* Customer Dashboard
* Owner Dashboard
* Google Analytics
* Product Reviews
* Product Recommendations
* Ad support
* Live Chat Support

## Technologies
* Python 3
* Javascript
* Jquery 
* Django 1.11
* HTML5
* CSS3 
* Bootstrap 4
* Font awesome
* PostgreSQL
* Celery
* Redis
* Ngrok

## Setup

To run this app, you will need to follow these 3 steps:

#### 1. Requirements
  - a Laptop

  - Text Editor or IDE (eg. vscode, PyCharm)

  - [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed on your Laptop.


#### 2. Install Python and Pipenv
  - [Python3](https://www.python.org/downloads/)
  

  - [Pipenv](https://pipenv-es.readthedocs.io/es/stable/)

#### 3. Local Setup and Running on Windows, Linux and Mac OS

  ```
  # Clone this repository into the directory of your choice
  $ git clone https://github.com/Williano/Final-Senior-Year-Project-.git

  # Move into project folder
  $ cd Final-Senior-Year-Project-

  # Install from Pipfile
  $ pipenv install -r requirements.txt 

  # Activate the Pipenv shell
  $ pipenv shell

  # Create database tables
  (Final-Senior-Year-Project-XXXX) $ python manage.py migrate
  
  # Create superuser account
  (Final-Senior-Year-Project-XXXX) $ python manage.py createsuperuser

  # Start server
  (Final-Senior-Year-Project-XXXX) $ python manage.py runserver
  
  # Copy the IP address provided once your server has completed building the site. (It will say something like >> Serving at 127.0.0.1....).
  
  # Open the address in the browser
  >>> http://127.0.0.1:XXXX
  
  
  # Django Admin
  >>> http://127.0.0.1:XXXX/admin/
  ```


## Status
Project is: _done_

## Contact
Created by [Williano](https://williano.github.io/) - feel free to contact me!

## License
>You can check out the full license [here](https://github.com/Williano/Final-Senior-Year-Project-/blob/master/LICENSE.md)

This project is licensed under the terms of the **MIT** license.

## Contributing

1. Fork it (<https://github.com/Williano/Final-Senior-Year-Project-.git>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request


