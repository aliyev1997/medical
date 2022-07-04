from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from core import views

router = routers.SimpleRouter()

router.register(r'doctors', views.DoctorViewSet, basename='doctor')
router.register(r'services', views.ServicesViewSet, basename='services')
router.register(r'feedback', views.FeedbackViewSet, basename='feedback')
router.register(r'feedbackmanager', views.FeedbackManagerViewSet, basename='feedbackmanager')
router.register(r'contacts', views.ContactsViewSet, basename='contacts')
router.register(r'apointment', views.ApointmentViewSet, basename='apointment')
router.register(r'ap', views.ApViewSet, basename='ap')
router.register(r'home', views.HomeViewSet, basename='home')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]

urlpatterns += router.urls
