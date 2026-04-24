from subscription_manager import SubscriptionManager
from payment_gateway import PaymentGateway
from admin_service import AdminService

manager = SubscriptionManager()
gateway = PaymentGateway()
admin = AdminService(manager)

print(admin.assign_plan("user1", "basic", trial_days=3, grace_days=2))
print(manager.check_access("user1", "premium_feature"))
print(manager.check_quota("user1", users=3, storage=50, communication=20, students=10, staff=5))
print(gateway.handle_event("success", "user1"))
print(admin.pause_subscription("user1"))
print(admin.resume_subscription("user1"))
print(admin.fetch_features("user1"))
