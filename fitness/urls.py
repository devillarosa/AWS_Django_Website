from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .api.views import ExerciseNameListView, ExerciseCreateView, ExerciseDetailsView, WorkoutCreateView, WorkoutDetailsView
import views

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

    # api/exercisename/
    url(r'^api/exercisename/$', ExerciseNameListView.as_view(), name='exercise_name'),

    # api/exercise/
    url(r'^api/exercise/$', ExerciseCreateView.as_view(), name='create_exercise'),

    # api/exercise/id
    url(r'^api/exercise/(?P<pk>[0-9]+)/$', ExerciseDetailsView.as_view(), name='details_exercise'),

    # api/workout/
    url(r'^api/workout/$', WorkoutCreateView.as_view(), name='create_workout'),

    # api/workout/id
    url(r'^api/workout/(?P<pk>[0-9]+)/$', WorkoutDetailsView.as_view(), name='details_workout'),

    ]

urlpatterns = format_suffix_patterns(urlpatterns)
