from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .api.views import ExerciseNameCreateView, ExerciseNameDetailsView
from .api.views import ExerciseCreateView, ExerciseDetailsView
from .api.views import WorkoutCreateView, WorkoutDetailsView

urlpatterns = [

    # /exercisename/
    url(r'api/exercisename/$', ExerciseNameCreateView.as_view(), name='create_exercisename'),

    # /exercisename/id
    url(r'api/exercisename/(?P<pk>[0-9]+)/$', ExerciseNameDetailsView.as_view(), name='details_exercisename'),

    # /exercise/
    url(r'api/exercise/$', ExerciseCreateView.as_view(), name='create_exercise'),

    # /exercise/id
    url(r'api/exercise/(?P<pk>[0-9]+)/$', ExerciseDetailsView.as_view(), name='details_exercise'),

    # /workout/
    url(r'api/workout/$', WorkoutCreateView.as_view(), name='create_workout'),

    # /workout/id
    url(r'api/workout/(?P<pk>[0-9]+)/$', WorkoutDetailsView.as_view(), name='details_workout'),

    ]

urlpatterns = format_suffix_patterns(urlpatterns)
