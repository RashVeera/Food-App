from . import views
from django.urls import path
app_name='food'
urlpatterns = [
    path('',views.Indexview.as_view(),name='index' ),
    path('item/',views.item,name='item page'),
    path('<int:pk>/',views.Detail.as_view(),name='details'),
    path('add/',views.create_item,name='create_item'),
    path('update/<int:id>/',views.update,name='update_item'),
    path('delete/<int:id>/',views.delete,name='delete'),
]
