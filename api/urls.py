from django.conf.urls import url
from .views import Signup,Login

urlpatterns = [
    url(r'^signup/$', Signup.as_view(), name='signup'),
    url(r'^login/$', Login.as_view(), name='login'),
]
