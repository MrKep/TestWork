from rest_framework.routers import SimpleRouter
from .views import case_list, case_create, CaseViewSet, DelCaseViewSet
from django.urls import include, path

router = SimpleRouter()

router.register('get', CaseViewSet, basename='case')

urlpatterns = [
    path('records/all/', case_list, name='case_list'),
    path('records/', include(router.urls)),
    path('records/create/', case_create, name='case_create'),
    path('records/delete', DelCaseViewSet.as_view()),
]
