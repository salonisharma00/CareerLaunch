
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import AptitudeQuestion, TestResult, Company, CodingQuestion, CodingAttempt, TechnicalQuestion

def home(request):
    companies = Company.objects.all()

    return render(
        request,
        'placement/home.html',
        {
            'companies': companies
        }
    )


def register(request):

    if request.method == 'POST':

        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'placement/register.html', {
                'error': 'Passwords do not match.'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'placement/register.html', {
                'error': 'Username already exists.'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.first_name = full_name
        user.save()

        return redirect('login')

    return render(request, 'placement/register.html')


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        return render(request, 'placement/login.html', {
            'error': 'Invalid username or password.'
        })

    return render(request, 'placement/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def dashboard(request):

    results = TestResult.objects.filter(
        user=request.user
    ).order_by('-created_at')

    companies_prepared = Company.objects.count()

    tests_completed = results.count()

    best_percentage = 0

    if results.exists():
        best_percentage = max(
            result.percentage for result in results
        )

    average_percentage = 0
    overall_preparation = 0

    if results.exists():
        average_percentage = sum(
            result.percentage for result in results
        ) / tests_completed

        overall_preparation = round(average_percentage)

    # Aptitude category performance

    quantitative_results = results.filter(
        category='quantitative'
    )

    logical_results = results.filter(
        category='logical'
    )

    verbal_results = results.filter(
        category='verbal'
    )

    quantitative_average = 0
    logical_average = 0
    verbal_average = 0

    if quantitative_results.exists():
        quantitative_average = round(
            sum(
                result.percentage
                for result in quantitative_results
            ) / quantitative_results.count()
        )

    if logical_results.exists():
        logical_average = round(
            sum(
                result.percentage
                for result in logical_results
            ) / logical_results.count()
        )

    if verbal_results.exists():
        verbal_average = round(
            sum(
                result.percentage
                for result in verbal_results
            ) / verbal_results.count()
        )

          # Performance Insights

    category_scores = {
        'Quantitative Aptitude': quantitative_average,
        'Logical Reasoning': logical_average,
        'Verbal Ability': verbal_average,
    }

    attempted_categories = {
        category: score
        for category, score in category_scores.items()
        if score > 0
    }

    strongest_area = None
    weakest_area = None
    recommendation = None

    if attempted_categories:
        strongest_area = max(
            attempted_categories,
            key=attempted_categories.get
        )

        weakest_area = min(
            attempted_categories,
            key=attempted_categories.get
        )

        if weakest_area == strongest_area:
            recommendation = (
                f'Keep practicing {strongest_area} '
                'to maintain your performance.'
            )
        else:
            recommendation = (
                f'Focus more on {weakest_area} '
                'to improve your placement readiness.'
            )

    else:
        recommendation = (
            'Start an aptitude practice test to '
            'identify your strongest and weakest areas.'
        )
       # Coding statistics

    coding_attempts = CodingAttempt.objects.filter(
        user=request.user
    )

    coding_attempts_count = coding_attempts.count()

    coding_correct = coding_attempts.filter(
        is_correct=True
    ).count()

    coding_accuracy = 0

    if coding_attempts_count > 0:
        coding_accuracy = round(
            (coding_correct / coding_attempts_count) * 100
        )

    recent_coding_attempts = coding_attempts.select_related(
        'question'
    ).order_by('-attempted_at')[:5]


    context = {
        'tests_completed': tests_completed,
        'best_percentage': round(best_percentage),
        'average_percentage': round(average_percentage),
        'overall_preparation': overall_preparation,
        'companies_prepared': companies_prepared,
        'recent_results': results[:5],

           'quantitative_average': quantitative_average,
            'logical_average': logical_average,
            'verbal_average': verbal_average,

            'strongest_area': strongest_area,
            'weakest_area': weakest_area,
            'recommendation': recommendation,

        'coding_attempts_count': coding_attempts_count,
        'coding_correct': coding_correct,
        'coding_accuracy': coding_accuracy,
        'recent_coding_attempts': recent_coding_attempts,
    }

    return render(
        request,
        'placement/dashboard.html',
        context
    )

@login_required
def aptitude(request):
    return render(request, 'placement/aptitude.html')

@login_required
def practice(request):

    category = request.GET.get('category', 'all')
    difficulty = request.GET.get('difficulty', 'all')

    questions = AptitudeQuestion.objects.all()

    if category != 'all':
        questions = questions.filter(category=category)

    if difficulty != 'all':
        questions = questions.filter(difficulty=difficulty)

    score = None
    total = questions.count()

    if request.method == 'POST':

        score = 0

        for question in questions:

            selected_answer = request.POST.get(
                f'question_{question.id}'
            )

            if selected_answer == question.correct_answer:
                score += 1

        percentage = 0

        if total > 0:
            percentage = (score / total) * 100

        TestResult.objects.create(
            user=request.user,
            category=category,
            difficulty=difficulty,
            score=score,
            total=total,
            percentage=percentage
        )

    return render(request, 'placement/practice.html', {
        'questions': questions,
        'score': score,
        'total': total,
        'category': category,
        'difficulty': difficulty
    })
@login_required
def companies(request):

    companies = Company.objects.all().order_by('name')

    return render(
        request,
        'placement/companies.html',
        {
            'companies': companies
        }
    )
@login_required
def company_detail(request, company_id):

    company = Company.objects.get(id=company_id)

    return render(
        request,
        'placement/company_detail.html',
        {
            'company': company
        }
    )
@login_required
def coding(request):

    coding_questions = CodingQuestion.objects.all().order_by('difficulty', 'title')

    return render(
        request,
        'placement/coding.html',
        {
            'coding_questions': coding_questions
        }
    )
@login_required
def coding_challenge(request, question_id):

    question = CodingQuestion.objects.get(
        id=question_id
    )

    result = None

    if request.method == 'POST':

        submitted_answer = request.POST.get(
            'code',
            ''
        ).strip()

        expected_answer = question.expected_answer.strip()

        if submitted_answer == expected_answer:
            result = 'correct'
            is_correct = True
        else:
            result = 'incorrect'
            is_correct = False

        CodingAttempt.objects.create(
            user=request.user,
            question=question,
            submitted_answer=submitted_answer,
            is_correct=is_correct
        )

    return render(
        request,
        'placement/coding_challenge.html',
        {
            'question': question,
            'result': result
        }
    )
@login_required
def technical(request):

    questions = TechnicalQuestion.objects.all()

    return render(
        request,
        'placement/technical.html',
        {
            'questions': questions
        }
    )