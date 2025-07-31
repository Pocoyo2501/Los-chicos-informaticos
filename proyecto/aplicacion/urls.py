from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),  # login (index4.html)
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),

    # rutas extra si deseas seguir usándolas
    path('index/', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('index3/', views.index3, name='index3'),
    path('index4/', views.index4, name='index4'),

path('login/', views.login_email, name='login'),
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),
    path('debug/', views.debug_urls),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

