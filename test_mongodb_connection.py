# test_mongodb_connection.py
from djongo import connection

try:
    connection.connect()
    print("Connexion à MongoDB réussie !")
except Exception as e:
    print(f"Erreur de connexion à MongoDB : {e}")