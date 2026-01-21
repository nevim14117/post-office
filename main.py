from flask import Flask, render_template, request
from flask import jsom
from flask import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Here you would handle the form submission
    sender_name = request.form.get('sender_name')
    sender_address = request.form.get('sender_address')
    sender_postal_code = request.form.get('sender_postal_code')
    recipient_name = request.form.get('recipient_name') 
    recipient_address = request.form.get('recipient_address')  
    recipient_postal_code = request.form.get('recipient_postal_code')
    package_weight = request.form.get('package_weight')
    package_dimensions = request.form.get('package_dimensions')
    delivery_type = request.form.get('delivery_type') 

if __name__ == '__main__':
    app.run(debug=True)
