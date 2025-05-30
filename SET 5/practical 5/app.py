#AIM: A program that creates a RESTful API thatsupports data validation and error handling.

from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)  # Corrected Flask app initialization
api = Api(app)

# Dummy data (replace with your actual data source)
items = {
    "1": {"name": "Item 1", "price": 10.99},
    "2": {"name": "Item 2", "price": 19.99},
}

# Request parser for input validation
parser = reqparse.RequestParser()
parser.add_argument("name", type=str, required=True, help="Name cannot be blank")
parser.add_argument("price", type=float, required=True, help="Price cannot be blank")

class ItemResource(Resource):
    def get(self, item_id):
        item = items.get(item_id)
        if item:
            return item
        else:
            return {"error": "Item not found"}, 404

    def put(self, item_id):
        args = parser.parse_args()
        items[item_id] = {"name": args["name"], "price": args["price"]}
        return items[item_id], 201

    def delete(self, item_id):
        if item_id in items:
            del items[item_id]
            return {"result": True}
        else:
            return {"error": "Item not found"}, 404

# Add the ItemResource as an API resource
api.add_resource(ItemResource, "/items/<item_id>")

# Run the app
if __name__ == "__main__":  # Corrected the check to run the app
    app.run(debug=True)

