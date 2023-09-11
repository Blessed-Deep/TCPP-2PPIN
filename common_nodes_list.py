import pandas as pd

# Read the Excel files into dataframes
covid_df = pd.read_excel("datasets/corona_nodes.xlsx")
h1n1_df = pd.read_excel("datasets/influenza_nodes.xlsx")


covid_set = set(covid_df['corona_nodes'])
h1n1_set = set(h1n1_df['influenza_nodes'])

# Find the common nodes
common_nodes = covid_set.intersection(h1n1_set)


common_nodes_list = list(common_nodes)

cn = pd.DataFrame({'common_nodes_list':common_nodes_list})
cn.to_excel('outputs/common_nodes/common_nodes_list.xlsx',index=False)