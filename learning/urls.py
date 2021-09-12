from django.urls import path, include
from . import views

app_name = 'learning'

urlpatterns = [
    path('', views.TopPage.as_view(), name='toppage'),
    path('index', views.Index.as_view(), name='index'),
    path('card_create',views.CardCreate.as_view(),name="card_create"),
    path('card_detail/<int:pk>', views.CardDetail.as_view(), name='card_detail'),
    path('card_update/<int:pk>', views.CardUpdate.as_view(), name="card_update"),
    path('card_delete/<int:pk>',views.CardDelete.as_view(),name="card_delete"),
    path('card_list',views.CardList.as_view(),name="card_list"),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('signup', views.SignUp.as_view(), name='signup'),
    path('category_list', views.CategoryList.as_view(), name='category_list'),
    path('category_detail/<str:name_en>',
         views.CategoryDetail.as_view(), name='category_detail'),
    # path('search', views.Search, name='search'),
]

