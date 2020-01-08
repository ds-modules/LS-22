"""Full urls for data sets loaded into correlation-causation notebook.
Hidden in a separate file to improve notebook cleanliness and avoid data set spoilers."""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import pearsonr


# USDA agriculture food consumption data
# from Tyler Veigen's Spurious Correlations
usda_url = "https://www2.census.gov/library/publications/2011/compendia/statab/131ed/tables/12s0217.xls"
# read into df
raw_food_data = pd.read_excel(usda_url, header=3)
# extract mozzerella data
mystery_var1 = raw_food_data.iloc[32,6:].astype('float')
# quick and dirty cleaning
food_data = raw_food_data.set_index("Commodity").drop(["Unit", 1980, 1985, 1990, 1995], axis=1).dropna()



# NSF data on engineering degrees 
# from Tyler Veigen's Spurious Correlations
nsf_url = "https://wayback.archive-it.org/5902/20181003231608/https://www.nsf.gov/statistics/infbrief/nsf11305/tab1.xls"
# read into df
raw_engr_data = pd.read_excel(nsf_url, header=1)
# extract ce data
mystery_var2 = raw_engr_data.iloc[24, 2:].astype('float')
# quick and dirty cleaning
engr_data = raw_engr_data.dropna().set_index("Field").drop(1999, axis=1)

# function for the datasaurus widget
def analyze_data(dataset_num):
    data = pd.read_csv("https://raw.githubusercontent.com/lockedata/datasauRus/master/inst/extdata/DatasaurusDozen.tsv", 
            index_col="dataset", sep='\t')
    dataset_list = data.index[::-1].unique()
    data = data.loc[dataset_list[dataset_num -1], :]
    fig = plt.figure(figsize=(14, 6));
    ax1=fig.add_subplot(121);
    sns.scatterplot(data=data, x="x", y="y");
    ax2 = fig.add_subplot(122);
    ax2.axis('off');
    s = pd.Series([data.x.mean(),np.std(data.x),data.y.mean(),np.std(data.y), 
                          pearsonr(data.x, data.y)[0],pearsonr(data.x, data.y)[1]]).apply(str)
    cell_vals = list(zip(['mean x', 'SD x', 'mean y', 'SD y', 'correlation', 'p-value'],s))
    ax2.table(cellText = cell_vals, bbox=[0, 0, 1, 1]);
    plt.show();