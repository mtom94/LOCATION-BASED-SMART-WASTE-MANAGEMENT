from django.contrib import admin
from django.urls import path
from w_app.views import *
from w_app.views import generate_csv
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
    # path('man_garbage_bins/', man_garbage_bins, name="man_garbage_bins"),
    path('add_garbage_bins/', add_garbage_bins, name="add_garbage_bins"),
    # path('add_grb_db/', add_grb_db, name="add_grb_db"),
    # path('edit_gbin/', edit_gbin, name="edit_gbin"),
    # path('del_gbin/', del_gbin, name="del_gbin"),
    path('reg_complaint/', reg_complaint, name="reg_complaint"),
    # path('view_cm_status/', view_cm_status, name="view_cm_status"),
    path('add_cmp_db/', add_cmp_db, name="add_cmp_db"),
    # path('view_users_complaint/', view_users_complaint, name="view_users_complaint"),
    # path('edit_cmp_status/', edit_cmp_status, name="edit_cmp_status"),
    # path('show_home_driver/', show_home_driver, name="show_home_driver"),
    path('generate_csv/',generate_csv,name='generate_csv'),

]