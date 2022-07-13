from django.urls import include, path
from haberler.api import views as api_views


urlpatterns = [
    path('makaleler/', api_views.makale_list_api_view, name='makale-list'),
    path('makaleler/<int:pk>', api_views.makale_detail, name='makale-detay'),
]
