from . import views
from django.urls import path

urlpatterns = [
    path('home', views.home, name='home'),
    path('dwnld', views.dwnld, name='dwnld'),
    path('business', views.business, name='business'),
    path('products/<int:id>', views.products, name='products'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('team', views.team, name='team'),
    path('agriculture', views.agriculture, name='agriculture'),
    path('manufacture', views.manufacture, name='manufacture'),
    path('contact', views.contact, name='contact'),
    path('faq', views.faq, name='faq'),
    path('gallery', views.gallery, name='gallery'),
    path('check', views.check, name='check'),
    path('branches', views.branches, name='branches'),
    path('viewproduct/<int:id>', views.viewproduct, name='viewproduct'),
    path('review', views.review, name='review'),
    path('upcoming', views.upcoming, name='upcoming'),
    path('underconstruction', views.underconstruction, name='underconstruction'),
    path('register',views.register,name='register'),

    path('cancel_policy',views.cancel_policy,name='cancel_policy'),
    path('privacy_policy',views.privacy_policy,name='privacy_policy'),
    path('prdt_shipping',views.prdt_shipping,name='prdt_shipping'),
    path('terms_condition',views.terms_condition,name='terms_condition'),

    path('offers',views.offers,name='offers'),
    path('career',views.career,name='career'),
    path('applyJob',views.applyJob,name='applyJob'),

    path('training',views.training,name='training'),
    path('trainer/',views.trainer,name='trainer'),
    path('add/session',views.add_session,name='add_session'),
    path('edit/session/<int:id>', views.edit_session, name='edit_session'), 


    path('delete/<int:id>/', views.delete_session, name='delete_session'),
]
