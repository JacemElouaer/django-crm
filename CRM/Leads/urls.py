from django.urls import path
from .views import *

app_name = "leads"
urlpatterns = [
    path('', lead_list, name="lead_list"),
    path('<int:id>/', lead_detail, name="lead_detail"),
    path('<int:id>/update', lead_update, name="lead_update"),
    path('<int:id>/delete', lead_delete, name="lead_delete"),
    path('create/', lead_create, name="lead_create")

]
