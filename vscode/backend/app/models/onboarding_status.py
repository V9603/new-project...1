# simple in-memory storage for onboarding progress

onboarding_progress = {}

def create_onboarding_record(school_id):
    onboarding_progress[school_id] = {
        "register_school": False,
        "create_admin": False,
        "complete_profile": False,
        "branding_setup": False,
        "academics_setup": False,
        "features_activation": False,
        "completed": False
    }

def update_step(school_id, step):
    onboarding_progress[school_id][step] = True

def get_status(school_id):
    return onboarding_progress.get(school_id, {})