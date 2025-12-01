from django.urls import path, include
from django.shortcuts import redirect
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import CustomLoginView, quiz, sessions, start, new_session, session_details
from .viewsets import QuizViewSet



app_name = 'website'

router = DefaultRouter()
router.register(r'quiz', QuizViewSet)


urlpatterns = [
    # Web site
    path('', lambda request: redirect('website:start')),
    path('start/', start, name='start'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path("quiz/", quiz, name="quiz"),
    path('sessions/', sessions, name='sessions'),
    path('session/<int:session_id>/', session_details, name='session_details'),
    path('quiz/<int:quiz_id>/', new_session, name='new_session'),

    # Endpoints
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/ui/', SpectacularSwaggerView.as_view(url_name='website:schema'), name='schema-swagger-ui'),
    path('api/doc/', SpectacularRedocView.as_view(url_name='website:schema'), name='schema-redoc'),
]
