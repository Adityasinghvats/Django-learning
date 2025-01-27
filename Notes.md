## Installation 
- As we are using uv for virtua env use uv pip install `<name>`.
- `django-admin startproject <name>` - first time.
- each main project has a sub folder with same name.
- cd into main folder then `python manage.py runserver`.
- everything is a small app here.
- url visited by user-> django url resolver -> urls.py -> views.py (logic part)-> via Model.py get DB access send response.
- views can use templates.