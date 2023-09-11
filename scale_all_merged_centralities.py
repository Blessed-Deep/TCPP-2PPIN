import pandas as pd
from sklearn.preprocessing import StandardScaler

corona_dt = pd.read_excel("outputs/corona_centrality_measures/corona_data_for_analysis/corona_centrality_data.xlsx")
influenza_dt = pd.read_excel("outputs/influenza_centrality_measures/influenza_data_for_analysis/influenza_centrality_data.xlsx")

corona_column_names = [column for column in corona_dt.columns if column not in ['Node', 'corona_nodes']]
influenza_column_names = [column for column in influenza_dt.columns if column not in ['Node', 'influenza_nodes']]
scaler = StandardScaler()

corona_scaled_columns = scaler.fit_transform(corona_dt[corona_column_names])
influenza_scaled_columns = scaler.fit_transform(influenza_dt[influenza_column_names])


corona_scaled_df = pd.DataFrame(corona_scaled_columns, columns=corona_column_names)
influenza_scaled_df = pd.DataFrame(influenza_scaled_columns, columns=influenza_column_names)

corona_scaled_df['Node'] = corona_dt['Node']
corona_scaled_df['corona_nodes'] = corona_dt['corona_nodes']
influenza_scaled_df['Node'] = influenza_dt['Node']
influenza_scaled_df['influenza_nodes'] = influenza_dt['influenza_nodes']


corona_scaled_df = corona_scaled_df[['Node', 'corona_nodes'] + corona_column_names]
influenza_scaled_df = influenza_scaled_df[['Node', 'influenza_nodes'] + influenza_column_names]

corona_scaled_df.to_excel("outputs/corona_centrality_measures/corona_data_for_analysis/corona_centrality_scaled_data.xlsx",index=False)
influenza_scaled_df.to_excel("outputs/influenza_centrality_measures/influenza_data_for_analysis/influenza_centrality_scaled_data.xlsx",index=False)

corona_scaled_df