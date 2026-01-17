from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

# TODO: Implement homepage route that returns a welcome message

@app.route("/", methods=["GET"])
def home():
    # Return a welcome message for the API homepage
    return jsonify({"message": "Welcome to the Product Catalog API"}), 200

# TODO: Implement GET /products route that returns all products or filters by category

@app.route("/products", methods=["GET"])
def get_products():
    # Check if category query parameter is provided
    category = request.args.get("category")

    if category:
        # Normalize input to lowercase for case-insensitive filtering
        category = category.lower()
        # Filter products by category (also normalize stored category)
        filtered = [p for p in products if p["category"].lower() == category]
        return jsonify(filtered), 200

    # Return all products if no category filter
    return jsonify(products), 200

# TODO: Implement GET /products/<id> route that returns a specific product by ID or 404

@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    # Search for the product by ID
    for product in products:
        if product["id"] == id:
            return jsonify(product), 200

    # Return 404 if product not found
    return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
