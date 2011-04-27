from onlineuser.models import Online

class OnlineUserMiddleware:
    def process_request(self, request):
        user = request.user
        session_key = request.session.session_key
        if user.is_authenticated():
            o, created = Online.objects.get_or_create(user=user)
            o.session_key = session_key
        else:
            ip=request.META['REMOTE_ADDR']
            o, created = Online.objects.get_or_create(session_key=session_key)
            o.ident=ip
        o.save()
