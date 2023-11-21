from django.urls import path
from .views import expense_form

urlpatterns = [
    path('', expense_form, name='expense_form'),

]
