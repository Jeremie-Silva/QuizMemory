from django.contrib.admin import register, ModelAdmin
from .models import UserProfile, Quiz, Question, Answer, Session


@register(UserProfile)
class UserProfileAdmin(ModelAdmin):
    list_display = ("user",)
    fields = ("user",)


@register(Quiz)
class QuizAdmin(ModelAdmin):
    list_display = ("title", "image_url",)
    fields = ("title", "image_url",)


@register(Question)
class QuestionAdmin(ModelAdmin):
    list_display = ("title", "quiz", "correct_answer", "image",)
    fields = ("title", "quiz", "image", "correct_answer",)


@register(Session)
class SessionAdmin(ModelAdmin):
    list_display = ("user", "quiz", "start_time",)
    fields = ("user", "quiz",)


@register(Answer)
class AnswerAdmin(ModelAdmin):
    list_display = ("session", "question", "content",)
    fields = ("session", "question", "content",)
