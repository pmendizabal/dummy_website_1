from flask import Blueprint, render_template

views = Blueprint(__name__, "home")

@views.route("/home/")
def home():
    return render_template("index.html")

@views.route("/cadenas/")
def cadena_valor():
    return render_template("cadenas.html")

@views.route("/capacitacion/")
def capacitacion():
    return render_template("capacitacion.html")

@views.route("/financiamiento/")
def financiamiento():
    return render_template("fin.html")

@views.route("/tesoreria/")
def tesoreria():
    return render_template("teso.html")