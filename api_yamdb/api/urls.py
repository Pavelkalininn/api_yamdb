from django.urls import path

urlpatterns = [
    # path('v1/api-token-auth/', views.obtain_auth_token),
    # path('v1/', include(router.urls)),
    path('v1/auth/signup/', ...),
    path('v1/auth/token/', ...),
    path('v1/users/', ...),
    path('v1/users/{str:username}/', ...),
    path('v1/users/me/', ...),
]
