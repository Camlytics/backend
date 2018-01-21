import json

from flask import Flask
from dateutil.parser import parse

app = Flask(__name__)


@app.route("/api/customers")
def customers():
    with open('customers.txt', 'r') as f:
        customer_records = [line[:-1] if '\n' in line else line for line in f.readlines()]
        customer_arrays = [customer_record.split('  ') for customer_record in customer_records]
        return json.dumps(
            [{'profile': customer_array[0], 'item_count': customer_array[1], 'updated_at': customer_array[2]}
             for customer_array in customer_arrays])


@app.route("/api/customers/count")
def current_customers_count():
    with open('state.txt', 'r') as f:
        record = f.read()[:-1]
        data_array = record.split('  ')
        print(record)
        return json.dumps({
            'count': data_array[0],
            'datetime': data_array[1]
        })


@app.route("/api/products")
def products():
    with open('products.txt', 'r') as f:
        products = [line[:-1] if '\n' in line else line for line in f.readlines()]
        return json.dumps(products)


@app.route("/api/customers/counts")
def customers_counts():
    counts = [0 for i in range(0, 23)]
    with open('records.txt', 'r') as f:
        records = [line[:-1] if '\n' in line else line for line in f.readlines()]
        for record in records:
            record_arr = record.split('  ')
            hour = parse(record_arr[1]).hour
            counts[hour] += 1
    return json.dumps(counts)
