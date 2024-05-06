import pytest

from regression import SalesRecord, predict_sales


@pytest.fixture
def sales():
    sale_1 = SalesRecord(weather_score=5,was_weekend_or_holiday=1,was_game_day=0,bread_sold=300)
    sale_2 = SalesRecord(weather_score=3,was_weekend_or_holiday=1,was_game_day=1,bread_sold=225)
    sale_3 = SalesRecord(weather_score=1,was_weekend_or_holiday=1,was_game_day=0,bread_sold=75)
    sale_4 = SalesRecord(weather_score=4,was_weekend_or_holiday=0,was_game_day=1,bread_sold=200)
    sale_5 = SalesRecord(weather_score=4,was_weekend_or_holiday=0,was_game_day=0,bread_sold=150)
    sale_6 = SalesRecord(weather_score=2,was_weekend_or_holiday=0,was_game_day=0,bread_sold=50)
    
    return[sale_1, sale_2, sale_3, sale_4, sale_5, sale_6]


def test_predict_sales_when_predicted_then_as_expected(sales):
    unknown_sale = SalesRecord(weather_score=4, was_weekend_or_holiday=1, was_game_day=0, bread_sold=0)
    known_sale = predict_sales(sales, unknown_sale)
    assert known_sale.bread_sold == 219
