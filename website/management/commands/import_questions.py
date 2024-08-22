import csv
from django.core.management.base import BaseCommand
from website.models import Quiz, Question


class Command(BaseCommand):
    help = 'Import questions and answers from a CSV file'

    def handle(self, *args, **kwargs):
        file_path = 'data.csv'
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    quiz_id = row['quiz_id']
                    quiz = Quiz.objects.get(id=quiz_id)
                    question_title = row['question_title']
                    correct_answer = row['correct_answer']

                    question = Question.objects.create(
                        quiz=quiz,
                        title=question_title,
                        correct_answer=correct_answer
                    )
                    self.stdout.write(self.style.SUCCESS(f'Question "{question_title}" imported successfully for quiz ID {quiz_id}.'))
                except Quiz.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Quiz with ID {quiz_id} does not exist.'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error importing question: {e}'))
