from django.contrib import admin
from django.urls import path
from ankieta.views import AnkietaList, AnkietaDetail, AnkietaDelete, AnkietaCreate, AnkietaEdit, AnkietaListJSON

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', AnkietaList.as_view(), name='ankieta_list'),
    path('data.json', AnkietaListJSON.as_view(), name='ankieta_list_json'),
    path('detail/<int:pk>', AnkietaDetail.as_view(), name='ankieta_detail'),
    path('delete/<int:pk>', AnkietaDelete.as_view(), name='ankieta_delete'),
    path('create/', AnkietaCreate.as_view(), name='ankieta_create'),
    path('edit/<int:pk>', AnkietaEdit.as_view(), name='ankieta_edit')
]
