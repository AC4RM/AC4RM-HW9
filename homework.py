import pandas as pd


class BankAccount(object):
    # Your code here
    pass


sql_query_1 = '''

              '''

sql_query_2 = '''

              '''


def train_model():
    titanic = pd.read_csv('https://raw.githubusercontent.com/AC4RM/AC4RM-dataset/main/homework/titanic.csv',
                          index_col=0)
    # Remove the category in the PClass column that only have one observation
    titanic = titanic[titanic.PClass != '*']
    survived = titanic.Survived
    titanic1 = titanic[['PClass', 'SexCode', 'Age']].copy()
    # Find the mean of each PClass and SexCode group
    imputation_dict = titanic1.groupby(['PClass', 'SexCode']).mean().to_dict()
    # Find the index of missing values
    impute_index = titanic1.Age.isnull()
    titanic1.loc[impute_index, 'Age'] = titanic1[impute_index].apply(lambda x: imputation_dict['Age'][(x[0], x[1])],
                                                                     axis=1)
    # Convert 1st, 2nd, 3rd to 1, 2, 3
    titanic1.PClass = titanic1.PClass.map(lambda t: int(t[0]))

    # Your code here


def word_count(input_string, number=False):
    """
    input_string: string to count
    number: whether to count the numbers
    """
    pass
