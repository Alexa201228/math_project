from django.urls import path

from . import views

urlpatterns = [
    path('', views.math, name="math"),
    path('razvitie-ponyatya-o-chisle.html/', views.ponyatia_o_chisle, name="ponyatia_o_chisle"),
    path('korni-stepeni-logarifmi.html/', views.korni, name="korni"),
    path('priamie-i-ploskosti-v-prostranstve.html/', views.priamie, name="priamie"),
    path('elementi-kombinatoriki.html/', views.kombinatorica, name="kombinatorica"),
    path('coordinati-i-vectori.html/', views.coordinati, name="coordinati"),
    path('osnovi-trigonometrii.html/', views.trigonometria, name="trigonometria"),
    path('functions-ich-grafiki-i-svoistva.html/', views.functions, name="functions"),
    path('mnogogranniki-i-kruglie-tela.html/', views.mnogogranniki, name="mnogogranniki"),
    path('nachala-matanaliza.html/', views.matan, name="matan"),
    path('integral-i-ego-primenenie.html/', views.integral, name="integral"),
    path('elementi-teorii-veroyatnostey-i-matstat.html/', views.teorver, name="teorver"),
    path('uravnenia-i-neravenstva.html/', views.neravenstva, name="neravenstva"),
]