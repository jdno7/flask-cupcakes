from flask import Flask, render_template, request, jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

def serialize_cupcake(cupcake):

    return {
        "id": cupcake.id,
        "flavor": cupcake.flavor,
        "size": cupcake.size,
        "rating": cupcake.rating,
        "image": cupcake.image,
    }


@app.route('/api/cupcakes')
def get_cupcakes():
    """Return JSON {cupcakes: [{id,flavor,size...}]}"""

    cupcakes = Cupcake.query.all()

    serialized = [serialize_cupcake(cupcake) for cupcake in cupcakes]

    return jsonify(cupcakes=serialized)



@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():

    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    if request.json.get('image'):
        image = request.json['image']
        cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
        db.session.add(cupcake)
        db.session.commit()
        return (jsonify(cupcake=serialize_cupcake(cupcake)), 201)

    cupcake = Cupcake(flavor=flavor, size=size, rating=rating)
    db.session.add(cupcake)
    db.session.commit()
    return (jsonify(cupcake=serialize_cupcake(cupcake)), 201)

@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    """Return JSON of an individual cupcake {id,flavor,size...} """

    cupcake = Cupcake.query.get_or_404(id)

    serialized = serialize_cupcake(cupcake)

    return jsonify(cupcake=serialized)

@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    """Update cupcake and Return JSON of an individual cupcake {id,flavor,size...} """

    data = request.json

    cupcake = Cupcake.query.get_or_404(id)

    cupcake.flavor = data['flavor']
    cupcake.size = data['size']
    cupcake.rating = data['rating']
    cupcake.image = data['image']
    db.session.add(cupcake)
    db.session.commit()

    serialized = serialize_cupcake(cupcake)

    return jsonify(cupcake=serialized)


@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    """Delete cupcake and Return {message: "Deleted"} """

    cupcake = Cupcake.query.get_or_404(id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Deleted")

@app.route('/')
def home_base():

    return render_template('home.html')