class utility:
    def slicer(self, df, list):
        df.drop(df.columns.difference(list), 1, inplace=True)
        return df