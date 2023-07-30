from django.urls import path 
from . import views


app_name = 'static_page'

urlpatterns = [
    path ('',views.index, name ="index"),
]
