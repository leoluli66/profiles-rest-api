from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet) #we don't need base_name, since we have a queryset object

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()), #APIview
    path('', include(router.urls)) #Viewset, via Routers
]
