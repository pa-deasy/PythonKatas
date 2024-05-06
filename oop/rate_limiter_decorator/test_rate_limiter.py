from rate_limiter import get_dummie_data


def test_rate_limiter_when_limit_reached_then_returns_expected_message():
    assert get_dummie_data() == 'Dummie Response'
    assert get_dummie_data() == 'Dummie Response'
    assert get_dummie_data() == 'Dummie Response'
    assert get_dummie_data() == 'Limit Reached'