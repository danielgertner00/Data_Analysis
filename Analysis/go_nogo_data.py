import pandas as pd

def gng(data_list, path):
    df_gng = pd.DataFrame({'ID','ErrCount','MeanRT','SDRT','MedianRT','MinRT','MaxRT'})
    results = []
    for d in data_list:
        data = pd.read_csv(path + '\\' + d, header=None, delimiter='\t')
        data.columns = ['Condition','RT','Corr']

        df = pd.DataFrame({
            'ID': d[:5],
            'ErrCount_go': len(data[(data['Condition'] == 'go') & (data['Corr'] == 1)]),
            'ErrCount_nogo': len(data[(data['Condition'] == 'nogo') & (data['Corr'] == 1)]),
            'MeanRT_go': data[data['Condition'] == 'go']['RT'].mean(),
            'MeanRT_nogo': data[data['Condition'] == 'nogo']['RT'].mean(),
            'SDRT_go': data[data['Condition'] == 'go']['RT'].std(),
            'SDRT_nogo': data[data['Condition'] == 'nogo']['RT'].std(),
            'MedianRT_go': data[data['Condition'] == 'go']['RT'].median(),
            'MedianRT_nogo': data[data['Condition'] == 'nogo']['RT'].median(),
            'MinRT_go': data[data['Condition'] == 'go']['RT'].min(),
            'MinRT_nogo': data[data['Condition'] == 'nogo']['RT'].min(),
            'MaxRT_go': data[data['Condition'] == 'go']['RT'].max(),
            'MaxRT_nogo': data[data['Condition'] == 'nogo']['RT'].max()
        }, index=[0])
        print(df)
        results.append(df)

    df_gng = pd.concat(results, ignore_index=True)
    return df_gng