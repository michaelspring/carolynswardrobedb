"""weatherWear URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from profiles import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.search, name='search'),
    url(r'^tidy/', views.tidy, name='tidy'),
    url(r'^results/', views.results, name='results'),
    url(r'^q_weekendBrunch/', views.q_weekendBrunch, name='weekend_brunch_url'),
    url(r'^q_summerVibes/', views.q_summerVibes, name='summer_vibes_url'),
    url(r'^q_professional/', views.q_professional, name='professional_url'),
    url(r'^q_partyTime/', views.q_partyTime, name='party_time_url'),
    url(r'^q_enVacances/', views.q_enVacances, name='en_vacances_url'),
    url(r'^q_active/', views.q_active, name='active_url'),
    url(r'^qfeelingFresh/', views.q_feelingFresh, name='feeling_fresh_url'),
    url(r'^q_inbetween/', views.q_inbetween, name='inbetweeen_url'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
