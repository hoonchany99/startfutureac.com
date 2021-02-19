from django.urls import path
from .views import main_view, mobile_view
urlpatterns = [
    path('', main_view, name = 'main-view'),
    path('mobile/', mobile_view, name = 'mobile-view')
]