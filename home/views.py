import os
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from formtools.wizard.views import SessionWizardView
from .models import Question, Unit, Department, Transactional, \
    Question, CustomUser, Rating
from .forms import QuestionForm, UnitForm, DepartmentForm, UserForm, \
    Page1Form, Page2Form, Page3Form, Page4Form, Page5Form, \
    ClientSurveyForm, RatingForm

User = get_user_model()


def dashboard_view(request):
    return render(request, 'dashboard.html')


def manage_surveys_view(request):
    return render(request, 'manage_surveys.html')


def feedback_view(request):
    return render(request, 'feedback.html')


# Users
def user_create(request):
    if request.method == 'POST':
        print("POST data:", request.POST)
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            print("Cleaned data:", form.cleaned_data)
            user = form.save(commit=False)
            user.save()  # Save first to ensure `id` is assigned
            if 'picture' in request.FILES:
                user.picture = request.FILES['picture']
                user.save()  # Save again to store the file with the custom name
            return redirect('home:user_list')
        else:
            print(form.errors)
    else:
        form = UserForm()
    return render(request, 'users/user_form.html', {'form': form})


def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            if form.cleaned_data["password"]:
                user.password = make_password(form.cleaned_data["password"])

            if 'picture' in request.FILES:
                # Delete the old picture file if it exists
                if user.picture:
                    old_picture_path = user.picture.path
                    if os.path.isfile(old_picture_path):
                        os.remove(old_picture_path)

                # Assign the new picture
                user.picture = request.FILES['picture']

            # Save the user with the new picture
            user.save()
            return redirect('home:user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form, 'user': user})


def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('home:user_list')
    return render(request, 'users/user_confirm_delete.html', {'user': user})


def user_list(request):
    users = User.objects.all()
    if request.headers.get('HX-Request'):
        return render(request, 'users/user_list.html', {'users': users})
    return render(request, 'users/user_list.html', {'users': users})


def user_create1(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            user = form.save(commit=False)
            if form.cleaned_data["password"]:
                user.password = make_password(form.cleaned_data["password"])
            user.save()
            return render(request, 'users/user_row.html', {'user': user})
        else:
            print(form.errors)
    else:
        form = UserForm()
    return render(request, 'users/user_form.html', {'form': form})


def user_update1(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            if form.cleaned_data["password"]:
                user.password = make_password(form.cleaned_data["password"])
            user.save()
            return render(request, 'users/user_row.html', {'user': user})
    else:
        form = UserForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form})


@require_http_methods(['DELETE'])
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return HttpResponse(status=200)


# Unit Views
# def unit_list(request):
#     print("1")
#     units = Unit.objects.all()
#     return render(request, 'units/unit_list.html', {'units': units})
def unit_list(request):
    units = Unit.objects.all()
    # Check if it's an HTMX request
    if request.headers.get('HX-Request'):
        return render(request, 'units/unit_list_partial.html', {'units': units})
    return render(request, 'units/unit_list.html', {'units': units})


def unit_create1(request):
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            unit = form.save()
            return render(request, 'units/unit_row.html',
                          {'unit': unit})
    else:
        form = UnitForm()
    return render(request, 'units/unit_form.html', {'form': form})


def unit_update(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    if request.method == 'POST':
        form = UnitForm(request.POST, instance=unit)
        if form.is_valid():
            unit = form.save()
            return render(request, 'units/unit_row.html',
                          {'unit': unit})
    else:
        form = UnitForm(instance=unit)
    return render(request, 'units/unit_form.html', {'form': form})


@require_http_methods(['DELETE'])
def unit_delete(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    unit.delete()
    return HttpResponse(status=200)

# def unit_delete(request, pk):
#     unit = get_object_or_404(Unit, pk=pk)
#     if request.method == 'POST':
#         unit.delete()
#         return JsonResponse({'success': True})
#     return render(request, 'units/unit_confirm_delete.html', {'unit': unit})


def department_list(request):
    departments = Department.objects.all()
    # Check if it's an HTMX request
    if request.headers.get('HX-Request'):
        return render(request, 'departments/department_list_partial.html', {'departments': departments})
    return render(request, 'departments/department_list.html', {'departments': departments})


def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save()
            return render(request, 'departments/department_row.html',
                          {'department': department, 'success': True})
    else:
        form = DepartmentForm()
    return render(request, 'departments/department_form.html', {'form': form})


def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            department = form.save()
            return render(request, 'departments/department_row.html', {'department': department})
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'departments/department_form.html', {'form': form})


@require_http_methods(['DELETE'])
def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    department.delete()
    return HttpResponse(status=200)


# Questions
def question_list(request):
    questions = Question.objects.all()
    # Check if it's an HTMX request
    if request.headers.get('HX-Request'):
        return render(request, 'questions/question_list_partial.html', {'questions': questions})
    return render(request, 'questions/question_list.html', {'questions': questions})


def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return render(request, 'questions/question_row.html',
                          {'question': question, 'success': True})
    else:
        form = QuestionForm()
    return render(request, 'questions/question_form.html', {'form': form})


def question_update(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save()
            return render(request, 'questions/question_row.html', {'question': question})
    else:
        form = QuestionForm(instance=question)
    return render(request, 'questions/question_form.html', {'form': form})


@require_http_methods(['DELETE'])
def question_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.delete()
    return HttpResponse(status=200)


def load_survey(request, user_id):
    # user_id = request.GET.get('user_id')
    user = get_object_or_404(CustomUser, user_id=user_id)
    return render(request, 'survey_form.html', {'user': user})


# wizard
FORMS = [("page1", Page1Form), ("page2", Page2Form),
         ("page3", Page3Form), ("page4", Page4Form), ("page5", Page5Form)]
TEMPLATES = {
    "page1": "surveys/page1.html",
    "page2": "surveys/page2.html",
    "page3": "surveys/page3.html",
    "page4": "surveys/page4.html",
    "page5": "surveys/page5.html",
}


class SurveyWizard(SessionWizardView):
    form_list = FORMS
    template_name = "survey/survey_form.html"

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, form, **kwargs):
        # Capture the user_id from the URL
        context = super().get_context_data(form=form, **kwargs)
        user_id = self.kwargs.get('user_id')
        user = get_object_or_404(CustomUser, user_id=user_id)

        # Pass the user data to the context
        context['user'] = user
        return context

    def done(self, form_list, **kwargs):
        # Retrieve the user and link responses to the correct user
        user_id = self.kwargs.get('user_id')
        user = get_object_or_404(CustomUser, user_id=user_id)

        # Create a Transaction instance linked to the user
        transaction = Transactional.objects.create(user_id=user.user_id)

        # Process form data
        for form in form_list:
            # Here, save each form's data as needed
            form.save(commit=False)
            form.instance.transaction = transaction
        transaction.save()

        return render(self.request, "survey/success.html", {"transaction": transaction})


def survey_form(request, user_id):
    user = get_object_or_404(CustomUser, user_id=user_id)
    if request.method == 'POST':
        form = ClientSurveyForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            survey = form.save(commit=False)
            survey.user_id = user_id
            if request.POST.get('latitude') and request.POST.get('longitude'):
                survey.latitude = request.POST.get('latitude')
                survey.longitude = request.POST.get('longitude')
            survey.save()  # Inserts the form data, including user_id, into the database
            # Redirect to a success page or thank you page
            return redirect('home:rating_view')
        else:
            print(form.errors)
    else:
        form = ClientSurveyForm()

    sqd_statements = {
        'sqd0': "SQD0. I am satisfied with the service that I availed.",
        'sqd1': "SQD1. I spent a reasonable amount of time for my transaction.",
        'sqd2': "SQD2. The office followed the transaction's requirements and steps based on the information provided.",
        'sqd3': "SQD3. The steps (including payment) I needed to do for my transaction were easy and simple.",
        'sqd4': "SQD4. I easily found information about my transaction from the office or its website.",
        'sqd5': "SQD5. I paid a reasonable amount of fees for my transaction. (if service was free, mark 'N/A' column)",
        'sqd6': "SQD6. I feel the office was fair to everyone, or 'walang palakasan', during my transaction.",
        'sqd7': "SQD7. I was treated courteously by the staff, and (if asked for help) the staff was helpful.",
        'sqd8': "SQD8. I got what I needed from the government office, or (if denied) denial of request was sufficiently explained to me.",
    }
    # Attach statements to form fields
    for field_name, field in form.fields.items():
        if field_name in sqd_statements:
            field.statement = sqd_statements[field_name]

    return render(request, 'survey_form.html', {'form': form, 'user': user})


def survey_success(request):
    return render(request, 'survey_success.html')


def rating_view(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            # if request.user:
            #     rating = form.save(commit=False)
            #     rating.user = request.user  # Assign the current user to the rating
            #     rating.save()
            form.save()
            # Redirect to a success or thank you page
            return redirect('home:survey_success')
    else:
        form = RatingForm()

    return render(request, 'rating_form.html', {'form': form})
