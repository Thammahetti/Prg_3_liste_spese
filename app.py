from flask import Flask, render_template,request,redirect,url_for
lista_spese = []
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html' , lista_spese = lista_spese) 

@app.route('/add', methods=['POST'])
def add():
    product = request.form['product']
    if product:
        lista_spese.append(product)
    return redirect(url_for('home'))
@app.route('/remove/<int:indice>', methods=['POST'])
def remove(indice):
    if 0 <= indice < len(lista_spese):
        lista_spese.pop(indice)

    return redirect(url_for('home'))
@app.route('/delete', methods=['POST'])
def delete():
    lista_spese.clear()

    return redirect(url_for('home'))

    


if __name__ == '__main__':
    app.run(debug=True)