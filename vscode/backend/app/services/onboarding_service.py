from backend.app.models.onboarding_status_model import OnboardingStatus
from backend.app.database import SessionLocal


def update_onboarding_status(school_id, step):
    db = SessionLocal()

    status = OnboardingStatus(
        school_id=school_id,
        step=step,
        status="completed"
    )

    db.add(status)
    db.commit()
    db.close()


def register_school(data):

    school_id = 1

    update_onboarding_status(school_id, "register_school")

    return {
        "message": "School registered",
        "school_id": school_id
    }


def create_admin(data):

    school_id = data.get("school_id")

    update_onboarding_status(school_id, "create_admin")

    return {"message": "Admin created"}


def complete_profile(data):

    school_id = data.get("school_id")

    update_onboarding_status(school_id, "complete_profile")

    return {"message": "Profile completed"}


def setup_branding(data):

    school_id = data.get("school_id")

    update_onboarding_status(school_id, "setup_branding")

    return {"message": "Branding setup"}


def setup_academics(data):

    school_id = data.get("school_id")

    update_onboarding_status(school_id, "setup_academics")

    return {"message": "Academics setup"}


def activate_features(data):

    school_id = data.get("school_id")

    update_onboarding_status(school_id, "activate_features")

    return {"message": "Features activated"}


def complete_onboarding(data):

    school_id = data.get("school_id")

    update_onboarding_status(school_id, "complete_onboarding")

    return {"message": "Onboarding completed"}


def get_onboarding_status(school_id):

    db = SessionLocal()

    steps = db.query(OnboardingStatus).filter(
        OnboardingStatus.school_id == school_id
    ).all()

    db.close()

    return steps


def admin_override(data):
    return {"message": "Admin override successful"}