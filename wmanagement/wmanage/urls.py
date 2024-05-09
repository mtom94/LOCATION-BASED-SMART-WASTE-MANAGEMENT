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
    path('user_profile/', user_profile, name="user_profile"),
    path('edit_prof/', edit_prof, name="edit_prof"),
    path('change_password/', change_password, name="change_password"),
    path('forgot_p/', forgot_p, name="forgot_p"),
    path('check_login/', check_login, name="check_login"),
    path('logout/', logout, name="logout"),
    path('show_home_admin/', show_home_admin, name="show_home_admin"),
    path('add_drivers/', add_drivers, name="add_drivers"),
    path('add_drw_db/', add_drw_db, name="add_drw_db"),
    path('man_driver/', man_driver, name="man_driver"),
    path('edit_drv/', edit_drv, name="edit_drv"),
    path('del_drv/', del_drv, name="del_drv"),
    path('show_home_user/', show_home_user, name="show_home_user"),
    path('man_garbage_bins/', man_garbage_bins, name="man_garbage_bins"),
    path('add_garbage_bins/', add_garbage_bins, name="add_garbage_bins"),
    path('add_grb_db/', add_grb_db, name="add_grb_db"),
    path('edit_gbin/', edit_gbin, name="edit_gbin"),
    path('del_gbin/', del_gbin, name="del_gbin"),
    path('reg_complaint/', reg_complaint, name="reg_complaint"),
    path('view_cm_status/', view_cm_status, name="view_cm_status"),
    path('add_cmp_db/', add_cmp_db, name="add_cmp_db"),
    path('view_users_complaint/', view_users_complaint, name="view_users_complaint"),
    path('edit_cmp_status/', edit_cmp_status, name="edit_cmp_status"),
    path('search_driver/', search_driver, name="search_driver"),
    path('search_places/', search_places, name="search_places"),
    path('view_place_drivers/', view_place_drivers, name="view_place_drivers"),
    path('view_place_drivers.html', view_place_drivers_html, name='view_place_drivers_html'),
    path('view_garbage_report/', view_garbage_report, name="view_garbage_report"),
    path('view_garbage_refresh/', view_garbage_refresh, name="view_garbage_refresh"),
    path('show_home_driver/', show_home_driver, name="show_home_driver"),
    path('assign_work/', assign_work, name="assign_work"),
    path('assign_db/', assign_db, name="assign_db"),
    path('view_works/', view_works, name="view_works"),
    path('work_finished/', work_finished, name="work_finished"),
    path('work_path/', work_path, name="work_path"),
    path('view_map_p/', view_map_p, name="view_map_p"),
]
