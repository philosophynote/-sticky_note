
from django.contrib import admin
from django.urls import path, include

from learning import views

handler500 = views.my_customized_server_error

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('learning.urls')),
]

