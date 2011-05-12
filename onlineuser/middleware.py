from onlineuser.models import Online

class OnlineUserMiddleware:
    def process_request(self, request):
        user = request.user
        ip=request.META['REMOTE_ADDR']
        if user.is_authenticated():
            o, created = Online.objects.get_or_create(user=user)
            o.session_key = ip
        else:
            o, created = Online.objects.get_or_create(ident=ip)
            o.session_key = ip
        if not created:
            o.save()
