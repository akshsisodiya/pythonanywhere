"""sentimentanalysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from cta import views

urlpatterns = [
    path('home/', include('cta.urls')),
    path('', include('cta.urls')),
    path('admin/', admin.site.urls),
    path('major_cities',views.major_cities, name='major_cities'),
    path('about-us/',views.about_us, name='about-us'),
    path('live-analysis/',views.live_analysis, name='live-analysis'),
    path('covid-cases/',views.covid_cases, name='covid-cases'),
    path('api/live-analysis/',views.api_live_analysis, name='covid-cases'),
    path('city/<str:city_name>/',views.city)

]