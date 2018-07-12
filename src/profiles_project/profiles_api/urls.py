from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    url('^hello-view/', views.HelloApiView.as_view()),        
    url('', include(router.urls)),
]
