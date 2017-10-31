from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import index
from .views import UserCreateView, UserDetailsView
from .views import ExerciseNameCreateView, ExerciseNameDetailsView
from .views import ExerciseCreateView, ExerciseDetailsView
from .views import WorkoutCreateView, WorkoutDetailsView

urlpatterns = [
    # /
    url(r'^$', index, name='index'),
    
    # /user/
    url(r'user/$', UserCreateView.as_view(), name='create_user'),

    # /user/id
    url(r'user/(?P<pk>[0-9]+)/$', UserDetailsView.as_view(), name='details_user'),

    # /exercisename/
    url(r'exercisename/$', ExerciseNameCreateView.as_view(), name='create_exercise'),

    # /exercisename/id
    url(r'exercisename/(?P<pk>[0-9]+)/$', ExerciseNameDetailsView.as_view(), name='details_exercise'),

    # /exercise/
    url(r'exercise/$', ExerciseCreateView.as_view(), name='create_exercise'),

    # /exercise/id
    url(r'exercise/(?P<pk>[0-9]+)/$', ExerciseDetailsView.as_view(), name='details_exercise'),

    # /workout/
    url(r'workout/$', WorkoutCreateView.as_view(), name='create_workout'),

    # /workout/id
    url(r'workout/(?P<pk>[0-9]+)/$', WorkoutDetailsView.as_view(), name='details_workout'),

    ]

urlpatterns = format_suffix_patterns(urlpatterns)
