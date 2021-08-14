from django.views import View
from django.contrib import auth, messages
from django.shortcuts import redirect


class SignOutView(View):
    def post(self, request):
        auth.logout(request)
        messages.info(request, 'Signed out successfully')
        return redirect('sign_in')


