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
    link = db.Column(db.String(2083))

    def __repr__(self):
         return '<Task %r>' % self.id





@app.route('/', methods = ['GET','POST'])
def index():
    portfolio = portfoliodtl.query.all()
    return render_template('/index.html', p = portfolio)




@app.route('/addportfolio', methods = ['POST','GET'])
def portfolio():
    if request.method =='POST':
        titles = request.form['title']
        name = request.form['name']
        year = request.form['year']
        images = request.form['image']
        infos =request.form['info'],
        links =request.form['link']
        
        newPortfolio = portfoliodtl(
            title=titles,
            company=name,
            year_completed=year,
            info=infos,
            image=images,
            link = links

        )
        try:
            db.session.add(newPortfolio)
            db.session.commit()
             
            return redirect('/')
        except:
            return "Couldnot add a portfolio "
    else:
        portfolio = portfoliodtl.query.all()
        return render_template('/addPortfolio.html',p = portfolio)


@app.route('/delete/<int:id>')
def delete(id):
    del_portfolio = portfoliodtl.query.get_or_404(id)

    try:
        db.session.delete(del_portfolio)
        db.session.commit()
        return redirect('/addportfolio')
    except:
        return "Error!!!!!!!!"

@app.route('/update/<int:id>', methods = ['GET','POST'])
def update(id):
    pl = portfoliodtl.query.get_or_404(id)



    if request.method =='POST':
        pl.titles = request.form['title']
        pl.name = request.form['name']
        pl.year = request.form['year']
        pl.images = request.form['image']
        pl.infos =request.form['info']
        pl.link =request.form['link']

        
        try:
            
            db.session.commit()
             
            return redirect('/')
        except:
            return "Couldnot update a portfolio "
    else:
        portfolio = portfoliodtl.query.all()
        return render_template('/editPortfolio.html',p = pl)

if __name__=='__main__':
    app.run(debug=True)