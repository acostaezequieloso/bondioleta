"""
URL configuration for empleados project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aplications.empleado.views import IndexView, ModeloPruebaListView, pruebalistview
from aplications.tasks import views
from aplications.tasks.views import MenuView as TasksMenuView
from django.conf import settings
from django.conf.urls.static import static
from aplications.tasks.views import buscar_categorias, search, cart, mycart



urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('home/', IndexView.as_view()),
    path('lista/', pruebalistview.as_view()),
    path('lista-prueba/', ModeloPruebaListView.as_view()),
    path('tasks/', TasksMenuView.as_view()),

    path('search/', views.search, name='search'),
    path('Categorias/<slug>',views.buscar_categorias,name='categorias'),
    path('detail/<slug>',views.detail,name='detail'),
    path('<slug>/cart',views.cart,name='cart'),
    path('mycart/',views.mycart,name='mycart'),
    
    
#Vistas creadas por mi para el restaurante
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    #path('tasks/', views.tasks, name='tasks'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)