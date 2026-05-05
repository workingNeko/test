import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="sql104.infinityfree.com",
        user="if0_41832222",
        password="gMigMPGxOV7",
        database="if0_41832222_XXX"
    )