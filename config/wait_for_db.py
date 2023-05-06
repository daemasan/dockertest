import os
import MySQLdb
from time import sleep
from pathlib import Path



from settings import env
print(env("DB_NAME"))
count_to_try = 0
LIMIT_OF_COUNT = 20 # 値は必要に応じて調整


def check_connection(count, limit):
    """
    docker-compose up実行時用、時間調整のための関数。
    """
    try:
        conn = MySQLdb.connect(
            unix_socket = "/var/run/mysqld/mysqld.sock",
            user=env("DB_USER"),
            passwd=env("DB_PASSWORD"),
            host="db",
            port=3306,
            db=env("DB_NAME"),
        )
    except MySQLdb._exceptions.OperationalError as e:
        count += 1
        print("Waiting for MySQL... (", count, "/ 20 )")
        sleep(3)
        if count < limit:
            check_connection(count, limit)
        else:
            print(e)
            print("Failed to connect mySQL.")
    else:
        print("Connected!\n")
        conn.close()
        exit()


if __name__ == "__main__":
    check_connection(count_to_try, LIMIT_OF_COUNT)