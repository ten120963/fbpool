from django.urls import path
#from . import views
#from .views import HomeView, AddPickView, UpdatePickView, DeletePickView, WeekView, WeekListView, TeamView, TeamListView, AuthorView
from .views import HomeView, AddPickView, UpdatePickView, DeletePickView, WeekView, TeamView, AuthorView, WinnerView, WinnerListView, CalculateView, StatusView, WinnerWeekView

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    #path('', StatusView.as_view(), name="home"),
    #path('week/<int:pk>', WeekDetailView.as_view(), name="week_detail"),
    path('add_pick/', AddPickView.as_view(), name="add_pick"),
    path('pick/edit/<int:pk>/', UpdatePickView.as_view(), name="update_pick"),
    path('pick/<int:pk>/remove', DeletePickView.as_view(), name="delete_pick"),
    path('weeks/<int:week>/', WeekView, name='week_view'),
    #path('week_list/', WeekListView, name='week_list'),
    path('teams/<str:team>/', TeamView, name='team_view'),
    #path('team_list/', TeamListView, name='team_list'),
    path('player/<str:author>/', AuthorView, name='author_view'),   
    path('winners/', WinnerView.as_view(), name="add_winners"), 
    path('winner_list/', WinnerListView.as_view(), name="winner_list"), 
    path('calculate/', CalculateView, name='calculate'),
    path('status/', StatusView.as_view(), name="status"),
    path('winner_week/', WinnerWeekView, name="winner_week"),
]
