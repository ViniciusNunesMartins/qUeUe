from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('queue/', include("Queue.urls")),
    path('member/', include("Member.urls")),
]
