# mainapp/mixins.py
from django.contrib.auth.mixins import UserPassesTestMixin
from communication.models import Post
from mainapp.models import DiscipleshipGroup, AgeGroup, ServingTeam, RopesClass

class PastorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name="Pastors").exists()

    def handle_no_permission(self):
        from django.shortcuts import redirect
        return redirect("/not-authorized/")


class PastorContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "post_instances": Post.objects.all()[:5],  # latest 5 posts
            "total_dgs": DiscipleshipGroup.objects.count(),
            "age_groups": AgeGroup.objects.count(),
            "departments": ServingTeam.objects.count(),
            "ropes_classes": RopesClass.objects.count(),
        })
        return context
