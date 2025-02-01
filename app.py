from flask import Flask, app,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///foods.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)


class Food(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    cooking_time=db.Column(db.Integer,nullable=False)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        food_name = request.form["name"]
        cooking_time = int(request.form["cooking_time"])
        
        new_food = Food(name=food_name, cooking_time=cooking_time)
        db.session.add(new_food)
        db.session.commit()
        
        return redirect(url_for("home"))

    foods = Food.query.all()
    return render_template("index.html", foods=foods)

with app.app_context():
    db.create_all() 

@app.route("/delete/<int:id>")
def delete_food(id):
    food = Food.query.get(id)
    if food:
        db.session.delete(food)
        db.session.commit()
    return redirect(url_for("home"))

if __name__=="__main__":
    app.run(debug=True)
