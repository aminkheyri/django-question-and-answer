from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'accounts'

api_urls = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
]

urlpatterns = [
    path('register/', views.UserRegister.as_view(), name='register'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
    path('dashboard/<str:username>/', views.UserDashboard.as_view(), name='dashboard'),
    path('api/', include(api_urls))
]


#{
#  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyNzY0MjU4MywianRpIjoiOWRmOTUyYjRhYmViNDc0MTg3OTFkMTA2Yjg3MmE1YWIiLCJ1c2VyX2lkIjoxfQ.RxnCq27NtUB0rBq9bcsoLPYFZQU-zIDQ3jTikFg-FRo",
#  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI3NTU2NDgzLCJqdGkiOiI4ZTJjMWI2NzU0ZjM0MTM4YjhkMzRiMjVjMWI4MGZjMiIsInVzZXJfaWQiOjF9.RkqkZFCFDbIkrzswpRNlMJJShODnTHufEw_Pax-D6T8"
#}
