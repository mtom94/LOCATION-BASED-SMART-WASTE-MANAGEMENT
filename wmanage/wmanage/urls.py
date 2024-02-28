"""
URL configuration for wmanage project.

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
from w_app.views import *
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', display_login), 
    path('display_login/', display_login, name="display_login"),
    path('display_reg/', display_reg, name="display_reg"),
    path('reg_u/', reg_u, name="reg_u"),
    path('check_login/', check_login, name="check_login"),
    path('logout/', logout, name="logout"),
    path('show_home_admin/', show_home_admin, name="show_home_admin"),
    path('add_drivers/', add_drivers, name="add_drivers"),
    path('add_drw_db/', add_drw_db, name="add_drw_db"),
    path('man_driver/', man_driver, name="man_driver"),
    path('edit_drv/', edit_drv, name="edit_drv"),
    path('del_drv/', del_drv, name="del_drv"),
    path('show_home_user/', show_home_user, name="show_home_user"),
]
