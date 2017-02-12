from django.conf.urls import url, include
from rest_framework_nested.routers import SimpleRouter, DefaultRouter, NestedSimpleRouter

from onemanager.score.views import ScoreViewSet, ScoreDataViewSet

root_router = DefaultRouter()
root_router.register('score', ScoreViewSet, 'score')
root_router.register('score-data', ScoreDataViewSet, 'score-data')

score_router = SimpleRouter()
score_router.register('score', ScoreViewSet, base_name='list-score')
score_data_router = NestedSimpleRouter(score_router, 'score', lookup='score')
score_data_router.register('data', ScoreDataViewSet, base_name='list-score-data')

urlpatterns = [
    url(r'', include(root_router.urls)),
    url(r'list/', include(score_router.urls)),
    url(r'list/', include(score_data_router.urls)),
]
