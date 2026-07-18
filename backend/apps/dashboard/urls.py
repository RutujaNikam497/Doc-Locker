from django.urls import path

from .views import (
    DashboardSummaryView,
    UpcomingExpiryView,
     MonthlyActionView
)

urlpatterns = [

    path(
        "",
        DashboardSummaryView.as_view(),
        name="dashboard-summary"
    ),

    path(
        "upcoming/",
        UpcomingExpiryView.as_view(),
        name="upcoming-expiry"
    ),

    path(
        "monthly-actions/",
        MonthlyActionView.as_view(),
        name="monthly-actions",
    ),

]