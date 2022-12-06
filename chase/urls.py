from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from chaseapi.views import register_user, login_user, TeamView, LikeView, JerseyPostView, CommentView
from django.conf.urls import include
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'teams', TeamView, 'team')
router.register(r'likes', LikeView, 'like')
router.register(r'jerseyPosts', JerseyPostView, 'jerseyPost')
router.register(r'comments', CommentView, 'comment')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
