from django.shortcuts import render, redirect
from .models import *

def index(request):
    feedbacks = CustomerFeedback.objects.all()
    return render(request, 'surveys.html', {'feedbacks': feedbacks})

def customer_feedback(request, id):
    feedback = CustomerFeedback.objects.get(id=id)
    if request.method == "POST":
        for question in feedback.question.all():  # Corrected from feedback.questions.all() to feedback.question.all()
            response_text = request.POST.get(f"response_{question.id}")
            selected_question_ids = request.POST.getlist(f"options_{question.id}")
            print(response_text)
            print(selected_question_ids)

            response = CustomerResponse.objects.create(
                feedback=feedback,
                question=question,
                response_text=response_text if question.question_type in ["Text", "Big Text"] else None
            )

            if selected_question_ids:
                selected_questions = Options.objects.filter(id__in=selected_question_ids)
                response.selected_option.set(selected_questions)
                print(selected_questions)
                print(selected_question_ids)

        return redirect('/thankyou/')
    
    return render(request, 'feedback.html', {'questions': feedback.question.all()})  # Same correction here


def thankyou(request):
    return render(request, 'thankyou.html')