from django.urls import path
# from .views import sign_up_by_html
from .views import sign_up_by_django

urlpatterns = [
    # path('', sign_up_by_html),
    path('django_sign_up/', sign_up_by_django),

]