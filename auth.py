from db import get_connection

def register_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        conn.commit()
        return True
    except:
        return False

    finally:
        cursor.close()
        conn.close()


def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user