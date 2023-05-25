"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


def read_csv():
    data = []
    with open('north_data/customers_data.csv', 'r', encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=',')
        for line in file_reader:
            data.append(line)

    return data


def read_csv_employees():
    data_employees = []
    with open('north_data/employees_data.csv', 'r', encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=',')
        for line in file_reader:
            data_employees.append(line)
    return data_employees


def read_csv_orders():
    data_orders = []
    with open('north_data/orders_data.csv', 'r', encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=',')
        for line in file_reader:
            data_orders.append(line)
    return data_orders


def main():
    conn = psycopg2.connect(host='localhost', database='north', user='alisavorotnikova', password='cxz3t55')
    data = read_csv()
    data_employees = read_csv_employees()
    data_orders = read_csv_orders()
    with conn:
        cursor = conn.cursor()
        for item in data[1:]:
            cursor.execute(
                f"INSERT INTO customers (customer_id, company_name, contact_name) VALUES ('{item[0]}', '{item[1]}', '{item[2]}')")

        for item in data_employees[1:]:
            cursor.execute(
                f"INSERT INTO employees (first_name, last_name, title, birth_date, notes) VALUES ('{item[0]}', '{item[1]}', '{item[2]}', '{item[3]}', '{item[4]}')")

        for item in data_orders[1:]:
            cursor.execute(
                f"INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) VALUES ({int(item[0])}, '{item[1]}', {int(item[2])}, '{item[3]}', '{item[4]}')")


if __name__ == '__main__':
    main()
