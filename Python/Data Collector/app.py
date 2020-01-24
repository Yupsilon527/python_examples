from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from email_sender import sendemail

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:postgres123@localhost/height_collector"

db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "data"
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(120),unique=True)
    height = db.Column(db.Integer)

    def __inil__(self,email_,height_):
        self.email=email_
        self.height=height_

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods = ["POST"])
def success():
    if request.method=="POST":
        email=request.form["email_name"]
        height=request.form["height_name"]
        if db.session.query(Data).filter(Data.email==email).count() == 0:
            submission = Data(email,height)
            db.session.add(submission)
            db.session.commit()
        text="Email already exists in our database."
        return render_template("success.html")

if __name__=="__main__":
    app.debug=True
    app.run()
