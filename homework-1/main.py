"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
from csv import DictReader


def main():
    with psycopg2.connect(host='localhost', database='north', user='roman', password='2901') as conn:
        with conn.cursor() as cur:
            with open('./north_data/employees_data.csv', newline='') as file:
                data = DictReader(file)
                i = 1
                for row in data:
                    cur.execute(f'INSERT INTO employees(first_name, last_name, title, birth_date, notes) '
                                f'VALUES (%s, %s, %s, %s, %s)',
                                (row["first_name"], row["last_name"], row["title"], row["birth_date"], row["notes"]))
                    i += 1
            with open('./north_data/customers_data.csv', newline='') as file:
                data = DictReader(file)
                for row in data:
                    cur.execute(f'INSERT INTO customers VALUES (%s, %s, %s)',
                                (row["customer_id"], row["company_name"], row["contact_name"]))
            with open('./north_data/orders_data.csv', newline='') as file:
                data = DictReader(file)
                for row in data:
                    cur.execute(f'INSERT INTO orders VALUES (%s, %s, %s, %s, %s)',
                                (row["order_id"], row["customer_id"], row["employee_id"], row["order_date"],
                                 row["ship_city"]))


if __name__ == '__main__':
    main()

