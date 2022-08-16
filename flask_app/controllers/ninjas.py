from flask_app.__innit__ import app
from flask import render_template, request, redirect 
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def new_ninja():
    ninja = Ninja.get_all()
    dojos = Dojo.get_all()
    return render_template('new_ninja.html', ninja=ninja, dojos=dojos)

@app.route('/create/ninja', methods=["POST"])
def create_ninja():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    Ninja.save(data)
    return redirect("/dojos")