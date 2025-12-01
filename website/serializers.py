from rest_framework.serializers import ModelSerializer
from website.models import Quiz



class QuizSerializer(ModelSerializer):
    class Meta:
        model = Quiz
        fields = [
            "id",
            "title",
            "image_url",
        ]
