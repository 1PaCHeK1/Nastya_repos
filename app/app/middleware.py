from rest_framework.response import Response
from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.models import Session

from asgiref.sync import sync_to_async

from users.models import User
import urllib.parse as urlparse

class DisableCSRFMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
        response = self.get_response(request)
        return response


class AuthChatMiddleware:
    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        scope["user"] = AnonymousUser()
        
        cookies = dict(scope['headers']).get(b'cookie', b'').decode()
        if cookies == '':
            cookies = '0=0'
        cookies = dict([s.split('=', maxsplit=1) for s in cookies.split('; ')])
        
        query_string = urlparse.parse_qs(scope.get('query_string'))
        session_id = None
        if 'sessionid' in cookies:
            session_id = cookies['sessionid']
        elif b'sessionid' in query_string: 
            session_id = query_string[b'sessionid'][0].decode()

        if session_id:
            sessions = await sync_to_async(Session.objects.filter)(session_key=session_id)
            if await sync_to_async(sessions.exists)():
                session = await sync_to_async(sessions.first)()
                session_data = session.get_decoded()
                uid = session_data.get('_auth_user_id')
                user = await sync_to_async(User.objects.get)(id=uid)
                scope["user"] = user
        
        return await self.inner(scope, receive, send)
        