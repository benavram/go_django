# go_django
## Synopsis

light template/skeleton for getting setting up a [django](https://docs.djangoproject.com/en/1.8/ "djano docs") project with MySql (or whatever).

## Motivation

setting up projects is pretty boring, this makes it faster provides for some level of consistency across projects and streamlines setup of my prefered django project structure

## Installation

in your terminal run:

``` bash
django-admin.py startproject --template=https://github.com/benavram/go_django/archive/master.zip --extension=py,gitignore project_name
```
## Usage
built for django 1.8

install in a virtualenv from the termnal using the command line above (make sure you change project_name to your project's name)


I like to move the .gitignore and requirements.txt files to the parent directory.  I also create the media and static roots there.
ends up looking something like this (running moveit.py and them ../main.py should do the same thing):

    .
    ├── virtualenv/
       ├── project_name/
            ├── project_name/
                ├── settings/
            ├── app_name/
            ├── static_files/
                ├── media/
                ├── static/
                    ├── css/
                    ├── fonts/
                    ├── img/
                    ├── js/
            ├── templates/
       ├── static/
            ├── media_root/
            ├── static_root/
    .

<<<<<<< HEAD
install requirements if you want - currently limited to django==1.8 and django-debug-toolbar>=1.3.0.  This project setup uses MySql, but I tend install the adapter for that independently because it can be a pain in the ass/platform dependent (or comment MySql and uncomment another db option)
=======
install requirements if you want - currently limited to django==1.8 and django-debug-toolbar>=1.3.0.  This project setup uses MySql, but I tend to set that up independently because it can be a pain in the ass/platform dependent.
>>>>>>> b48d517c2526e0b3cc6bc741d6f1a351010c71fb

``` bash
pip install -r requirements.txt
```

setup your database and run migrations.  You can update/add connection settings in project_name/setttings/cred.py

```bash
python manage.py migrate
```

## Credit
in creating this I took a lot of ideas from the folllowing sources:

https://github.com/codingforentrepreneurs

https://github.com/lincolnloop/django-layout

https://github.com/jcalazan/django-project-template


## License

freely distributable under the terms of the [license](https://github.com/benavram/go_django/blob/master/license.md).
