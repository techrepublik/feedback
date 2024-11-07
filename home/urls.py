from django.urls import path
from .views import SurveyWizard
from .forms import Page1Form, Page2Form, Page3Form, Page4Form, Page5Form
from . import views

# Define the form list and associate each step with a form
FORMS = [
    ("page1", Page1Form),
    ("page2", Page2Form),
    ("page3", Page3Form),
    ("page4", Page4Form),
    ("page5", Page5Form),
]

app_name = 'home'
urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    #     path('survey/<str:user_id>/', SurveyWizard.as_view(FORMS), name='survey_wizard'),
    path('survey/success/', views.survey_success,
         name='survey_success'),  # Add a success view if needed
    path('rate/', views.rating_view, name='rating_view'),
    path('survey/<str:user_id>/', views.survey_form, name='survey_form'),
    #     path('survey/', views.survey_form, name='survey_form'),


    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:pk>/update/', views.user_update, name='user_update'),
    path('users/<int:pk>/delete/', views.user_delete, name='user_delete'),

    path('units/', views.unit_list, name='unit_list'),
    path('units/create/', views.unit_create1, name='unit_create'),
    path('units/<int:pk>/update/', views.unit_update, name='unit_update'),
    path('units/<int:pk>/delete/', views.unit_delete, name='unit_delete'),

    path('departments/', views.department_list, name='department_list'),
    path('departments/create/', views.department_create,
         name='department_create'),
    path('departments/<int:pk>/update/',
         views.department_update, name='department_update'),
    path('departments/<int:pk>/delete/',
         views.department_delete, name='department_delete'),

    path('questions/', views.question_list, name='question_list'),
    path('questions/create/', views.question_create,
         name='question_create'),
    path('questions/<int:pk>/update/',
         views.question_update, name='question_update'),
    path('questions/<int:pk>/delete/',
         views.question_delete, name='question_delete'),
]
