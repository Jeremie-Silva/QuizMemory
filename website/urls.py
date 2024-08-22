from django.urls import path
from .views import CustomLoginView, quiz, sessions, start, new_session, session_details
from django.shortcuts import redirect


app_name = 'website'

urlpatterns = [
    path('', lambda request: redirect('website:start')),
    path('start/', start, name='start'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path("quiz/", quiz, name="quiz"),
    path('sessions/', sessions, name='sessions'),
    path('session/<int:session_id>/', session_details, name='session_details'),
    path('quiz/<int:quiz_id>/', new_session, name='new_session'),
]
