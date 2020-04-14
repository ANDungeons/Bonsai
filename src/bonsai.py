"""
A bonsai is a data structure built on and around a Pandas Dataframe.
The bonsai will know the difference between which columns hold descriptive
"independent" variables and which hold "dependent" data.
"""
import pandas

class Bonsai(object):

    def __init__(self, name, file_name=None, independent=[]):
        self.name = name
        self.independent = independent
        if file_name:
            self.data = pandas.read_csv(file_name)
        else:
            self.data = pandas.DataFrame()
        self.dependent = []
        self.__update_depndents()

    def __update_depndents(self):
        print(type(self.data.columns))
        self.dependent = [i for i in self.data.columns if i not in self.independent]

    def unflatten(self, restrict={}):
        self.__unflatten_bonsai(self.data, self.independent, restrict=restrict)

    def get_specific_leaves(self, column, row, value, restrict={}, ignore=[]):

        # Raise any errors related to invalid inputs
        if not column in self.data.columns:
            raise IndexError(f'{column} not in data!')
        if not row in self.data.columns:
            raise IndexError(f'{row} not in data!')
        if not value in self.data.columns:
            raise IndexError(f'{value} not in data!')

        # Raise error if told to ignore requested value
        if value in ignore or column in ignore or row in ignore:
            raise ValueError('You cannot ignore the requested column!')

        indies = self.independent.copy()
        indies.remove(column)
        indies.remove(row)
        depends = self.dependent.copy()
        depends.remove(value)

        # Create a copy of the Bonsai to mess with
        df_temp = self.data.copy(deep=True)

        # Remove the non-request dependent columns and ignored independent
        if len(ignore) > 0:
            df_temp.drop(ignore, axis=1, inplace=True)
        if len(depends) > 0:
            df_temp.drop(depends, axis=1, inplace=True)

        # Get the vertical Bonsai
        vertical_bonsai = unflatten_bonsai(df_temp, indies, restrict=restrict)

        # Get the request leaves of the verticle Bonsai
        return vertical_bonsai


    @staticmethod
    def __unflatten_bonsai(df, layers, dependents, restrict={}):

        column = layers.pop(0)
        types = pandas.unique(df[column].values)

        if column in restrict:
            types = [i for i in types if i not in restrict[column]]

        branch = {}

        for type in types:
            df_type = df[df[column] == type]
            df_type.drop([column], axis=1, inplace=True)
            if len(layers) > 0:
                branch[type] = unflatten_bonsai(df_type, layers, restrict)
            else:
                # Does this need to be turned into a leaf?
                branch[type] = df_type

        return branch

    @staticmethod
    def get_leaves_and_branches(vertical_bonsai):
        """
        Get the leaves within an unflattened Bonsai.
        Each leaf is stored as a list of size 2, where index 0 is the leaf
        and index 1 is the list of all the branches to it from the trunk

        :param vertical_bonsai: dict [of dicts...] of leaves, where keys are branches
        :return: List of all the leaves,
        """
        leaves = []

        for b, l in vertical_bonsai.items():
            branch_leaves = []
            if isinstance(l, dict):
                branch_leaves.extend(get_leaves_and_branches(l))
            else:
                branch_leaves.append([l, []])

            for leaf in branch_leaves:
                branch_trail = leaf[1]
            branch_trail.append(b)
            leaves.append([leaf[0], branch_trail])

    return leaves
