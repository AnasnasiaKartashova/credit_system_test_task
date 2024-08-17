from django.urls import path
from credit_system.views.get_makers_list_view import MakersListView


urlpatterns = [
    path(
        "get_makers_list/<int:contract_id>/",
        MakersListView.as_view(),
        name="makers_list",
    ),
]
