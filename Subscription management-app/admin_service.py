class AdminService:
    def __init__(self, subscription_manager):
        self.manager = subscription_manager

    def assign_plan(self, user_id, plan, trial_days=0, grace_days=0):
        return self.manager.activate_subscription(user_id, plan, trial_days, grace_days)

    def change_plan(self, user_id, new_plan):
        return self.manager.activate_subscription(user_id, new_plan)

    def pause_subscription(self, user_id):
        if user_id in self.manager.subscriptions:
            self.manager.subscriptions[user_id]["paused"] = True
            return f"Paused subscription for user {user_id}"
        return "User not found"

    def resume_subscription(self, user_id):
        return self.manager.resume_subscription(user_id)

    def check_health(self, user_id):
        if user_id in self.manager.subscriptions:
            return f"Subscription health: {self.manager.subscriptions[user_id]}"
        return "No subscription found"

    def fetch_features(self, user_id):
        return self.manager.fetch_enabled_features(user_id)
