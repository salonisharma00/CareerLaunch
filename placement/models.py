from django.db import models
from django.contrib.auth.models import User


class AptitudeQuestion(models.Model):

    CATEGORY_CHOICES = [
        ('quantitative', 'Quantitative Aptitude'),
        ('logical', 'Logical Reasoning'),
        ('verbal', 'Verbal Ability'),
    ]

    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    question = models.TextField()

    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)

    correct_answer = models.CharField(max_length=1)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class TestResult(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    category = models.CharField(max_length=20)

    difficulty = models.CharField(max_length=10)

    score = models.IntegerField()

    total = models.IntegerField()

    percentage = models.FloatField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.score}/{self.total}"


class Company(models.Model):

    name = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    eligibility = models.TextField(blank=True)

    skills = models.TextField(blank=True)

    interview_rounds = models.TextField(blank=True)

    preparation_tips = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name
        
class CodingQuestion(models.Model):

    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('java', 'Java'),
        ('cpp', 'C++'),
    ]

    title = models.CharField(max_length=200)

    description = models.TextField()

    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES
    )

    language = models.CharField(
        max_length=10,
        choices=LANGUAGE_CHOICES
    )

    example_input = models.TextField(blank=True)

    example_output = models.TextField(blank=True)

    expected_answer = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
class CodingAttempt(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    question = models.ForeignKey(
        CodingQuestion,
        on_delete=models.CASCADE
    )

    submitted_answer = models.TextField()

    is_correct = models.BooleanField(
        default=False
    )

    attempted_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.question.title}"
class TechnicalQuestion(models.Model):

    CATEGORY_CHOICES = [
        ('dbms', 'DBMS'),
        ('oops', 'OOP'),
        ('os', 'Operating Systems'),
        ('cn', 'Computer Networks'),
        ('general', 'General Technical'),
    ]

    question = models.TextField()

    answer = models.TextField()

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    difficulty = models.CharField(
        max_length=10,
        choices=[
            ('easy', 'Easy'),
            ('medium', 'Medium'),
            ('hard', 'Hard'),
        ]
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.question