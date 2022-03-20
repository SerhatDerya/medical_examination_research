import preprocessing
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = preprocessing.preprocess()

def draw_catplot():
    
    df_reduced = df[["active","alco","cholesterol","gluc","overweight","smoke","cardio"]].melt(id_vars="cardio")
    
    catplot = sns.catplot(x="variable", hue="value", col="cardio", data=df_reduced, kind="count");
    fig = catplot.fig
    fig.savefig("catplot.png")
    
    return catplot;

def draw_heatmap():
    
    df_corr = df.corr()
    matrix = np.triu(df_corr)

    plt.figure(figsize=(13,7))
    heatmap = sns.heatmap(df.corr(), linewidths=.5, annot=True, mask=matrix);
    plt.savefig("heatmap.png")
    
    return heatmap;