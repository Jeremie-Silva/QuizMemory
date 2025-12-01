from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from website.models import Quiz
from website.serializers import QuizSerializer



class QuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated,]
