"""Shared README timestamps; rendering never changes the recorded values."""
from datetime import datetime, timedelta, timezone

BEIJING = timezone(timedelta(hours=8))


def beijing_day(value):
    return datetime.fromisoformat(value).astimezone(BEIJING).date().isoformat()


def case_day(c):
    return beijing_day(c['readme_added_at'])


def latest_review_day(d):
    update = d.get('latest_update')
    return beijing_day(update['reviewed_at']) if update else d['collected_on']


def case_review_day(c, d):
    days = [beijing_day(u['reviewed_at']) for u in d.get('updates', [])
            if c['slug'] in u['new_cases'] + u['updated_cases']]
    if c.get('claim_review'):
        days.append(beijing_day(c['claim_review']['reviewed_at']))
    return max(days, default=case_day(c))


def format_readme_time(value):
    return datetime.fromisoformat(value).astimezone(BEIJING).strftime('%Y-%m-%d %H:%M:%S')


def readme_dates(c, english=False):
    added = format_readme_time(c['readme_added_at'])
    updated = format_readme_time(c['readme_updated_at'])
    if english:
        return f'**Added to README:** {added}<br>**Content updated:** {updated}'
    return f'**收录到 README：** {added}<br>**内容更新：** {updated}'
