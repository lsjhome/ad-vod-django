from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.post_list),
        url(r'^(?P<id>\d+)/$', views.post_detail), # post_detail이라는 함수가 있어야 하고 거기에는 id라는 필드를 받을 수 있어야 한다.
]
