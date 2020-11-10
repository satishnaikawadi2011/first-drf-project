
from django.contrib import admin
from django.urls import path

from api import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/<int:id>',views.user_detail),
    path('users/',views.user_list),
    path('user/create',views.create_user),
    path('user/update/<int:id>',views.update_user),
    path('user/delete/<int:id>',views.delete_user)
]
