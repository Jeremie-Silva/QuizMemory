from random import shuffle
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from website.models import Quiz, Session, Question, Answer
from django.db.models import F


class CustomLoginView(LoginView):
    template_name = "website/login.html"
    next_page = "website:quiz"


@login_required
def quiz(request):
    return render(request, "website/quiz.html", {"quiz": Quiz.objects.all()})


@login_required
def sessions(request):
    sessions = Session.objects.filter(user=request.user.profile).order_by('-start_time')  # Trie les sessions du plus récent au plus ancien
    for session in sessions:
        correct_answers_count = session.answers.filter(content__iexact=F('question__correct_answer')).count()
        session.score = f"{correct_answers_count} / {session.quiz.questions.count()}"
    return render(request, "website/sessions.html", {"sessions": sessions})


@login_required
def start(request):
    return render(request, 'website/start.html', {"quiz": Quiz.objects.all()})


@login_required
def new_session(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    session, created = Session.objects.get_or_create(user=request.user.profile, quiz=quiz, completed=False)
    if created:
        all_questions = list(quiz.questions.all())
        shuffle(all_questions)
        request.session[f'shuffled_questions_{session.id}'] = [q.id for q in all_questions]
        request.session[f'current_question_index_{session.id}'] = 0
    question_ids = request.session.get(f'shuffled_questions_{session.id}', [])
    current_index = request.session.get(f'current_question_index_{session.id}', 0)
    if current_index < len(question_ids):
        current_question = Question.objects.get(id=question_ids[current_index])
    else:
        current_question = None
    if not current_question:
        session.completed = True
        session.save()
        request.session.pop(f'shuffled_questions_{session.id}', None)
        request.session.pop(f'current_question_index_{session.id}', None)
        return redirect("website:session_details", session_id=session.id)
    if request.method == "POST":
        user_answer = request.POST.get("answer")
        if user_answer:
            Answer.objects.create(session=session, question=current_question, content=user_answer)
            request.session[f'current_question_index_{session.id}'] += 1
            return redirect("website:new_session", quiz_id=quiz.id)
    return render(request, "website/new_session.html", {"quiz": quiz, "question": current_question, 'session': session})


@login_required
def session_details(request, session_id):
    session = get_object_or_404(Session, id=session_id, user=request.user.profile)
    correct_answers_count = session.answers.filter(content__iexact=F('question__correct_answer')).count()
    total_questions = session.quiz.questions.count()
    session_score = f"{correct_answers_count} / {total_questions}"
    questions_and_answers = []
    for question in session.quiz.questions.all():
        user_answer = session.answers.filter(question=question).first()
        questions_and_answers.append({
            "question": question,
            "user_answer": user_answer,
            "correct_answer": question.correct_answer
        })
    return render(request, "website/session_details.html", {
        "session": session,
        "session_score": session_score,
        "questions_and_answers": questions_and_answers
    })
