from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('predict',views.find,name='predict'),
    path('about',views.about,name='about')

]
