from django.urls import path
from . import views
app_name = "chat"
urlpatterns = [path("", views.lista, name="lista"), path("<int:usuario_id>/", views.conversa, name="conversa")]
