
## Web Scrapping (Laptops et Smartphones)
Cette application Django permet de gérer et d'afficher une liste de laptops et de smartphones. Elle inclut des fonctionnalités de pagination, des modèles de données structurés, et des templates pour afficher les produits.

<br />

## Fonctionnalités

* Liste des Laptops : Affiche une liste paginée des laptops avec leurs caractéristiques.
* Liste des Smartphones : Affiche une liste des smartphones avec leurs détails.
* Modèles de Données : Utilise des modèles Django pour stocker les informations sur les laptops et les smartphones.
* Templates : Des templates HTML pour afficher les données de manière structurée.

<br />

## Installation : 

```bash
$ # Get the code
$ git clone https://github.com/McOP81/web-scrapping.git
$ cd web-scrapping
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules - SQLite Storage
$ pip install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```

<br />

## Structure du Projet

* apps/home/views.py : Contient les vues pour afficher les laptops et les smartphones.
* apps/home/models.py : Définit les modèles Laptop et Smartphone.
* apps/templates/home/ : Contient les templates HTML pour l'affichage des produits.
* scrap/ : Contient des fichiers JSON pour charger des données de test.

<br />