from django.urls import path
from basicapp import views


#TEMPLATE TAGGING
app_name = 'basicapp'


urlpatterns = [
    path('other/',views.other,name = 'other'),
    path('relative/',views.relative,name='relative'),
    path('index/',views.index,name='index'),
]
