from django.urls import path
from .import views
urlpatterns = [
   path('', views.home, name="home"),
   path('warehouse/', views.warehouse, name="warehouse"),
   path('newitem/', views.NewItem, name="newitem"),
   path('addproduct/', views.AddProduct, name="addproduct"),
   path('outwarehouse/', views.outWareHouse, name="outwarehouse"),
   path('summary/', views.summary, name="summary"),
   path('personal/', views.PersonalFunc, name="personal"),
   path('userless/', views.UserlessFunc, name="userless"),
]