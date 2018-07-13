from django.conf.urls import url
from django.contrib import admin
from Monthly_Expenses_App import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^getpage/',views.Home_Logs)
]
