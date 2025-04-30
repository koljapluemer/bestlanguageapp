from django.urls import path, include

urlpatterns = [
    path('tool/', include('app.router.admin.tool')),
] 