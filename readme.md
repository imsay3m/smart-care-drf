1. creating virtual environment
    - <code>python -m venv virtualEnvironmentName</code> 
    <br>
    <b>Note</b>: <i>Go to desired directory first</i>

2. change directory to virtualenvironment
    - after creating virtual environment change directory to virtualEnvironmentName
    - <code>cd virtualEnvironmentName/</code>

3. activating virtual environment
    - <code>source Scripts/activate</code>

4. check pip package list
    - <code>pip list</code>

5. version check django and install django
    - <code>django-admin --version</code>
    - <code>pip install django</code>
    - <code>django-admin --version</code>

6. create a project
    - <code>django-admin startproject projectName</code>

7. change directory to projectName
    - after creating django project change directory to projectName
    - <code>cd projectName/</code>

8. start the server
    - <code>python manage.py runserver</code>

9. create an app
    - <code>django-admin startapp appName</code>

10. for import problem
    - Type <code>pip show Django</code> in terminal
    - Go to the path of intallation mentioned there
    - It will be inside "lib" by default..go back to scripts
    - Inside the scripts , there will be python.exe app
    - Choose this as your interpreter

11. crispy forms installation
    - <code>pip install crispy-bootstrap5</code>
    - <code>INSTALLED_APPS =<br>
    (
        <br>
                                ...
        <br>
                                "crispy_forms",
        <br>
                                "crispy_bootstrap5",
        <br>
                                ...
        <br>
    )
        </code>
    - <code>CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"<br>
    CRISPY_TEMPLATE_PACK = "bootstrap5"</code>
    - Installed Packages <code>pip freeze > requirements.txt</code>
    - add gitignore file
    

12. Create migrations
    - <code>python manage.py makemigrations</code>

13. Run migration
    - <code>python manage.py migrate</code>

14. Create superuser for authenficiation/admin panel
    - <code>python manage.py createsuperuser</code>

15. psycopg2 installation for PostgreSql
    - <code>pip install psycopg2</code>
    - <code>DATABASES = {<br>
        'default': {<br>
            'ENGINE': 'django.db.backends.postgresql_psycopg2',<br>
            'NAME': 'your_db_name',<br>
            'USER': 'postgres',<br>
            'PASSWORD': 'your_db_password',<br>
            'HOST': 'localhost',<br>
            'PORT': '5432',<br>
            }<br>
        }<br>
    </code>

16. django-environ package installation
    - <code>pip install django-environ</code>
    - <code>
        import environ<br>
        env = environ.Env()<br>
        environ.Env.read_env()<br>
        ...<br>
        # Your secret key<br>
        SECRET_KEY = env("SECRET_KEY")<br>
        ...<br>
        DATABASES = {<br>
            'default': {<br>
                'ENGINE': 'django.db.backends.postgresql_psycopg2',<br>
                'NAME': env("DB_NAME"),<br>
                'USER': env("DB_USER"),<br>
                'PASSWORD': env("DB_PASSWORD"),<br>
                'HOST': env("DB_HOST"),<br>
                'PORT': env("DB_PORT"),<br>
            }<br>
        }<br>
        </code>

17. Django Media Files
    - settings.py<br>
    <code>MEDIA_URL='/media/'<br>
    MEDIA_ROOT = BASE_DIR /'media'</code>

    - urls.py<br>
    <code>from django.conf import settings<br>
    from django.conf.urls.static import static<br>urlpatterns += static(settings.MEDIA_URL, document_root)</code>


18. Django Rest Framework
    - Installations<br>
        <code>pip install djangorestframework<br>
        pip install markdown<br>
        pip install django-filter</code>
    - In Settings.py<br>
    Add `'rest_framework'` to your `INSTALLED_APPS`.<br>


19. Rest Framework Token Model & Django Filter Backend
    - In Settings.py<br>
    Add `'rest_framework.authtoken'` to your `INSTALLED_APPS`.
    - Django Filter Installation<br>
    <code>pip install django-filter</code>
    - In Settings.py<br>
    Add `'django_filters',` to your `INSTALLED_APPS`.

20. 
    - Installed Packages <code>pip freeze > requirements.txt</code>