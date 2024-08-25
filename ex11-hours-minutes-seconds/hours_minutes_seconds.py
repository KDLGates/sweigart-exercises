def get_hours_minutes_seconds(total_seconds:int) -> str:
    if total_seconds == 0:
        return '0s'

    s_wp = total_seconds
    total_minutes = s_wp // 60
    m_wp = total_minutes
    s_wp -= total_minutes * 60
    total_hours = m_wp // 60 + s_wp // 60 // 60
    m_wp -= total_hours * 60
    total_minutes = m_wp
    total_seconds = s_wp
    # print(f'{total_hours=}h {total_minutes=}m {total_seconds=}s')
    output = ''
    if total_hours:
        output += f'{total_hours}h '
    if total_minutes:
        output += f'{total_minutes}m '
    if total_seconds:
        output += f'{total_seconds}s'
    return output.strip()

assert get_hours_minutes_seconds(30) == '30s'
assert get_hours_minutes_seconds(60) == '1m'
assert get_hours_minutes_seconds(90) == '1m 30s'
assert get_hours_minutes_seconds(3600) == '1h'
assert get_hours_minutes_seconds(3601) == '1h 1s'
assert get_hours_minutes_seconds(3661) == '1h 1m 1s'
assert get_hours_minutes_seconds(90042) == '25h 42s'
assert get_hours_minutes_seconds(0) == '0s'
