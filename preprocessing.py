def preprocess():
    import pandas as pd
    import numpy as np

    df = pd.read_csv("medical_examination.csv")
    
    # Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
    
    df["cholesterol"] = np.where(df["cholesterol"] == 1, 0, 1)
    df["gluc"] = np.where(df["gluc"] == 1, 0, 1)
    
    # Add 'overweight' column

    df['overweight'] = np.where((df["weight"]/((df["height"]/100)**2)) > 25, 1, 0)
    
    # "ap_hi" should be higher than "ap_lo"
    
    df = df[df["ap_hi"]>df["ap_lo"]]
    
    # if "height" is less than 2.5th percentile delete the related row
    
    df = df[df["height"]>=df["height"].quantile(0.025)]
    
    # if "height" is greater than 97.5th percentile delete the related row
    
    df = df[df["height"] <= df["height"].quantile(0.975)]

    # if "weight" is less than 2.5th percentile delete the related row
    
    df = df[df["weight"] >= df["weight"].quantile(0.025)]

    # if "weight" is greater than 97.5th percentile delete the related row
    
    df = df[df["weight"] <= df["weight"].quantile(0.975)]

    return df
