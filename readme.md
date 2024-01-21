Project 'StudyApp'
Based on training program PYSTACK WEEK 9.0 by Caio Sampaio

January 2024
--

Initial Setup

    Python Version 3.12.1

#1 Create new Virtual Env
   
    py -m venv venv

#2 Activate it

    venv\Scripts\Activate

#2.1 In case of permission issues, run this: 
     
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

3# Install django and pillow

    pip install django==5.0.1
    pip install pillow==10.2.0

4# Subir o DB

    py manage.py makemigrations
    py manage.py migrate

#5 Subir a aplicação local

    python manage.py runserver
