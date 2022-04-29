from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home),
    path('Login/',views.Login),
    path('Signup/',views.Signup),
    path('Order/',views.Order),
    path('EachItem/<uuid:pk>/',views.EachItem),
    path('Logout/',views.Logout),
    path('YourCart/',views.YourCart),
]
