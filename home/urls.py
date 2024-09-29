from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('feedback/<int:id>', views.customer_feedback, name='feedback'),
    path('thankyou/', views.thankyou, name='thankyou'),
]