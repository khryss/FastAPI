from collections import namedtuple

import nasdaqdatalink


YearAverage = namedtuple("YearAverage", "year average")


class StockService:
    DATABASE_CODE = 'WIKI'
    FRIDAY_ID = 4

    def __init__(self, company):
        self.df = nasdaqdatalink.get(f"{self.DATABASE_CODE}/{company}")

    def get_yearly_average(self):
        results = []

        # TODO: Edgecase - Are there cases when the week closes at another day?
        # TODO: Handle exceptions.

        current_year = self.df.index.min().year
        max_year = self.df.index.max().year
        while True:
            if current_year > max_year:
                return results

            year_average = YearAverage(current_year, self.get_average_for_year(current_year))
            results.append(year_average)

            current_year += 1

    def get_average_for_year(self, year):
        df = self.df
        current_year_df = df[df.index.year == year]
        fridays_filter = current_year_df.index.dayofweek == self.FRIDAY_ID

        return current_year_df[fridays_filter]['Close'].mean()
