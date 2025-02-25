from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('party/<int:party_id>/', views.party_detail, name='party_detail'),
    path('vote/', views.vote, name='vote'),
    path('results/', views.results, name='results'),
      # Add this line

]