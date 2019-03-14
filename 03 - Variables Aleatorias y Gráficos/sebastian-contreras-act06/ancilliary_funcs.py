import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def print_miss_values(dataframe,var,print_list = False):
    
    """
    Función que retorna la cantidad de casos perdidos y el porcentaje correspondiente, con el argumento opcional "print_list", el cual lista los casos con datos perdidos
    """
    
    print(dataframe[var].isna().value_counts('%'))
    print(dataframe[var].isna().value_counts())
    print("")
    tmp_na = dataframe[dataframe[var].isna()]['ccodealp']
    if print_list is True:
        print(tmp_na)
        
        
def dotplot(dataframe, plot_var, plot_by, global_stat=False, statistic='mean'):
    """
    Función que genera un dotplot de una variable agrupada por un atributo. El argumento opcional global_stat grafica la media global de la variable, mientras que el argumento statistic indica la medida estadística con que agrupa los datos
    """
    
    if statistic is 'mean':
        tmp_group_stat = dataframe.groupby(plot_by)[plot_var].mean()
        plt.plot(tmp_group_stat.values, tmp_group_stat.index, 'o', color = 'grey')
    if statistic is 'median':
        tmp_group_stat = dataframe.groupby(plot_by)[plot_var].median()
        plt.plot(tmp_group_stat.values, tmp_group_stat.index, 'o', color = 'grey')
    if global_stat == True:
        plt.axvline(df[plot_var].mean(), color = 'tomato', linestyle = '--')
    plt.legend();
    
def plot_hist(dataframe, var, sample_mean=False, true_mean=False):
    
    """
    Función que gráfica histograma de una variable a partir de un dataframe. Los argumentos opcionales sample_mean y true_mean agregarán una línea vertical indicando la media del dataframe de la submuestra y el original correspondiente. 
    """
    
    tmp_var = dataframe[var].dropna()
    plt.hist(tmp_var, color='slategrey',alpha=.4)
    if sample_mean is True:
        plt.axvline(tmp_var.mean(), color='tomato', lw=3, linestyle='--')
    if true_mean is True:
        plt.axvline(df[var].mean(), color='dodgerblue', lw=3, linestyle='--')