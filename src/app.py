import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the Jackson family object
jackson_family = FamilyStructure("Jackson")

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_members():
    try:
        members = jackson_family.get_all_members()
        return jsonify(members), 200
    except:
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"msg": "Member not found"}), 404

@app.route('/member', methods=['POST'])
def add_member():
    body = request.get_json()
    if not body:
        return jsonify({"msg": "Body is required"}), 400

    required_fields = ["first_name", "age", "lucky_numbers"]
    for field in required_fields:
        if field not in body:
            return jsonify({"msg": f"'{field}' is required"}), 400

    new_member = {
        "first_name": body["first_name"],
        "age": body["age"],
        "lucky_numbers": body["lucky_numbers"]
    }
    if "id" in body:
        new_member["id"] = body["id"]

    member = jackson_family.add_member(new_member)
    return jsonify(member), 200

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    success = jackson_family.delete_member(member_id)
    if success:
        return jsonify({"done": True}), 200
    else:
        return jsonify({"msg": "Member not found"}), 404

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
