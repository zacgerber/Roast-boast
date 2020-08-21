"""roastboast URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from homepage import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('make_post_view/', views.make_post_view),
    path('sorted_by_vote_view/', views.sorted_by_vote_view),
    path('up_vote_view/<int:up_vote_id>/', views.up_vote_view),
    path('down_vote_view/<int:down_vote_id>/', views.down_vote_view),
    path('roast_view/', views.roast_view, name="roast"),
    path('boast_view/', views.boast_view, name="boast"),
    # path('delete_post_view/<str:post_id>/', views.delete_post_view),
    path('admin/', admin.site.urls),
]
