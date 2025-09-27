from django.urls import path
from .views import CalculateMaterialsView
urlpatterns = [
    path('view/', CalculateMaterialsView.as_view(), name='material-view')
]
