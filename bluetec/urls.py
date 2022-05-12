from django.urls import path
from .views import home, team, about_us, career, service, case_studies, contact_us, portfolio

urlpatterns = [
    path(r'', home, name='home'),
    path(r'team/', team, name='our-team'),
    path(r'about_us/', about_us, name='about-us'),
    path(r'service/', service, name='service'),
    path(r'case_studies/', case_studies, name='case-studies'),
    path(r'contact_us/', contact_us, name='contact-us'),
    path(r'portfolio/', portfolio, name='portfolio'),
    path(r'career/', career, name='career'),
]
