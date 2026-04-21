import pandas as pd


def tsc(data_list, path):
    df_taskswitching = pd.DataFrame({'ID',
                                     # REPEAT CONGRUENT
                                     'Total_ReCon',
                                     'TotCorr_ReCon'
                                     'ErrCount_ReCon',
                                     'MeanRT_ReCon',
                                     'SDRT_ReCon',
                                     'MedianRT_ReCon',
                                     'MinRT_ReCon',
                                     'MaxRT_ReCon',
                                     'ErrRate_ReCon',
                                     # REPEAT INCONGRUENT
                                     'Total_ReIncon',
                                     'TotCorr_ReIncon'
                                     'ErrCount_ReIncon',
                                     'MeanRT_ReIncon',
                                     'SDRT_ReIncon',
                                     'MedianRT_ReIncon',
                                     'MinRT_ReIncon',
                                     'MaxRT_ReIncon',
                                     'ErrRate_ReIncon',
                                     # SWITCH CONGRUENT
                                     'Total_SwCon',
                                     'TotCorr_SwCon'
                                     'ErrCount_SwCon',
                                     'MeanRT_SwCon',
                                     'SDRT_SwCon',
                                     'MedianRT_SwCon',
                                     'MinRT_SwCon',
                                     'MaxRT_SwCon',
                                     'ErrRate_SwCon',
                                     # SWITCH INCONGRUENT
                                     'Total_SwIncon',
                                     'TotCorr_SwIncon'
                                     'ErrCount_SwIncon',
                                     'MeanRT_SwIncon',
                                     'SDRT_SwIncon',
                                     'MedianRT_SwIncon',
                                     'MinRT_SwIncon',
                                     'MaxRT_SwIncon',
                                     'ErrRate_SwIncon'})
    results = []
    for d in data_list:
        data_raw = pd.read_csv(path + '/' + d, header=None, delimiter='\t')
        data_raw.columns = ['Blockname', 'TaskType', 'ConWord', 'ConNum', 'ReqButton', 'RT', 'Corr', 'Taskswitching']
        # 1. Nazwa bloku (trening vs zadanie właściwe);
        data = data_raw[data_raw['Blockname'] == 'realblock']

        df = pd.DataFrame({
            'ID': d[:5],
            # REPEAT CONGRUENT
            'Total_ReCon': len(data[(data['Taskswitching'] == 1) & (data['ConNum'] == 1)]),
            'TotCorr_ReCon': len(data[(data['Taskswitching'] == 1) & (data['ConNum'] == 1) & (data['Corr'] == 1)]),
            'ErrCount_ReCon': len(data[(data['Taskswitching'] == 1) & (data['ConNum'] == 1) & (data['Corr'] > 1)]),
            'MeanRT_ReCon': data[(data['Taskswitching'] == 1) & (data['ConNum'] == 1)]['RT'].mean(),
            'SDRT_ReCon': data[(data['Taskswitching'] == 1) & (data['ConNum'] == 1)]['RT'].std(),
            'MedianRT_ReCon': data[(data['Taskswitching'] == 1) & (data['ConNum'] == 1)]['RT'].median(),
            'MinRT_ReCon': data[(data['Taskswitching'] == 1) & (data['ConNum'] == 1)]['RT'].min(),
            'MaxRT_ReCon': data[(data['Taskswitching'] == 1) & (data['ConNum'] == 1)]['RT'].max(),
            'ErrRate_ReCon': (len(
                data[(data['Taskswitching'] == 1) & (data['ConNum'] == 1) & (data['Corr'] > 1)]) / len(
                data[(data['Taskswitching'] == 1) & (data['ConNum'] == 1)])) * 100,
            # REPEAT INCONGRUENT
            'Total_ReIncon': len(data[(data['Taskswitching'] == 1) & (data['ConNum'] == 2)]),
            'TotCorr_ReIncon': len(data[(data['Taskswitching'] == 1) & (data['ConNum'] == 2) & (data['Corr'] == 1)]),
            'ErrCount_ReIncon': len(data[(data['Taskswitching'] == 1) & (data['ConNum'] == 2) & (data['Corr'] > 1)]),
            'MeanRT_ReIncon': data[(data['Taskswitching'] == 1) & (data['ConNum'] == 2)]['RT'].mean(),
            'SDRT_ReIncon': data[(data['Taskswitching'] == 1) & (data['ConNum'] == 2)]['RT'].std(),
            'MedianRT_ReIncon': data[(data['Taskswitching'] == 1) & (data['ConNum'] == 2)]['RT'].median(),
            'MinRT_ReIncon': data[(data['Taskswitching'] == 1) & (data['ConNum'] == 2)]['RT'].min(),
            'MaxRT_ReIncon': data[(data['Taskswitching'] == 1) & (data['ConNum'] == 2)]['RT'].max(),
            'ErrRate_ReIncon': (len(
                data[(data['Taskswitching'] == 1) & (data['ConNum'] == 2) & (data['Corr'] > 1)]) / len(
                data[(data['Taskswitching'] == 1) & (data['ConNum'] == 2)])) * 100,
            # SWITCH CONGRUENT
            'Total_SwCon': len(data[(data['Taskswitching'] == 2) & (data['ConNum'] == 1)]),
            'TotCorr_SwCon': len(data[(data['Taskswitching'] == 2) & (data['ConNum'] == 1) & (data['Corr'] == 1)]),
            'ErrCount_SwCon': len(data[(data['Taskswitching'] == 2) & (data['ConNum'] == 1) & (data['Corr'] > 1)]),
            'MeanRT_SwCon': data[(data['Taskswitching'] == 2) & (data['ConNum'] == 1)]['RT'].mean(),
            'SDRT_SwCon': data[(data['Taskswitching'] == 2) & (data['ConNum'] == 1)]['RT'].std(),
            'MedianRT_SwCon': data[(data['Taskswitching'] == 2) & (data['ConNum'] == 1)]['RT'].median(),
            'MinRT_SwCon': data[(data['Taskswitching'] == 2) & (data['ConNum'] == 1)]['RT'].min(),
            'MaxRT_SwCon': data[(data['Taskswitching'] == 2) & (data['ConNum'] == 1)]['RT'].max(),
            'ErrRate_SwCon': (len(
                data[(data['Taskswitching'] == 2) & (data['ConNum'] == 1) & (data['Corr'] > 1)]) / len(
                data[(data['Taskswitching'] == 2) & (data['ConNum'] == 1)])) * 100,
            # SWITCH INCONGRUENT
            'Total_SwIncon': len(data[(data['Taskswitching'] == 2) & (data['ConNum'] == 2)]),
            'TotCorr_SwIncon': len(data[(data['Taskswitching'] == 2) & (data['ConNum'] == 2) & (data['Corr'] == 1)]),
            'ErrCount_SwIncon': len(data[(data['Taskswitching'] == 2) & (data['ConNum'] == 2) & (data['Corr'] > 1)]),
            'MeanRT_SwIncon': data[(data['Taskswitching'] == 2) & (data['ConNum'] == 2)]['RT'].mean(),
            'SDRT_SwIncon': data[(data['Taskswitching'] == 2) & (data['ConNum'] == 2)]['RT'].std(),
            'MedianRT_SwIncon': data[(data['Taskswitching'] == 2) & (data['ConNum'] == 2)]['RT'].median(),
            'MinRT_SwIncon': data[(data['Taskswitching'] == 2) & (data['ConNum'] == 2)]['RT'].min(),
            'MaxRT_SwIncon': data[(data['Taskswitching'] == 2) & (data['ConNum'] == 2)]['RT'].max(),
            'ErrRate_SwIncon': (len(
                data[(data['Taskswitching'] == 2) & (data['ConNum'] == 2) & (data['Corr'] > 1)]) / len(
                data[(data['Taskswitching'] == 2) & (data['ConNum'] == 2)])) * 100,
            # GENERAL STATISTICS
            'TaskSwitchRT_Mean': data[(data['Taskswitching'] == 2)]['RT'].mean(),
            'TaskSwitchRT_SD': data[(data['Taskswitching'] == 2)]['RT'].std(),
            'TaskRepeatRT_Mean': data[(data['Taskswitching'] == 1)]['RT'].mean(),
            'TaskRepeatRT_SD': data[(data['Taskswitching'] == 1)]['RT'].std(),
            'SwitchCost': np.abs(
                (data[(data['Taskswitching'] == 2)]['RT'].mean()) - (data[(data['Taskswitching'] == 1)]['RT'].mean())),
            'TaskConRT_Mean': data[(data['ConNum'] == 1)]['RT'].mean(),
            'TaskConRT_SD': data[(data['ConNum'] == 1)]['RT'].std(),
            'TaskInconRT_Mean': data[(data['ConNum'] == 2)]['RT'].mean(),
            'TaskInconRT_SD': data[(data['ConNum'] == 2)]['RT'].std(),
            'TaskInterference': np.abs(
                (data[(data['ConNum'] == 1)]['RT'].mean()) - (data[(data['ConNum'] == 2)]['RT'].mean()))
        }, index=[0])
        print(df)
        results.append(df)

    df_taskswitching = pd.concat(results, ignore_index=True)
    return df_taskswitching
