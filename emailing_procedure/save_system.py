import recipient
import pandas as pd

def save(participants):
    df_new = pd.DataFrame()
    for participant in participants:
        temp = pd.DataFrame([participant.to_dict()])
        df_new = pd.concat([df_new, temp])
    print(df_new)
    df_new.to_csv('participants.csv', index=False)


def load():
    df = pd.read_csv('participants.csv')
    participants = []
    for i in df.index:
        id = df.loc[i, 'ID']
        email = df.loc[i, 'email']
        day = df.loc[i, 'day']
        IsCognit = df.loc[i, 'IsCognit']
        OB = recipient.Recipient(id, email, day, IsCognit)
        participants.append(OB)
    return participants