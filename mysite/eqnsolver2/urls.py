from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),  # 127.0.0.1:8000/eqnsolver
    path('solve_2var', views.solve_2var, name="solve_2var"),  # 127.0.0.1:8000/eqnsolver/solve_2var
    path('results_2var', views.results_2var, name="results_2var"),  # 127.0.0.1:8000/eqnsolver/results_2var
    path('solve_3var', views.solve_3var, name="solve_3var"),  # 127.0.0.1:8000/eqnsolver/solve_3var
    path('results_3var', views.results_3var, name="results_3var"),  # 127.0.0.1:8000/eqnsolver/results_3var
]