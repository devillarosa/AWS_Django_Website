from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .api.views.exercise import ExerciseView, ExerciseDetailsView
from .api.views.user_exercise import UserExerciseView, UserExerciseDetailsView
from .api.views.workout import WorkoutView, WorkoutDetailsView

app_name = 'fitness'

urlpatterns = [

    # api/userexerciselist/
    url(r'^api/exercise/$', ExerciseView.as_view(), name='exercise'),

    # api/userexercise/id
    url(r'^api/exercise/(?P<pk>[0-9]+)/$', ExerciseDetailsView.as_view(), name='details_exercise'),

    # api/userexerciselist/
    url(r'^api/userexercise/$', UserExerciseView.as_view(), name='user_exercise'),

    # api/userexercise/id
    url(r'^api/userexercise/(?P<pk>[0-9]+)/$', UserExerciseDetailsView.as_view(), name='details_user_exercise'),

    # api/workout/
    url(r'^api/workout/$', WorkoutView.as_view(), name='workout'),

    # api/workout/id
    url(r'^api/workout/(?P<pk>[0-9]+)/$', WorkoutDetailsView.as_view(), name='details_workout'),

    ]

urlpatterns = format_suffix_patterns(urlpatterns)
