
from django.contrib import admin
from django.urls import path
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
