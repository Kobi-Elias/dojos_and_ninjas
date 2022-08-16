from flask_app.__innit__ import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask import render_template, redirect, request


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojo():
    dojo_list = Dojo.get_all()
    return render_template("dojo.html", dojos=dojo_list)

@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    data = {
    "name": request.form["name"]
}
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    dojo= Dojo.ninja_in_dojo(data)
    return render_template("dojo_show.html", dojo = dojo)