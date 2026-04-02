# onboarding_steps.py

steps = {
    "school_registered": False,
    "admin_created": False,
    "features_activated": False,
    "onboarding_completed": False
}

def update_step(step_name):
    steps[step_name] = True

    if (
        steps["school_registered"]
        and steps["admin_created"]
        and steps["features_activated"]
    ):
        steps["onboarding_completed"] = True


def get_status():
    return {
        "status": "Onboarding completed" if steps["onboarding_completed"] else "Onboarding in progress",
        "steps": steps
    }
ONBOARDING_STEPS = [
    "school_registration",
    "admin_creation",
    "school_profile",
    "branding_setup",
    "academic_setup",
    "feature_activation",
    "onboarding_completed"
]