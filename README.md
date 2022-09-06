# Image Gallery build with Django


![Alt text](/photobucket_ss.png?raw=true "/photobucket")


Photo Album sorted by categories

## Setup

- ``` git clone https://github.com/kurekhombre/photobucket.git ```
- Create virtual environment ```python3 -m venv venv``` and activate it
  - Linux/Mac ``` source venv/bin/activate ```
  - Windows ``` venv\Scripts\activate.bat ```
- ``` pip install -r requirements.text ```
- Generate SECRET KEY with 
  - https://djecrety.ir/ or 
  - ``` python manage.py shell ``` 
   ``` >>> from django.core.management.utils import get_random_secret_key``` 
  ``` print(get_random_secret_key) ```
- Create  file '.env' in project folder and paste ``` SECRET_KEY='<your_key>' ```
- ``` python manage.py makemigrations ```
- ``` python manage.py migrate ```
- ``` python manage.py runserver ```


 ENJOY :)
