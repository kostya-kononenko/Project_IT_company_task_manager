from django.urls import path

from .views import index, TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, \
    TaskWorkerUpdateView, WorkerListView, WorkerDetailView, WorkerCreateView, WorkerDeleteView, WorkerUpdateView

urlpatterns = [
    path("", index, name="index"),
    path(
        "tasks/",
        TaskListView.as_view(),
        name="task-list"),

    path("tasks/<int:pk>/",
         TaskDetailView.as_view(),
         name="task-detail"),

    path("tasks/create/",
         TaskCreateView.as_view(),
         name="task-create"),

    path("tasks/<int:pk>/update/",
         TaskUpdateView.as_view(),
         name="task-update"),

    path("tasks/<int:pk>/delete/",
         TaskDeleteView.as_view(),
         name="task-delete"),

    path(
        "cars/<int:pk>/assign/",
        TaskWorkerUpdateView.as_view(),
        name="task-worker-update"
    ),

    path("workers/",
         WorkerListView.as_view(),
         name="worker-list"),

    path(
        "workers/<int:pk>/",
        WorkerDetailView.as_view(),
        name="worker-detail"
    ),

    path("workers/create",
         WorkerCreateView.as_view(),
         name="worker-create"),

    path("workers/<int:pk>/delete/",
         WorkerDeleteView.as_view(),
         name="worker-delete"),

    path("workers/<int:pk>/update/",
         WorkerUpdateView.as_view(),
         name="worker-update"),


]

app_name = "task_manager"
