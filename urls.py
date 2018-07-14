from django.conf.urls import url
from django.contrib import admin
from Monthly_Expenses_App import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^show/',views.Home_Logs),
    url(r'^AddExpenses/',views.AddExpenses),
    url(r'^update/',views.update),
    
]
