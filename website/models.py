from django.db.models import Model, CASCADE, OneToOneField, CharField, ForeignKey, IntegerField, TextField, BooleanField, DateTimeField
from django.contrib.auth.models import User


class UserProfile(Model):
    user = OneToOneField(User, on_delete=CASCADE, related_name="profile")
    is_staff = False

    def __str__(self):
        return self.user.username


class Quiz(Model):
    title = CharField(max_length=255)

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


class Session(Model):
    user = ForeignKey(UserProfile, on_delete=CASCADE, related_name="sessions")
    quiz = ForeignKey(Quiz, on_delete=CASCADE, related_name="sessions")
    start_time = DateTimeField(auto_now_add=True)
    end_time = DateTimeField(null=True, blank=True)
    completed = BooleanField(default=False)

    def __str__(self):
        return f"{self.user.user.username} - {self.quiz.title} - {'Completed' if self.completed else 'In Progress'}"

    @property
    def score(self):
        return sum([1 for question in self.quiz.questions.all() if question.answer.right_answer])
