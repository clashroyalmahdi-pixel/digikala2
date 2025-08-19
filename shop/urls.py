
from django.urls import path
from . import views
urlpatterns = [
    path('', views.helloworled, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user , name='logout'),
    path('product/<int:pk>', views.product , name='product'),
    path('category/<str:cat>', views.category , name='category'),
    path('signup/', views.signup_user , name='signup'),
    path('update_user/', views.update_user , name='update_user'),
    path('update_info/', views.update_info , name='update_info'),
    path('update_password/', views.update_password , name='update_password'),
    path('category/', views.category_summry , name='category_summry'),
    path('search/', views.search , name='search'),
    path('orders/', views.user_orders , name='orders'),
    path('order_details/<int:pk>', views.order_details , name='order_details'),
]