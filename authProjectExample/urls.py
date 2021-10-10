from django.contrib                 import admin
from django.urls                    import path
from authAppExample                 import views  as authAppViews
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('admin/',                                  admin.site.urls),  # use defaul Djando Admin
    path('login/',                                  TokenObtainPairView.as_view()), # use credentials to return tokens
    path('refresh/',                                TokenRefreshView.as_view()), # generate new access token
    path('user/',                                   authAppViews.UserCreateView.as_view()), # create a new user
    path('user/<int:pk>/',                          authAppViews.UserDetailView.as_view()), # check info for an specific user based on id(pk)
]