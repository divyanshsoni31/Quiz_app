from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="quiz"),
    path("login/",views.loginview,name="login"),
    path("register/",views.registerview,name="register"),
    path("marks/",views.score,name="marks"),
    path("logout/",views.logoutview,name="logout")
]
