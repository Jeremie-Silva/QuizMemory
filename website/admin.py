from django.contrib.admin import register, ModelAdmin
from .models import UserProfile, Quiz, Question, Answer, Session


@register(UserProfile)
class UserProfileAdmin(ModelAdmin):
    list_display = ("user",)
    fields = ("user",)


@register(Quiz)
class QuizAdmin(ModelAdmin):
    list_display = ("title", "cumulative_score")
    fields = ("title", "cumulative_score")


@register(Question)
class QuestionAdmin(ModelAdmin):
    list_display = ("title", "quiz", "score")
    fields = ("title", "quiz", "score")


@register(Answer)
class AnswerAdmin(ModelAdmin):
    list_display = ("question", "content", "right_answer")
    fields = ("question", "content", "right_answer")


@register(Session)
class SessionAdmin(ModelAdmin):
    list_display = ("user", "quiz", "score", "start_time")
    fields = ("user", "quiz")
