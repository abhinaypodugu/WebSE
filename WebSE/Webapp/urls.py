from Webapp import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="Webapp"),
    path('fddonate', views.FoodDonationView),
    path('login', views.loginPage, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.Logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('reset_password/', auth_views.PasswordResetView.as_view(),
         name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('accounts/login/', views.loginPage),
    path('fdrequest', views.FoodRequestView, name="fdrequest"),
]
