from number_to_word import NumberAsWord


def time_in_words(hour: int, minute: int) -> str:
    if _is_on_the_hour(minute):
        return _on_the_hour_wording(hour)
    elif _is_quarter_past(minute):
        return _quarter_past_wording(hour)
    elif _is_half_past(minute):
        return _half_past_wording(hour)
    elif _is_quarter_to(minute):
        return _quarter_to_wording(hour)
    elif _is_past_the_hour(minute):
        return _past_the_hour_wording(hour, minute)
    elif _is_to_the_hour(minute):
        return _to_the_hour_wording(hour, minute)
    else:
        raise Exception('Not a valid time')


def _is_on_the_hour(minute: int) -> bool:
    return minute == 0


def _is_quarter_past(minute: int) -> bool:
    return minute == 15


def _is_half_past(minute: int) -> bool:
    return minute == 30


def _is_quarter_to(minute: int) -> bool:
    return minute == 45


def _is_past_the_hour(minute: int) -> bool:
    return minute > 0 and minute <= 30


def _is_to_the_hour(minute: int) -> bool:
    return minute > 30 and minute <= 59


def _on_the_hour_wording(hour: int) -> str:
    return f"{NumberAsWord(hour).value} o' clock"


def _quarter_past_wording(hour: int) -> str:
    return f"quarter past {NumberAsWord(hour).value}"


def _half_past_wording(hour: int) -> str:
    return f"half past {NumberAsWord(hour).value}"


def _quarter_to_wording(hour: int) -> str:
    return f"quarter to {NumberAsWord(hour + 1).value}"


def _past_the_hour_wording(hour: int, minute: int) -> str:
    return f"{NumberAsWord(minute).value} {_minute_wording(minute)} past {NumberAsWord(hour).value}"


def _to_the_hour_wording(hour: int, minute: int) -> str:
    return f"{NumberAsWord(60 - minute).value} {_minute_wording(minute)} to {NumberAsWord(hour + 1).value}"


def _minute_wording(minute: int) -> str:
    if minute == 1:
        return 'minute'
    else:
        return 'minutes'
