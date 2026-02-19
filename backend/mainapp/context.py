from .models import FellowshipGroup, Services, Department, Course
from django.conf import settings
from communication.models import Post
from userapp.models import CustomUser

leaders = CustomUser.objects.filter(groups__name__in=["Pastors", "Admins"]).distinct()
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
        "total_fgs" : FellowshipGroup.objects.count(),
        "services_count" : Services.objects.count(),
        "departments_count" : Department.objects.count(),
        "courses_count" : Course.objects.count(),
        "global_posts": Post.objects.all(),
        "members_count": CustomUser.objects.count(),
    }

