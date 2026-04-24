from flask import Flask, request, jsonify
from subscription_manager import SubscriptionManager
from payment_gateway import PaymentGateway
from admin_service import AdminService

app = Flask(__name__)

manager = SubscriptionManager()
gateway = PaymentGateway()
admin = AdminService(manager)

@app.route("/", methods=["GET"])
def home():
    return "Subscription Management API is running!"

@app.route("/assign_plan", methods=["POST"])
def assign_plan():
    data = request.json
    return jsonify({"message": admin.assign_plan(
        data["user_id"], data["plan"], data.get("trial_days", 0), data.get("grace_days", 0)
    )})

@app.route("/check_access", methods=["POST"])
def check_access():
    data = request.json
    return jsonify({"message": manager.check_access(data["user_id"], data["feature"])})

@app.route("/check_quota", methods=["POST"])
def check_quota():
    data = request.json
    return jsonify({"message": manager.check_quota(
        data["user_id"], data["users"], data["storage"], data["communication"], data["students"], data["staff"]
    )})

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    return jsonify({"message": gateway.webhook_handler(data)})

@app.route("/health/<user_id>", methods=["GET"])
def health(user_id):
    return jsonify({"message": admin.check_health(user_id)})

@app.route("/pause/<user_id>", methods=["POST"])
def pause(user_id):
    return jsonify({"message": admin.pause_subscription(user_id)})

@app.route("/resume/<user_id>", methods=["POST"])
def resume(user_id):
    return jsonify({"message": admin.resume_subscription(user_id)})

@app.route("/features/<user_id>", methods=["GET"])
def features(user_id):
    return jsonify({"features": admin.fetch_features(user_id)})

if __name__ == "__main__":
    app.run(debug=True)
