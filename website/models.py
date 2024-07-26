from django.db.models import Model, CASCADE, OneToOneField, CharField, ForeignKey, IntegerField, TextField, BooleanField
from django.contrib.auth.models import User


class UserProfile(Model):
    user = OneToOneField(User, on_delete=CASCADE, related_name="profile")
    is_staff = False

    def __str__(self):
        return self.user.username


class Quiz(Model):
    title = CharField(max_length=255)
    cumulative_score = IntegerField(default=0)

    def __str__(self):
        return self.title


class Question(Model):
    title = CharField(max_length=255)
    quiz = ForeignKey(Quiz, on_delete=CASCADE, related_name="questions")
    score = IntegerField(default=0)

    def __str__(self):
        return self.title


class Answer(Model):
    question = ForeignKey(Question, on_delete=CASCADE, related_name="answers")
    content = TextField()
    right_answer = BooleanField(default=False)

    def __str__(self):
        return self.content
