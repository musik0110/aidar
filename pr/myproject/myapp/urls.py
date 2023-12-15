# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static
from .views import SignUpView

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')

# myapp/urls.py
from django.urls import path
from .views import CustomLoginView, register

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    # Другие URL-пути вашего приложения...
]


urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignUpView.as_view(), name='signup'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)