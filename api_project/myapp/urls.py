# myapp/urls.py
from django.urls import path
from .views import PersonListCreateView, PersonDetailView, EmergencyListCreateView, EmergencyDetailView, FindingListCreateView, FindingDetailView

urlpatterns = [
    path('api/people/', PersonListCreateView.as_view(), name='person-list-create'),
    path('api/people/<int:pk>/', PersonDetailView.as_view(), name='person-detail'),
    path('api/emergencies/', EmergencyListCreateView.as_view(), name='emergency-list-create'),
    path('api/emergencies/<int:pk>/', EmergencyDetailView.as_view(), name='emergency-detail'),
    path('api/findings/', FindingListCreateView.as_view(), name='finding-list-create'),
    path('api/findings/<int:pk>/', FindingDetailView.as_view(), name='finding-detail'),
]

