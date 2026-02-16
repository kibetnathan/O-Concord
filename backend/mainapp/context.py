from .models import DiscipleshipGroup, AgeGroup, ServingTeam, RopesClass
def profile_processor(request):
    """Adds the logged-in user's profile to every template context."""
    profile = None
    if request.user.is_authenticated:
        try:
            profile = request.user.profile
        except Exception:
            profile = None
    return {'profile': profile}

def global_stats(request):
    return{
        "total_dgs" : DiscipleshipGroup.objects.count(),
        "age_groups" : AgeGroup.objects.count(),
        "departments" : ServingTeam.objects.count(),
        "ropes_classes" : RopesClass.objects.count(),
    }

