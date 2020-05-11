from django.urls import path
from .views import member_index, member_queue, member_create, member_exit


urlpatterns = [
    path('', member_index, name='member_index'),
    path('queue/', member_queue, name='member_queue'),
    path('create/', member_create, name='member_create'),
    path('exit/', member_exit, name='member_exit'),
]
