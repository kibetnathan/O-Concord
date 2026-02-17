# mainapp/mixins.py
from django.contrib.auth.mixins import UserPassesTestMixin

class PastorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name="Pastors").exists()

    def handle_no_permission(self):
        from django.shortcuts import redirect
        return redirect("/not-authorized/")
