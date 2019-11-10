## How to build this Django project_004
- `django-admin startproject project_004`
- `cd project_004`
- `python manage.py startapp first_app`
- `cd ..`
- Create **templates** folder
- Create **first_app** folder inside **templates** folder
- Add `TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')` in `settings.py`
- Update `'DIRS': [TEMPLATE_DIR,]` in `settings.py`
