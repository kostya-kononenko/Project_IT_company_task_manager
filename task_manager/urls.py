from django.urls import path

from .views import index, TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, \
    TaskWorkerUpdateView, WorkerListView, WorkerDetailView, WorkerCreateView, WorkerDeleteView, WorkerUpdateView, \
    PositionListView, PositionDetailView, PositionCreateView, PositionDeleteView, PositionUpdateView, TaskTypeListView, \
    TaskTypeDetailView, TaskTypeCreateView, TaskTypeDeleteView, TaskTypeUpdateView

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

    path("positions/",
         PositionListView.as_view(),
         name="position-list"),

    path(
        "positions/<int:pk>/",
        PositionDetailView.as_view(),
        name="position-detail"
    ),

    path("positions/create",
         PositionCreateView.as_view(),
         name="position-create"),

    path("positions/<int:pk>/delete/",
         PositionDeleteView.as_view(),
         name="position-delete"),

    path("positions/<int:pk>/update/",
         PositionUpdateView.as_view(),
         name="position-update"),

    path("tasktypes/",
         TaskTypeListView.as_view(),
         name="task-types-list"),

    path(
        "tasktypes/<int:pk>/",
        TaskTypeDetailView.as_view(),
        name="task-types-detail"
    ),

    path("tasktypes/create",
         TaskTypeCreateView.as_view(),
         name="task-types-create"),

    path("tasktypes/<int:pk>/delete/",
         TaskTypeDeleteView.as_view(),
         name="task-types-delete"),

    path("tasktypes/<int:pk>/update/",
         TaskTypeUpdateView.as_view(),
         name="task-types-update"),
]

app_name = "task_manager"
