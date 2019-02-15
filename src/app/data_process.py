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


class data_process:

    def __init__(self, data):
        self.data = data
        self.raw_df = None
        self.clean_df = None

    def load(self, file_name, **kwargs):
        file_name = f'../data/{file_name}.csv'
        self.raw_df = pd.read_csv(file_name, **kwargs)  #reads the csv file and converts it to the dframe
        print.self.raw_df.nunique() #shows nunique from the new df
        self.raw_df.to_csv(f'../data/{file_name}_raw_data.csv')  #saves the original data in a new csv
        return self.raw_df  #save the created dframe

    #def clean(self, name, *, raw_df, drop_c, drop_NaN, drop_dup, convert):
        #if
        #self.raw_df.datadrop(['zipMerchant', 'zipcodeOri'], axis=1, inplace=True)

        #return.self.clean_df

    #def __hot__(self, columns):

        #df = self.clean_df
        #hot_encoding = pd.get_dummies(data[['age', 'gender', 'category']])
        #df_one_hot = pd.hot_encoding([df, hot_encoding], axis=1, sort=False)
        #return.self.df_hot



    #def __save__(self, name, ):

        #return.clean_df





