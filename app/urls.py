from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.MonthCalendar.as_view(), name='month'),
    path('month/<int:year>/<int:month>/', views.MonthCalendar.as_view(), name='month'),
    path('room/<int:year>/<int:month>/<int:day>', views.RoomView.as_view(), name='room'),
    # path('room/<int:pk>', views.StaffView.as_view(), name='staff'),
    path('calendar/<int:pk>', views.CalendarView.as_view(), name='calendar'),
    path('calendar/<int:pk>/<int:year>/<int:month>/<int:day>', views.CalendarView.as_view(), name='calendar'),
    path('booking/<int:pk>/<int:year>/<int:month>/<int:day>/<int:hour>', views.BookingView.as_view(), name='booking'),
    path('thanks', views.ThanksView.as_view(), name='thanks'),
    path('mypage/<int:pk>/', views.MyPageView.as_view(), name='mypage'),
    # path('mypage/<int:year>/<int:month>/<int:day>/', views.MyPageView.as_view(), name='mypage'),
    # path('mypage/holiday/<int:year>/<int:month>/<int:day>/<int:hour>/', views.Holiday, name='holiday'),
    # path('mypage/delete/<int:year>/<int:month>/<int:day>/<int:hour>/', views.Delete, name='delete'),
    path('mypage/delete/<int:pk>/', views.Delete, name='delete'),
]