import datetime

class SubscriptionManager:
    def __init__(self):
        self.subscriptions = {}

    def activate_subscription(self, user_id, plan, trial_days=0, grace_days=0):
        expiry = None
        if trial_days > 0:
            expiry = datetime.datetime.now() + datetime.timedelta(days=trial_days)
        self.subscriptions[user_id] = {
            "plan": plan,
            "active": True,
            "expiry": expiry,
            "grace_days": grace_days,
            "paused": False,
            "quota": {
                "users": 5 if plan == "basic" else 50,
                "storage": 100 if plan == "basic" else 1000,
                "communication": 100 if plan == "basic" else 1000,
                "students": 50 if plan == "basic" else 500,
                "staff": 10 if plan == "basic" else 100
            }
        }
        return f"Activated {plan} for user {user_id} with trial {trial_days} days and grace {grace_days} days"

    def deactivate_subscription(self, user_id):
        if user_id in self.subscriptions:
            self.subscriptions[user_id]["active"] = False
            return f"Deactivated subscription for user {user_id}"
        return "User not found"

    def resume_subscription(self, user_id):
        if user_id in self.subscriptions:
            self.subscriptions[user_id]["active"] = True
            self.subscriptions[user_id]["paused"] = False
            return f"Resumed subscription for user {user_id}"
        return "User not found"

    def check_access(self, user_id, feature):
        sub = self.subscriptions.get(user_id)
        if not sub or not sub["active"]:
            return "Access denied: No active subscription"

        if sub["paused"]:
            return "Access denied: Subscription paused"

        if sub["expiry"] and datetime.datetime.now() > sub["expiry"]:
            grace_end = sub["expiry"] + datetime.timedelta(days=sub["grace_days"])
            if datetime.datetime.now() <= grace_end:
                return "Access limited: Subscription in grace period"
            return "Access denied: Subscription expired"

        plan = sub["plan"]
        if plan == "premium":
            return f"Access granted to {feature}"
        else:
            return f"{feature} blocked for {plan} plan"

    def check_quota(self, user_id, users, storage, communication, students, staff):
        sub = self.subscriptions.get(user_id)
        if not sub:
            return "No subscription found"
        q = sub["quota"]
        if users > q["users"]:
            return "User limit exceeded"
        if storage > q["storage"]:
            return "Storage limit exceeded"
        if communication > q["communication"]:
            return "Communication quota exceeded"
        if students > q["students"]:
            return "Student limit exceeded"
        if staff > q["staff"]:
            return "Staff limit exceeded"
        return "Quota check passed"

    def fetch_enabled_features(self, user_id):
        sub = self.subscriptions.get(user_id)
        if not sub:
            return []
        if sub["plan"] == "premium":
            return ["all_features"]
        else:
            return ["basic_features"]
