# mainapp/mixins.py
from django.contrib.auth.mixins import UserPassesTestMixin
from communication.models import Post
from userapp.models import CustomUser, Profile
from mainapp.models import DiscipleshipGroup, AgeGroup, ServingTeam, RopesClass

class PastorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name="Pastor").exists()

    def handle_no_permission(self):
        from django.shortcuts import redirect
        return redirect("/not-authorized/")


class PastorContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "posts": Post.objects.all()[:3],
            "leaders": CustomUser.objects.filter(groups__name__in=["Pastor", "Leader", "DG Leader"]).distinct(),
        })
        return context
