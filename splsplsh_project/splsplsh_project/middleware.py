from django.contrib.auth.views import redirect_to_login

class LoginRequiredMiddleware(object):
    def process_request(self, request):
        if not (request.user.is_authenticated()
            or request.path.startswith('/accounts/login')
            or request.path.startswith('/accounts/reset')
            or request.path.startswith('/accounts/register')
            or request.path.startswith('/accounts/activate')
            or request.path.startswith('/static')):
            return redirect_to_login(request.get_full_path())
