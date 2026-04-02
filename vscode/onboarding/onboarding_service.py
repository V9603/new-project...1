from backend.app.models.onboarding_status import *
onboarding_state = {
    "school": False,
    "admin": False,
    "profile": False,
    "branding": False,
    "academics": False,
    "features": False,
    "completed": False
}


def register_school(data: dict):
    onboarding_state["school"] = True
    return {"message": "School registered successfully"}


def create_admin(data: dict):
    if onboarding_state["school"] == False:
        return {"error": "Register school first"}

    onboarding_state["admin"] = True
    return {"message": "Admin created successfully"}


def complete_profile(data: dict):
    onboarding_state["profile"] = True
    return {"message": "Profile completed"}


def setup_branding(data: dict):
    onboarding_state["branding"] = True
    return {"message": "Branding setup completed"}


def setup_academics(data: dict):
    onboarding_state["academics"] = True
    return {"message": "Academics setup completed"}


def activate_features(data: dict):
    onboarding_state["features"] = True
    return {"message": "Features activated"}


def complete_onboarding():
    onboarding_state["completed"] = True
    return {"message": "Onboarding completed"}

schools = []

def register_school(data):
    school = {
        "id": len(schools) + 1,
        "name": data["name"],
        "status": "registered"
    }

    schools.append(school)

    return school

def register_school(data):
    return {"message": "School registered", "data": data}


admins = []

def create_admin(data):

    admin = {
        "school_id": data["school_id"],
        "name": data["name"],
        "email": data["email"]
    }

    admins.append(admin)

    return {"message": "Admin created", "admin": admin}

profiles = []

def complete_profile(data):

    profile = {
        "school_id": data["school_id"],
        "address": data["address"],
        "phone": data["phone"]
    }

    profiles.append(profile)

    return {"message": "Profile completed", "profile": profile}

branding_data = []

def setup_branding(data):

    branding = {
        "school_id": data["school_id"],
        "logo": data["logo"],
        "theme": data["theme"]
    }

    branding_data.append(branding)

    return {"message": "Branding setup completed"}

academics_data = []

def setup_academics(data):

    academics = {
        "school_id": data["school_id"],
        "classes": data["classes"]
    }

    academics_data.append(academics)

    return {"message": "Academics setup completed"}

features_data = []

def activate_features(data):

    features = {
        "school_id": data["school_id"],
        "features": data["features"]
    }

    features_data.append(features)

    return {"message": "Features activated"}

completed_onboarding = []

def complete_onboarding(data):

    completed_onboarding.append(data["school_id"])

    return {"message": "Onboarding completed"}


def get_onboarding_status(school_id):
    return {"school_id": school_id, "status": "in_progress"}


def admin_override(data):
    return {"message": "Admin override applied"}

