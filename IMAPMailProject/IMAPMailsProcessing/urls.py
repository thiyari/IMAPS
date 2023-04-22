from tkinter import N
from django.urls import path
from . import views

urlpatterns = [
    path('IMAPMailsProcessing/', views.index),
    path('IMAPMailsProcessing/login/', views.login), # our-domain.com/IMAPMailsProcessing
    path('IMAPMailsProcessing/home/', views.home, name='home'),
    path('IMAPMailsProcessing/mails/', views.mails, name='mails'),
    path('IMAPMailsProcessing/subject/', views.subject, name='subject'),
    path('IMAPMailsProcessing/date/', views.date, name='date'),
    path('IMAPMailsProcessing/body/', views.body, name='body'),
    path('IMAPMailsProcessing/fromaddr/', views.fromaddr, name='fromaddr'),
    path('IMAPMailsProcessing/delete/', views.delete, name='delete'),
    path('IMAPMailsProcessing/SelectMailsDeletion/', views.SelectMailsDeletion, name='SelectMailsDeletion'),
    path('IMAPMailsProcessing/FromSearchForm/', views.FromSearchForm, name='FromSearchForm'),
    path('IMAPMailsProcessing/BodySearchForm/', views.BodySearchForm, name='BodySearchForm'),
    path('IMAPMailsProcessing/SinceDateForm/', views.SinceDateForm, name='SinceDateForm'),
    path('IMAPMailsProcessing/logout/', views.logout, name='logout')
]

