I will use this README to keep track of the stages along the development.

-> I forgot to add this track at the beginning of the development. 
However I will add what I can up to this stage.

1) I've learned a few key things to create a Django application. 
See as follows: 
    a) Use the following steps to create a Django project:
        1) Create a virtual environment:
            a) python -m venv myworld
                . This will set up a venv and create a folder named "myword" with subfolders and files.
        2) Activate virtual environment:
            a) source myworld/bin/activate
        3) Install django:
            a) python -m pip install Django
        4) Create a django project:
            a) django-admin startproject my_log_app
                . This command create a django application. Django creates a my_log_app folder on my computer with subfolder and files.
        5) Use the following command to run the project:
            a) python manager.py runserver
                . Open a new window browser and type the IP address

    b) Modify your application in with the following steps to reach what you need:
        1) Inside the my_log_app there will be the necessary structure 
        to make you application work. 
        2) Let's start from views.py:
            a) Inside views.py will have to import HttpResponse and declare 
            a function to send Http request:
                1) from django.http import HttpResponse
                2) def my_log_app(request): return HttpResponse("Hello world")
