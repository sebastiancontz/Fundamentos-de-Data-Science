import pandas as pd
import numpy as np
import factor_analyzer as fact
import missingno as miss
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import *

def inspeccion_datos(dataframe):
    """
    Esta función retorna las medias descriptivas para los variables continuos y la frecuencia para las variables discretas.
    Recibe como argumento un dataframe
    """
    for colname,serie in dataframe.iteritems():
        if pd.api.types.is_numeric_dtype(serie):
            print('"{}" es una variable continua, y su descripción es:'.format(colname))
            print('-----------')
            print(serie.describe())
            print('')
        else:
            frec=serie.value_counts('%')
            print('"{}" es una variable discreta, y su frecuencia es:'.format(colname))
            print('-----------')
            print(frec)
            print('')

def barplot_missdata(dataframe):
    """
    Función que retorna gráfico de barras de la librería seaborn, mostrando los datos perdidos, ordenados de mayor a menor. 
    """
    sns.set(style="darkgrid")
    tmp_df = pd.DataFrame(data=dataframe.isna().sum())
    tmp_df = tmp_df.rename(columns={0: 'missdata'})
    tmp_df = tmp_df.rename(columns={0: 'missdata'}).sort_values('missdata',ascending=False)
    ax = sns.barplot(x='missdata', y = tmp_df.index, data=tmp_df);

    for p in ax.patches:
        ax.annotate("%.0f" % p.get_width(), (p.get_x() + p.get_width(), p.get_y() + 1.2),
                    xytext=(5, 10), textcoords='offset points')

    plt.tight_layout()
    plt.show()

def saturated_model(df, dependent, estimation=smf.logit,fit_model=True):
    """
    saturated_model - returns a saturated model

    @parameters:
        - df: a `pandas.core.frame.DataFrame` object.
        - dependent: String. Name of the dependent variable to be modelled.
        - estimation: Method. A `statsmodels` class estimator
        - fit_model: Bool. Whether the returned model should be fitter or not. Default: True

    @returns:
        - A `smf` model.

    """
    # seleccionamos todas las variables que no sean la dependiente
    tmp_vars = "+".join(df.columns.drop(dependent))
    # generamos la estimación del modelo
    tmp_model = estimation(dependent+ '~ '+ tmp_vars, df)
    # si fit model es verdadero, podemos realizar el fit de forma automática
    if fit_model is True:
        tmp_model = tmp_model.fit()
    # recuerden retornar el objeto :)
    return tmp_model

def results_summary_to_dataframe(results):
    '''This takes the result of an statsmodel results table and transforms it into a dataframe'''
    pvals = results.pvalues
    coeff = results.params
    conf_lower = results.conf_int()[0]
    conf_higher = results.conf_int()[1]

    results_df = pd.DataFrame({"pvals":pvals,
                               "coeff":coeff,
                               "conf_lower":conf_lower,
                               "conf_higher":conf_higher
                                })

    #Reordering...
    results_df = results_df[["coeff","pvals","conf_lower","conf_higher"]]
    return results_df

def coefplot(model, varnames=True, intercept=False, fit_stats=True, figsize=(7, 12)):
    """
    coefplot - Visualize coefficient magnitude and approximate frequentist significance from a model.
    
    @parameters:
        - model: a `statsmodels.formula.api` class generated method, which must be already fitted.
        - varnames: if True, y axis will contain the name of all of the variables included in the model. Default: True
        - intercept: if True, coefplot will include the $\beta_{0}$ estimate. Default: False.
        - fit_stats: if True, coefplot will include goodness-of-fit statistics. Default: True.
        
    @returns:
        - A `matplotlib` object.
    """
    if intercept is True:
        coefs = model.params.values
        errors = model.bse
        if varnames is True:
            varnames = model.params.index
    else:
        coefs = model.params.values[1:]
        errors = model.bse[1:]
        if varnames is True:
            varnames = model.params.index[1:]
            
    tmp_coefs_df = pd.DataFrame({'varnames': varnames, 'coefs': coefs,'error_bars': errors})
    fig, ax = plt.subplots(figsize=figsize)
    ax.errorbar(y=tmp_coefs_df['varnames'], x=tmp_coefs_df['coefs'], 
                xerr=tmp_coefs_df['error_bars'], fmt='o', 
                color='slategray', label='Estimated point')
    ax.axvline(0, color='tomato', linestyle='--', label='Null Effect')
    ax.set_xlabel(r'$\hat{\beta}$')
    fig.tight_layout()
    plt.legend(loc='best')
    
    if fit_stats is True:
        if 'linear_model' in model.__module__.split('.'):
            plt.title(r'R$^{2}$' + "={0}, f-value={1}, n={2}".format(round(model.rsquared, 2),
                                                                     round(model.f_pvalue, 3),
                                                                     model.nobs))
        elif 'discrete_model' in model.__module__.split('.'):
            plt.title("Loglikelihood = {0}, p(ll-Rest)={1}, n={2}".format(round(model.llf, 2),
                                                                          round(model.llr_pvalue, 3),
                                                                          model.nobs))

def stats_bondad_ajuste(modelo):
    """
    Función que retorna los ajustes de bondad para un modelo de la librería scikitlearn
    Retorna los valores LLF, LLNull, LLR-pvalue, Diferencia entre LLF y LLNull.
    """        
    estadisticos = []
    estadisticos.append(modelo.llf)
    estadisticos.append(modelo.llnull)
    estadisticos.append(modelo.llr_pvalue)
    estadisticos.append(float(modelo.llf)-float(modelo.llnull))
    
    datos = pd.Series(data=estadisticos,index=['Log-Likelihood', 'LL-Null', 'LLR p-value', 'Diff_LLF_LLNull'])
    return datos

def convertir_str_to_int(dataframe):
    """
    Función que convierte los valores númericos con formato string a datos tipo integer.
    """
    for colname in dataframe:
        for index, value in enumerate (dataframe[colname].unique()):
            try:
                dataframe[colname] = dataframe[colname].replace(value,int(value))
            except:
                pass

def explorar_dotplot(dataf,var_obj,group_by,output_media=False):
    """
    Esta función permite graficar un dotplot entre una variable agrupadora y una objetivo
    """
    #Agrupando 
    tmp_group= dataf.groupby(group_by)[var_obj].mean()
    if output_media is True:
        print(pd.DataFrame(tmp_group))
    
    #Graficando las medias en un dot plot
    plt.plot(tmp_group.index, tmp_group.values, 'o', color = 'grey')
    plt.axhline(tmp_group.mean(), 
                color = 'tomato', 
                linestyle = '--')
    
    plt.xlabel(group_by)
    plt.ylabel(var_obj)
    plt.title('"{}"  según  "{}"'.format(var_obj,group_by),size=12)

def explorar_lmplot(eje_x,eje_y,abrir_por,dataf,col=5):
    """
    Esta función permite hacer un gráfico de dispersión entre dos variables y abrirla por una tercera variable
    eje_x: variable independiente
    eje_y: variable dependiente
    abrir_por: variable bajo la cual queremos ampliar análisis
    dataf: matriz de datos
    """
    sns.lmplot(x=eje_x, y=eje_y, col=abrir_por,data=dataf,col_wrap=col);

def explorar_regplot(dataframe, eje_x,eje_y):
    """
    Esta función permite hacer un gráfico de dispersión entre dos variables y abrirla por una tercera variable
    eje_x: variable independiente
    eje_y: variable dependiente
    dataf: matriz de datos
    """
    sns.regplot(x=eje_x, y=eje_y, data=dataframe);

def explorar_dotplot2(dataf,var_obj,group_by,output_media = False):
    """
    Esta función permite graficar un dotplot entre una variable agrupadora y una objetivo
    """
    #Agrupando 
    tmp_group= dataf.groupby(group_by)[var_obj].mean()
    if output_media is True:
        print(pd.DataFrame(tmp_group))
    
    #Graficando las medias en un dot plot
    #plt.plot(tmp_group.values, tmp_group.index, 'o', color = 'grey', label=group_by)
    plt.plot(tmp_group.values, tmp_group.index, 'o', color = 'grey')
    plt.xlim(0, 1)
    plt.axvline(tmp_group.mean(), 
                color = 'tomato', 
                linestyle = '--')
                #label='media global es {}'.format(round(dataf[var_obj].mean(),3)))
    #plt.legend(fancybox=True, framealpha=.8, shadow=True, borderpad=0)
    plt.xlabel(var_obj)
    plt.ylabel(group_by)
    plt.title('"{}"  según  "{}"'.format(var_obj,group_by),size=10)

def boxplot_por_notas(dataframe):
    categoric_cols = []
    for colname in dataframe.columns:
        if dataframe[colname].dtype == 'object':
            categoric_cols.append(colname)
        else:
            pass

    for index, value in enumerate(categoric_cols):
        sns.set(style="darkgrid")
        fig, axs = plt.subplots(ncols=3)
        
        sns.boxplot(x=value, y='G1', data=dataframe.loc[:,[value, 'G1', 'G2', 'G3']],
                    palette="bright", ax= axs[0]).set_title('G1')
        sns.boxplot(x=value, y='G2', data=dataframe.loc[:,[value, 'G1', 'G2', 'G3']],
                    palette="bright", ax= axs[1]).set_title('G2')
        sns.boxplot(x=value, y='G3', data=dataframe.loc[:,[value, 'G1', 'G2', 'G3']], 
                    palette="bright", ax= axs[2]).set_title('G3')
        plt.tight_layout()

def binarize_variables(df, var, saturate=False):
    """
    binarize_variables - Return a set of dummy variables according to a categorical variable

    @parameters:
    - df: a pd.DataFrame object to store dummy variables.
    - var: categorical variable to extract dummy categories from.
    - saturate: if True, the number of dummy variables will be the same as the number of categories in var.
    if False, the number of dummy variables will be N-1, taking the highest frequency category as reference.
    Useful for regression modeling and reassuring parameter identification.

    @returns:
    - A finite quantity of series.

    """
    if pd.api.types.is_string_dtype(df[var]) is True:
        if saturate is True:
            for i in df[var].unique():
                processed_string = str(i).lower().replace('-', '_')
                df[processed_string] = np.where(df[var] == i, 1, 0)
        elif saturate is False:
            get_freq = df[var].value_counts()
            recoding = get_freq[get_freq != get_freq.max()]
            for i in recoding.index:
                processed_string = str(i).lower().replace('-', '_')
                df[processed_string] = np.where(df[var] == i, 1, 0)
    else:
        print(var, "is not categorical. Perhaps you meant to use `replace` for custom ranges?")

def inverse_logit(x):
    """
    Función que retorna el logit inverso para la `y` estimada de un modelo
    """
    return 1 / (1 + np.exp(-x))

def reportar_metricas_modelo(y_test, yhat):
    """
    Función que retorna las métricas de precisión y recall para las variables objetivos de los datos de entrenamiento y testeo de un modelo predictivo.
    """
    prec = precision_score(y_test, yhat)
    rec = recall_score(y_test, yhat)
    print("Precision: ", prec, "\nRecall: ", rec)
    print(classification_report(y_test, yhat))

def remove_character(dataf,var):
    """
    Esta función suprime caractér ' " ' de adelante y al final de la cadena
    *dataf= DataFrame a utilizar
    *var=String, nombre de la variable a limpiar '"' de los extremos
    """
    tmp=[]
    for i in dataf[var]:
        if type(i)==str:
            i=i.strip('"')
            tmp.append(i)
        else:
            tmp.append(i)

    dataf[var]=tmp

def comparar_modelos_ols(modelo1,modelo2):
    """
    Función que retorna las tablas de resultados de dos modelos OLS de la librería `scikit-learn`
    """
    
    print ('Modelo 1:', modelo1.summary().tables[0])
    print ('Modelo 2:', modelo2.summary().tables[0])

def report_scores(y_predecido,y_testing):
    print("Error Cuadrático Promedio: {}".format(mean_squared_error(y_testing, y_predecido)))
    print("r2: {}".format(r2_score(y_testing, y_predecido)))