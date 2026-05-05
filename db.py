import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="trolley.proxy.rlwy.net",
        user="root",
        password="iFuJTZmhdhpEtMnVYyCMRhNpfqGSGhfV",
        database="railway",
        port="3306",
    )