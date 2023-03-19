import nasdaqdatalink


class StockService:
    DATABASE_CODE = 'WIKI'
    FRIDAY_ID = 4

    def get_yearly_average(self, company):
        df = nasdaqdatalink.get(f"{self.DATABASE_CODE}/{company}")

        fridays_filter = df.index.dayofweek == self.FRIDAY_ID
        # TODO: Compute the average for each year.
        # TODO: Edgecase - Are there cases when the week closes at another day?
        return 2015, df[fridays_filter]['Close'].mean()
