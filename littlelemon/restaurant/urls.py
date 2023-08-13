from django.urls import path
from . import views
#from .views import menuview, bookingview

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='home'),
    #path('menu/', menuview.as_view()),
    #path('booking/', bookingview.as_view()),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuView.as_view()),
]
