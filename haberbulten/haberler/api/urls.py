from django.urls import include, path
from haberler.api import views as api_views


urlpatterns = [
    path('makaleler/', api_views.makale_list_api_view, name='makale-list')
]
