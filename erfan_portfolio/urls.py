from django.urls import path
from erfan_portfolio.views import erfan_portfolio_view

urlpatterns=[
    path('erfan/',erfan_portfolio_view,name='erfan')
]