"""Shared README timestamps; rendering never changes the recorded values."""
from datetime import datetime, timedelta, timezone

BEIJING = timezone(timedelta(hours=8))


def format_readme_time(value):
    return datetime.fromisoformat(value).astimezone(BEIJING).strftime('%Y-%m-%d %H:%M:%S')


def readme_dates(c, english=False):
    added = format_readme_time(c['readme_added_at'])
    updated = format_readme_time(c['readme_updated_at'])
    if english:
        return f'**Added to README:** {added}<br>**Content updated:** {updated}'
    return f'**收录到 README：** {added}<br>**内容更新：** {updated}'
