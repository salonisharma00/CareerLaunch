from django.contrib import admin
from .models import AptitudeQuestion, TestResult, Company, CodingQuestion, CodingAttempt, TechnicalQuestion

admin.site.register(AptitudeQuestion)
admin.site.register(TestResult)
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created_at',
    )

    fields = (
        'name',
        'description',
        'eligibility',
        'skills',
        'interview_rounds',
        'preparation_tips',
    )
admin.site.register(CodingQuestion)
admin.site.register(CodingAttempt)
admin.site.register(TechnicalQuestion)