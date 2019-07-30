from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from tasks import views

urlpatterns = [
    path('', views.Index, name='index'),
    #path("", views.index, name="cat.jpg"),
    #path("list/",
         #views.tasks_by_tag,
         #name="list"),
    #path("list/tag/<slug:tag_slug>",
         #views.tasks_by_tag,
         #name="list_by_tag"),
    path("tasks/", include("tasks.urls", namespace="tasks")),
    path("accounts/", include("accounts.urls")),
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
