from django.urls import path
from .views import LabListView, LabDetailView,ContactMessageCreateView

urlpatterns = [
    path('labs/', LabListView.as_view(), name='lab-list'),
    path('labs/<str:key>/', LabDetailView.as_view(), name='lab-detail'),
    path('contact/', ContactMessageCreateView.as_view(), name='contact-create'),
]
