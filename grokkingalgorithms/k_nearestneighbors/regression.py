from dataclasses import dataclass

from math import sqrt
from statistics import mean


@dataclass
class SalesRecord():
    weather_score: int
    was_weekend_or_holiday: int
    was_game_day: int
    bread_sold: int
    

@dataclass
class SalesRecordSimilarity():
    bread_sold: int
    similarity: float


def predict_sales(sales: list[SalesRecord], predicted_sale: SalesRecord) -> SalesRecord:
    sales_similarites = [SalesRecordSimilarity(bread_sold=s.bread_sold,similarity=_sale_similarity(predicted_sale, s)) for s in sales]
    sales_similarites.sort(key=lambda s: s.similarity)
    closest_4_sales = [s.bread_sold for s in sales_similarites[:4]]
    
    predicted_sale.bread_sold = round(mean(closest_4_sales))
    
    return predicted_sale
    

def _sale_similarity(sale_a: SalesRecord, sale_b: SalesRecord):
    return sqrt(pow((sale_a.weather_score - sale_b.weather_score), 2) +
                pow((sale_a.was_weekend_or_holiday - sale_b.was_weekend_or_holiday), 2) + 
                pow((sale_a.was_game_day - sale_b.was_game_day), 2))
    