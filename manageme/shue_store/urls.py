from django.urls import path, include
from .views import index
from .views import parentView
from .views import deviceView

urlpatterns = [
    path('', index.index, name='index'),
    path('device/', deviceView.showList, name='device'),
    path('device/add/', deviceView.Register.as_view(), name='device-add'),
    path('device/delete/<str:id>', deviceView.delete, name='device-delete'),

    path('parent/', parentView.showList, name='parent'),
    path('parent/add/', parentView.Register.as_view(), name='parent-add'),
    path('parent/delete/<str:id>', parentView.delete, name='parent-delete'),

]
