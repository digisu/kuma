from kuma.core.jobs import KumaJob
from .utils import (spam_day_stats,
                    spam_dashboard_historical_stats,
                    spam_dashboard_recent_events)


class SpamDayStatsJob(KumaJob):
    """Cache spam stats for multiple days."""
    lifetime = 60 * 60 * 24 * 7
    fetch_on_miss = True
    version = 5

    def fetch(self, day):
        return spam_day_stats(day)


class SpamDashboardHistoricalStats(KumaJob):
    """Cache historical spam stats for multiple days."""
    lifetime = 60 * 60 * 24
    fetch_on_miss = False
    version = 7

    def fetch(self, end_date):
        return spam_dashboard_historical_stats(end_date=end_date)


class SpamDashboardRecentEvents(KumaJob):
    """Cache recent event data for a very short time."""
    lifetime = 60
    fetch_on_miss = True
    version = 1

    def fetch(self):
        return spam_dashboard_recent_events()
