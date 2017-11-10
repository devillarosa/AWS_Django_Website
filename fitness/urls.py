from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView
import views
from .api.views.user_exercise import UserExerciseView, UserExerciseDetailsView

app_name = 'fitness'

urlpatterns = [

    # Home page for user
    url(r'^home/$', views.home_page, name='home_page'),

    # Page for adding exercise
    url(r'^exercise/$', views.exercise_page, name='exercise_page'),

    # Page for logging workout
    url(r'^workout/$', views.workout_page, name='workout_page'),

    # Page for viewing history and statistics
    url(r'^history/$', views.history_page, name='history_page'),


    ### Fitness API URLS ###

    # api/userexerciselist/
    url(r'^api/userexercise/$', UserExerciseView.as_view(), name='user_exercise'),

    # api/userexercise/id
    url(r'^api/userexercise/(?P<pk>[0-9]+)/$', UserExerciseDetailsView.as_view(), name='details_user_exercise'),

    # api/workout/
#    url(r'^api/workout/$', WorkoutCreateView.as_view(), name='workout'),

    # api/workout/id
#    url(r'^api/workout/(?P<pk>[0-9]+)/$', WorkoutDetailsView.as_view(), name='details_workout'),

    ]

urlpatterns = format_suffix_patterns(urlpatterns)
