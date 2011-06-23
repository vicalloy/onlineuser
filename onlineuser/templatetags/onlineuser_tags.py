from django.template import Library

from onlineuser.models import getOnlineInfos

register = Library()

@register.inclusion_tag('onlineuser/dummy.html')
def onlineinfos(detail=True, template='onlineuser/onlineinfos.html'):
    ctx = getOnlineInfos(detail)
    ctx['template'] = template
    return ctx
