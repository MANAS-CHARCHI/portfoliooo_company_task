from django.urls import path
from Portfolio.views import *

urlpatterns = [
    path('folio/', PortfolioView.as_view(), name='portfolio-details'),
    path('folio/<int:pk>', PortfolioView.as_view(), name='portfolio-details'),
    path('education/', EducationView.as_view(), name='education-details'),
    path('education/<int:pk>', EducationView.as_view(), name='education-details'),
    path('projects/', ProjectsView.as_view(), name='projects-details'),
    path('projects/<int:pk>', ProjectsView.as_view(), name='projects-details'),
]

