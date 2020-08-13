def create_train_test_split(features : pd.DataFrame, target : pd.DataFrame) -> dict:
    """ Create a Training, Test and Validation Split from the data
        :params features; Dataset for splitting
        :params target: Target varables
        :returns data_split: training testing and validation as list of DataFrames
        Reference - https://stackoverflow.com/questions/38250710/how-to-split-data-into-3-sets-train-validation-and-test
    """
    x, x_test, y, y_test = train_test_split(features,
                                            target,
                                            stratify=target.id,
                                            test_size=0.2,
                                            train_size=0.8)
    x_train, x_cv, y_train, y_cv = train_test_split(x,
                                                    y,
                                                    stratify=y.id,
                                                    test_size = 0.25,
                                                    train_size =0.75)
    
    data_split = {'train' : {'x':x_train,'y':y_train},
                 'test' : {'x':x_test,'y':y_test},
                 'val' : {'x':x_cv,'y':y_cv}}
    
    return data_split
