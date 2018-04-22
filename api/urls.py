from django.conf.urls import url
from .views import Signup, Login, TournamentView, GroundView, UserView, LoginView, FPView

urlpatterns = [
    url(r'^signup/$', Signup.as_view(), name='signup'),
    # url(r'^login/$', Login.as_view(), name='login'),
    url(r'^tournament/$', TournamentView.as_view(), name='tournament'),
    url(r'^ground/$', GroundView.as_view(), name='ground'),
    url(r'^users/$', UserView.as_view(), name='users'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^pwreset/$', FPView.as_view(), name='password reset'),
]
