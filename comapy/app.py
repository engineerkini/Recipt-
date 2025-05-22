from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/receipt', methods=['POST'])
def receipt():
    customer_name = request.form['customer_name']
    parcel_desc = request.form['parcel_desc']
    amount = request.form['amount']
    return render_template('receipt.html', customer_name=customer_name, parcel_desc=parcel_desc, amount=amount)

if __name__ == '__main__':
    app.run(debug=True)
