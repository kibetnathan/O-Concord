def profile_processor(request):
    """Adds the logged-in user's profile to every template context."""
    profile = None
    if request.user.is_authenticated:
        try:
            profile = request.user.profile
        except Exception:
            profile = None
    return {'profile': profile}