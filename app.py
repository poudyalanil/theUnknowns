from flask import Flask, render_template,  url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app  = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///tuks.db'
db = SQLAlchemy(app)

# here we will store portfolios' details
class portfoliodtl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable = False)
    company = db.Column(db.String(120), nullable = True)
    year_completed = db.Column(db.Integer)
    info = db.Column(db.String(500), nullable = False)
    image = db.Column(db.String(2083), nullable = False)

    def __repr__(self):
        return self.title





@app.route('/', methods = ['GET'])
def index():
    portfolio = portfoliodtl.query.all()
    return render_template('/index.html', portfolio = portfolio)




@app.route('/addportfolio', methods = ['POST','GET'])
def portfolio():
    if request.method =='POST':
        title = request.form['title']
        name = request.form['name']
        year = request.form['year']
        images = request.form['image']
        infos =request.form['info']
        
        newPortfolio = portfoliodtl(
            title=title,
            company=name,
            year_completed=year,
            info=infos,
            image=images

        )
        try:
            db.session.add(newPortfolio)
            db.session.commit()
            return redirect('/')
        except:
            return "Couldnot add a portfolio "
    else:
        return render_template('/addPortfolio.html')


if __name__=='__main__':
    app.run(debug=True)