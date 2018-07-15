from django.conf.urls import url
from django.contrib import admin
from expense_record_app import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^show/',views.Home_Logs),
    url(r'^AddExpenses/',views.AddExpenses),
    url(r'^update/',views.update),
    url(r'^Login/',views.Login),
    url(r'^Sum/',views.calculation),
    url(r'^Divide/',views.DivideExpense)
