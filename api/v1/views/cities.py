#!/usr/bin/python3
"""
Creating new view for State object
that handles all default RestFul API actions
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
<<<<<<< HEAD
from models import State


@app_views.route('/states', methods=["GET"])
def get_all_states():
=======
from models import City


@app_views.route("/states/<state_id>/cities", methods=["GET"],
                 strict_slashes=False)
def state_city(state_id):
>>>>>>> 0e81719157a643eb18d87f79e759126afbcf4786
    """
    gets all states
    """
<<<<<<< HEAD
    states = []
    for v in storage.all("State").values():
        states.append(v.to_dict())
    return (jsonify(states))


@app_views.route("/states/<state_id>", methods=["GET"])
def state(state_id=None):
=======
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    cities = []
    all_cities = storage.all("City")
    for k, v in all_cities.items():
        if v.state_id == str(state_id):
            cities.append(v.to_dict())
    return (jsonify(cities), 200)


@app_views.route("/cities/<city_id>", methods=["GET"],
                 strict_slashes=False)
def city_all(city_id):
>>>>>>> 0e81719157a643eb18d87f79e759126afbcf4786
    """
    function to retrieve list of all states
    """
<<<<<<< HEAD
    if state_id is None:
        states = storage.all("State")
        get_state = [value.to_dict() for key, value in states.items()]
        return (jsonify(get_state))
    get_state = storage.get("State", state_id)
    if get_state is not None:
        return (jsonify(get_state.to_dict()))
    abort(404)


@app_views.route('/states/<state_id>', methods=["DELETE"])
def delete_states(state_id):
=======
    ct = storage.get("City", city_id)
    if ct is None:
        abort(404)
    return (jsonify(ct.to_dict()), 200)


@app_views.route('/cities/<city_id>', methods=["DELETE"],
                 strict_slashes=False)
def delete_cities(city_id):
>>>>>>> 0e81719157a643eb18d87f79e759126afbcf4786
    """
    function to delete state based on id
    """
<<<<<<< HEAD
    del_state = storage.all("State").values()
    obj = [obje.to_dict() for obje in del_state if obje.id == state_id]
    if obj == []:
        abort(404)
    obj.remove(obj[0])
    for obje in del_state:
        if obje.id == state_id:
            storage.delete(obje)
            storage.save()
    return (jsonify({}), 200)


@app_views.route('/states/', methods=["POST"])
def post_states():
=======
    try:
        del_city = storage.all("City").values()
        obj = [obje.to_dict() for obje in del_city if obje.id == city_id]
        if obj is None:
            abort(404)
        obj.remove(obj[0])
        for obje in del_city:
            if obje.id == city_id:
                storage.delete(obje)
                storage.save()
        return (jsonify({}), 200)
    except Exception:
        abort(404)


@app_views.route('/states/<state_id>/cities', methods=["POST"],
                 strict_slashes=False)
def post_cities(state_id):
>>>>>>> 0e81719157a643eb18d87f79e759126afbcf4786
    """
    function to add states
    """
<<<<<<< HEAD
    content = request.get_json()
    if content is None:
        return (jsonify({"error": "Not a JSON"}), 400)
    name = content.get("name")
    if name is None:
        return (jsonify({"error": "Missing name"}), 400)

    add_state = State()
    add_state.name = name
    add_state.save()

    return (jsonify(add_state.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=["PUT"], strict_slashes=False)
def update_states(state_id):
=======
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    content = request.get_json()
    if not content:
        return (jsonify({"error": "Not a JSON"}), 400)
    if "name" not in content:
        return (jsonify({"error": "Missing name"}), 400)
    content['state_id'] = state.id
    post_city = City(**content)
    post_city.save()

    return (jsonify(post_city.to_dict()), 201)


@app_views.route('/cities/<city_id>', methods=["PUT"],
                 strict_slashes=False)
def update_cities(city_id):
>>>>>>> 0e81719157a643eb18d87f79e759126afbcf4786
    """
    function to update states
    """
<<<<<<< HEAD
    set_state = storage.get("State", state_id)
    if set_state is None:
        abort(404)

    if not request.json:
        return (jsonify({"error": "Not a JSON"}), 400)

    content = request.get_json()
=======
    check = ["id", "created_at", "updated_at", "state_id"]

    set_city = storage.get("City", city_id)
    if not set_city:
        abort(404)
>>>>>>> 0e81719157a643eb18d87f79e759126afbcf4786

    if not request.get_json():
        return (jsonify({"error": "Not a JSON"}), 400)

    content = request.get_json()
    for key, value in content.items():
<<<<<<< HEAD
        if key != "id" or key != "created_at" or key != "updated_at":
            setattr(set_state, key, value)

    set_state.save()
    return (jsonify(set_state.to_dict()), 200)
=======
        if key not in check:
            setattr(set_city, key, value)

    set_city.save()
    return (jsonify(set_city.to_dict()), 200)
>>>>>>> 0e81719157a643eb18d87f79e759126afbcf4786
