from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel_planner.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models for the database
class Itinerary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.String(10), nullable=False)
    end_date = db.Column(db.String(10), nullable=False)
    accommodations = db.relationship('Accommodation', backref='itinerary', lazy=True)
    activities = db.relationship('Activity', backref='itinerary', lazy=True)

class Accommodation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    itinerary_id = db.Column(db.Integer, db.ForeignKey('itinerary.id'), nullable=False)

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    date = db.Column(db.String(10), nullable=False)
    itinerary_id = db.Column(db.Integer, db.ForeignKey('itinerary.id'), nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    itineraries = Itinerary.query.all()
    return render_template('index.html', itineraries=itineraries)

@app.route('/create', methods=['GET', 'POST'])
def create_itinerary():
    if request.method == 'POST':
        name = request.form['name']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        new_itinerary = Itinerary(name=name, start_date=start_date, end_date=end_date)
        db.session.add(new_itinerary)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_itinerary.html')

@app.route('/itinerary/<int:id>', methods=['GET', 'POST'])
def view_itinerary(id):
    itinerary = Itinerary.query.get(id)
    if not itinerary:
        return redirect(url_for('index'))

    if request.method == 'POST':
        if 'add_accommodation' in request.form:
            name = request.form['accommodation_name']
            location = request.form['accommodation_location']
            new_accommodation = Accommodation(name=name, location=location, itinerary_id=id)
            db.session.add(new_accommodation)
            db.session.commit()
        elif 'add_activity' in request.form:
            activity_name = request.form['activity_name']
            activity_date = request.form['activity_date']
            activity_description = request.form['activity_description']
            new_activity = Activity(name=activity_name, date=activity_date, description=activity_description, itinerary_id=id)
            db.session.add(new_activity)
            db.session.commit()

    return render_template('view_itinerary.html', itinerary=itinerary)

@app.route('/itinerary/edit/<int:id>', methods=['GET', 'POST'])
def edit_itinerary(id):
    itinerary = Itinerary.query.get(id)
    if not itinerary:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        itinerary.name = request.form['name']
        itinerary.start_date = request.form['start_date']
        itinerary.end_date = request.form['end_date']
        db.session.commit()
        return redirect(url_for('view_itinerary', id=id))

    return render_template('edit_itinerary.html', itinerary=itinerary)

@app.route('/accommodation/delete/<int:id>', methods=['GET'])
def delete_accommodation(id):
    accommodation = Accommodation.query.get(id)
    db.session.delete(accommodation)
    db.session.commit()
    return redirect(url_for('view_itinerary', id=accommodation.itinerary_id))

@app.route('/activity/delete/<int:id>', methods=['GET'])
def delete_activity(id):
    activity = Activity.query.get(id)
    db.session.delete(activity)
    db.session.commit()
    return redirect(url_for('view_itinerary', id=activity.itinerary_id))

if __name__ == "__main__":
    app.run(debug=True)
