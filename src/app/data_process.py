import pandas as pd

#Read data from a file (with options like quotechar
#clean the raw data
    #drop columns
    #drop NaN
    #drop duplicates
    #convert categorical data
#One hot encoding
#save to file
#load clean data


class DataProcess:
    def __init__(self):
        self.raw_df = None
        self.clean_df = None

    def load(self, file_name, **kwargs):
        data = f'../data/bank/{file_name}.csv'
        df = pd.read_csv(data, **kwargs)  #reads the csv file and converts it to the dframe
        print(df.nunique()) #shows nunique from the new df
        print(df.head()) #show head?
        self.raw_df = df



    def cleanc(self): #drop_NaN, drop_dup, convert

        df_unique = self.raw_df.loc[:, self.raw_df.apply(pd.Series.nunique) != 1]
        self.clean_df = df_unique
        print(df_unique.head())

        


    #def __hot__(self, columns):

        #df = self.clean_df
        #hot_encoding = pd.get_dummies(data[['age', 'gender', 'category']])
        #df_one_hot = pd.hot_encoding([df, hot_encoding], axis=1, sort=False)
        #return.self.df_hot



    #def __save__(self, name, ):

        #return.clean_df





