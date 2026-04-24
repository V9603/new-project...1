from backend.app.onboarding.onboarding_steps import onboarding_steps

def update_step(step):
    if step in onboarding_steps:
        onboarding_steps[step] = True

def get_status():
    return onboarding_steps