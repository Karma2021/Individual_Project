from django.urls import path

from user import views



urlpatterns = [

    path("login/",views.login_page),

    path('register/',views.register_page),

    path('logout/',views.logout_fn)



   

   

   

    # path('admin/', admin.site.urls),

]