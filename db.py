import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="mysql://root:iFuJTZmhdhpEtMnVYyCMRhNpfqGSGhfV@trolley.proxy.rlwy.net:36970/railway",
        user="root",
        password="iFuJTZmhdhpEtMnVYyCMRhNpfqGSGhfV",
        database="railway",
        port="3306",
    )