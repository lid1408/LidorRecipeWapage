
from DataAccess import DAL
from DataAccess import Insertfunc
from DataAccess import stackdata
from flask import Flask, jsonify, render_template, url_for, request, redirect
import psycopg2 , random, json
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
@app.route("/lid")
def server():
    return ("lidor")

y = DAL() 
@app.route("/cakes")
def index():
    return jsonify(y)

@app.route("/process_cart", methods = ["POST", "GET"])
def process_cart():
    if request.method == "POST":
        user =(str(request.form["id"]), str(request.form["fullname"]), str(request.form["Email"]), str(request.form["Country"]), str(request.form["City"]), str(request.form["Street"]), str(request.form["ccnum"]), str(request.form["EM"]), str(request.form["EY"]) ,str(request.form["cvv"]), str(request.form["AMOUNT"]), str(request.form["price"]) ,str(request.form["productNAME"]))
        amountToUpdate = request.form["NewStack"]
        InStack = request.form["INStack"]
        instack = request.form["RightStack"]
        Insertfunc(user,amountToUpdate,InStack,instack)
        return redirect("http://127.0.0.1:5500/server/templates/checkoutpage.html" ,code=302)
    else:
        return render_template("cartry.html")

@app.route("/<usr>")
def user(usr):
    return f"<p> {usr} </p>"


@app.route("/MyStack")
def stack():
    data=stackdata()
    return jsonify(data)
if __name__ == "__main__":
    app.run(debug=True)


# def StackData():
#     #ShowInServer = stackdata()
#     app = Flask(__name__)

#     @app.route("/updatedStack")
#     def product():
#         #return ShowInServer
#         return ("fff")
#     if __name__ == "__main__":
#         app.run(debug=True)


#insertDAL()
#StackData()

