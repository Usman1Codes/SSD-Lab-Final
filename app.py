from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory database
inventory = ["Laptop", "Mouse", "Keyboard"]

@app.route('/')
def home():
    return render_template('index.html', items=inventory)

@app.route('/add', methods=['POST'])
def add_item():
    new_item = request.form.get('item')
    if new_item:
        inventory.append(new_item)
    return redirect(url_for('home'))

@app.route('/remove/<item>')
def remove_item(item):
    if item in inventory:
        inventory.remove(item)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
