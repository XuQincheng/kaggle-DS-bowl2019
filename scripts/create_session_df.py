import pandas as pd
from pathlib import Path
from reduce_memory_usage import reduce_mem_usage


path = Path('../data')

print('Loading Data')
train_data = reduce_mem_usage(pd.read_csv(path/'train.csv'))
train_labels = reduce_mem_usage(pd.read_csv(path/'train_labels.csv'))

train_data['id'] = list(range(train_data.shape[0]))
train_data['timestamp'] = pd.to_datetime(train_data.timestamp)


def get_start_of_assessment():
    min_time_stamp = (train_data.loc[train_data.game_session.isin(train_labels.game_session)]
                      .groupby('game_session')
                      .agg({'timestamp': 'min'})
                      .reset_index())
    assessment_session_events = (train_data.loc[train_data.game_session
                                                          .isin(min_time_stamp.game_session)])
    merged_ = assessment_session_events.merge(
        min_time_stamp, on='game_session')
    first_events = merged_.loc[merged_.timestamp_x == merged_.timestamp_y]
    keep_cols = ['event_id', 'game_session', 'timestamp_x',
                 'event_data', 'installation_id', 'event_count',
                 'event_code', 'game_time', 'title', 'type', 'world', 'id']
    return first_events[keep_cols].rename(columns={'timestamp_x': 'timestamp'})


def get_prior_events(id):
    ref_row = train_data.loc[train_data['id'] == id]
    ref_timestamp = ref_row.timestamp.dt.to_pydatetime()[0]
    ref_install_id = ref_row.installation_id.item()
    return train_data.loc[(train_data.timestamp <= ref_timestamp) &
                          (train_data.installation_id == ref_install_id)]


print('Prepping data')
start_assess = get_start_of_assessment()
session_df = []
print('Creating Session Dataframe')
for i, (idx, row) in enumerate(start_assess.iterrows()):
    print(i, end='\r')
    prior_events = get_prior_events(row.id)
    prior_events['session'] = i
    session_df.append(prior_events)

session_df = pd.concat(session_df,axis=0)
print()
print('Saving Data')
session_df.to_csv(path/'session_df.csv')
print('All done')
