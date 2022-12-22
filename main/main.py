from flask import Flask, render_template, request, make_response

from database.base_connect import BaseConnect

bd = BaseConnect()

bd.list('Masters')

app = Flask(__name__)

menu = [{"name": "Каталог", "url": "catalog"},
        {"name": "Корзина", "url": "basket"},
        {"name": "История \n заказов", "url": "products"}]

basket_list = []


@app.route("/")
def root():
    return render_template("root.html", title="Главная", menu=menu)


@app.route("/catalog", methods=['GET', 'POST'])
def catalog():
    if request.method == 'POST':
        id = request.form.get('id')
        if not id is None:
            return render_template("clients.html", title="Каталог", menu=menu, arrEntity=[bd.get_by_id("Clients", id)])
        else:
            entity = request.form.get('add_in_basket')
            basket_list.append(entity)

        print(basket_list)
    return render_template("clients.html", title="Каталог", menu=menu, arrEntity=bd.list("Clients"))


@app.route("/basket", methods=['GET', 'POST'])
def basket():
    if request.method == 'POST':
        id = request.form.get('id')
        if not id is None:
            return render_template("basket.html", title="Корзина", menu=menu, arrEntity=[bd.get_by_id("Clients", id)])
        else:
            entity = request.form.get('add_in_basket')
            basket_list.append(entity)

        print(basket_list)
    return render_template("basket.html", title="Корзина", menu=menu, arrEntity=bd.get_all_by_list_id("Clients", basket_list))


if __name__ == '__main__':
    # get_link_from_json()
    app.run(host='0.0.0.0', port=4556)
