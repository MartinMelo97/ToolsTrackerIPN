# Instrucciones

1. Crea un entorno virtual y actívalo
2. Ubícate en el root del proyecto (donde se encuentra este archivo y el `manage.py`)
3. Ejecuta `pip install -r requirements.txt`
4. Crea un superusuario para que puedas acceder al administrador de Django `python manage.py createsuperuser`
5. Ejecuta `python manage.py runserver`
6. En el navegador entra a `http://localhost:8000/account`

## ERRORES CON LA BASE DE DATOS
1. Elimina el archivo `db.sqlite3`
2. Corre `python manage.py migrate`
3. Crea nuevamente un superusuario
4. Corre el servidor