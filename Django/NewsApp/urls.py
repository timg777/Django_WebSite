from django.urls import path
from .views import NewsP, Home, Contact, NewsDate, modelform, addModalForm

urlpatterns = [
    path('news/', NewsP, name='news'),
    path('', Home, name='home'),
    path('newsdate/<int:year>', NewsDate, name='newsdate'),
    path('contact/', Contact, name='contact'),
    # path('signup/', register, name='register'),
    # path('addUser/', addUser, name='addUser'),
    path('modalform/', modelform, name='form'),
    path('addmodalform/', addModalForm, name='modalform'),
]
