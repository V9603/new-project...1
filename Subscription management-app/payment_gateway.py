class PaymentGateway:
    def handle_event(self, event_type, user_id):
        if event_type == "success":
            return f"Payment successful for user {user_id}"
        elif event_type == "failure":
            return f"Payment failed for user {user_id}"
        elif event_type == "cancel":
            return f"Subscription cancelled for user {user_id}"
        elif event_type == "renew":
            return f"Subscription renewed for user {user_id}"
        else:
            return "Unknown event"

    def webhook_handler(self, data):
        event_type = data.get("event")
        user_id = data.get("user_id")
        return self.handle_event(event_type, user_id)
