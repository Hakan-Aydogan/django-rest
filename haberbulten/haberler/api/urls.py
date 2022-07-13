from django.urls import include, path
from haberler.api import views as api_views


urlpatterns = [
    path('makaleler/', api_views.MakaleListApiView.as_view(), name='makale-list'),
    path('makaleler/<int:pk>',
         api_views.MakaleDetailApiView.as_view(), name='makale-detay'),
    path('yazarlar/', api_views.YazarlarListApiView.as_view(), name='yazarlar'),
    path('yazarlar/<int:pk>', api_views.YazarDetailApiView.as_view(), name='yazar'),
]


""" urlpatterns = [
    path('makaleler/', api_views.makale_list_api_view, name='makale-list'),
    path('makaleler/<int:pk>', api_views.makale_detail, name='makale-detay'),
] """
