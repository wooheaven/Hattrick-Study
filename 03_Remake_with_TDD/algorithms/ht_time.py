from datetime import datetime, date, timedelta


class HattrickTime():
    def findLastSunOrWed(self, target_day_str=None):
        if target_day_str is None:
            target_day = date.today()
        else:
            target_day = datetime.strptime(target_day_str, '%Y/%m/%d')
        # weekday 2 = Wed
        # weekday 6 = Sun
        delta_last_wed = (target_day.weekday() - 2) % 7
        delta_last_sun = (target_day.weekday() - 6) % 7
        delta_last = min(delta_last_wed, delta_last_sun)

        last_wed_or_sun = target_day - timedelta(days=delta_last)
        result = last_wed_or_sun.strftime('%Y/%m/%d')

        return result
