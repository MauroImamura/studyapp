# StudyApp

Based on training program PYSTACK WEEK 9.0 by Caio Sampaio
<p align="end">Janeiro de 2024</p>

This application provides a study platform where users can create sets of flashcards to test their knowledge. With the flashcards, it is possible to create challenges and generate reports that indicate students' performance in each subject. 
Furthermore, there is a section for submitting and sharing materials, allowing users to access them from anywhere.

<img src="https://github.com/MauroImamura/images/blob/main/StudyApp.jpg"/>

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

4# Create DB

    py manage.py makemigrations
    py manage.py migrate

#5 Run locally

    python manage.py runserver
