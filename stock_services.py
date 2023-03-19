import nasdaqdatalink


class StockService:
    DATABASE_CODE = 'WIKI'
    FRIDAY_ID = 4

    def get_yearly_average(self, company):
        results = []
        df = nasdaqdatalink.get(f"{self.DATABASE_CODE}/{company}")

        # TODO: Edgecase - Are there cases when the week closes at another day?

        current_year = df.index.min().year
        max_year = df.index.max().year
        while True:
            if current_year > max_year:
                return results

            current_year_df = df[df.index.year == current_year]

            fridays_filter = current_year_df.index.dayofweek == self.FRIDAY_ID
            results.append((current_year, current_year_df[fridays_filter]['Close'].mean()))

            current_year += 1
