"""
URL configuration for webApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from ankieta.views import AnkietaList, AnkietaDetail, AnkietaDelete, AnkietaCreate, AnkietaEdit, AnkietaListJSON

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AnkietaList.as_view(), name='ankieta_list'),
    path('data.json', AnkietaListJSON.as_view(), name='ankieta_list_json'),
    path('detail/<int:pk>', AnkietaDetail.as_view(), name='ankieta_detail'),
    path('delete/<int:pk>', AnkietaDelete.as_view(), name='ankieta_delete'),
    path('create/', AnkietaCreate.as_view(), name='ankieta_create'),
    path('edit/<int:pk>', AnkietaEdit.as_view(), name='ankieta_edit')
]
