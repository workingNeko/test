import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="mysql.railway.internal",
        user="if0_41832222",
        password="iFuJTZmhdhpEtMnVYyCMRhNpfqGSGhfV",
        database="railway",
        port="3306",
    )