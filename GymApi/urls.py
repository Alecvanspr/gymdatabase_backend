from GymApi import views
from GymApi.views import set, location, session, equipment, exercise, set, muscleGroup, training ,user
from django.urls import path

urlpatterns = [
    #Set
    path('sets/', set.SetViewSet.as_view({'get': 'list'})),
    path('set/<int:id>/', set.SetViewSet.as_view({'get': 'get'})),
    path('set/', set.SetViewSet.as_view({'post': 'create'})),
    path('sessionset/<int:id>/', set.SetPerSession.as_view({'get': 'list'})),

    #Session
    path('session/', session.SessionViewSet.as_view({'get': 'list'})),
    path('session/<int:id>/', session.SessionViewSet.as_view({'get': 'get'})),
    path('session/', session.SessionViewSet.as_view({'post': 'create'})),
    path('sessionlist/<int:user_id>/', session.SessionViewSet.as_view({'get': 'get_list'})),
    
    #MuscleGroup
    path('muscle_group/', muscleGroup.MuscleGroupViewSet.as_view({'get': 'list'})),

    #Exercise
    path('exercises/', exercise.ExerciseViewSet.as_view({'get': 'list'})),

    #TrainDay
    path('trainings/', training.TraindayViewSet.as_view({'get': 'list'})),
    path('training/<int:id>/', training.TraindayViewSet.as_view({'get': 'get'})),
    path('training/', training.TraindayViewSet.as_view({'post': 'create'})),

    #Equipment
    path('equipment/', equipment.EquipmentViewSet.as_view({'get': 'list'})),

    #Location
    path('location/', location.LocationViewSet.as_view({'get': 'list'})),

    #Login
    path('login/', user.login, name='login'),
    path('logout/', user.logout, name='logout'),
    path('register/', user.register, name='register'),
]



