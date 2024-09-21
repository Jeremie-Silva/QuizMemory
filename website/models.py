from django.db.models import Model, CASCADE, OneToOneField, CharField, ForeignKey, IntegerField, TextField, BooleanField, DateTimeField, URLField, ImageField
from django.contrib.auth.models import User


class UserProfile(Model):
    user = OneToOneField(User, on_delete=CASCADE, related_name="profile")
    is_staff = False

    def __str__(self):
        return self.user.username


class Quiz(Model):
    title = CharField(max_length=255)
    image_url = URLField()

    def __str__(self):
        return self.title


class Question(Model):
    title = CharField(max_length=255)
    quiz = ForeignKey(Quiz, on_delete=CASCADE, related_name="questions")
    correct_answer = CharField(max_length=255)
    image = ImageField(upload_to="question_images/", null=True, blank=True)


    def __str__(self):
        return self.title


class Session(Model):
    user = ForeignKey(UserProfile, on_delete=CASCADE, related_name="sessions")
    quiz = ForeignKey(Quiz, on_delete=CASCADE, related_name="sessions")
    start_time = DateTimeField(auto_now_add=True)
    end_time = DateTimeField(null=True, blank=True)
    completed = BooleanField(default=False)

    def __str__(self):
        return f"{self.user.user.username} - {self.quiz.title}"


class Answer(Model):
    session = ForeignKey(Session, on_delete=CASCADE, related_name="answers")
    question = ForeignKey(Question, on_delete=CASCADE, related_name="answer")
    content = CharField(max_length=255)

    def __str__(self):
        return self.content
