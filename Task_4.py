from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for users
users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"}
}

# -------------------------------
# HOME ROUTE
# -------------------------------
@app.route('/')
def home():
    return "🚀 Welcome to the User API! Try /users to see all users."

# -------------------------------
# GET all users
# -------------------------------
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# -------------------------------
# GET user by ID
# -------------------------------
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id])
    return jsonify({"error": "User not found"}), 404

# -------------------------------
# CREATE new user (POST)
# -------------------------------
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Invalid input"}), 400

    user_id = max(users.keys(), default=0) + 1
    users[user_id] = {"name": data["name"], "email": data["email"]}
    return jsonify({"id": user_id, "message": "User created successfully"}), 201

# -------------------------------
# UPDATE existing user (PUT)
# -------------------------------
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    users[user_id].update(data)
    return jsonify({"message": "User updated successfully", "user": users[user_id]})

# -------------------------------
# DELETE user
# -------------------------------
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    del users[user_id]
    return jsonify({"message": "User deleted successfully"})

# Run app
if __name__ == '__main__':
    app.run(debug=True)

