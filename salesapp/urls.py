from django.urls import path
from.import views as v

urlpatterns = [
    path('',v.population,name='population'),
    path('home',v.home,name="home"),
    path('covid',v.covid,name='covid'),
    path('coviddata',v.covidapi,name='coviddata'),
] 