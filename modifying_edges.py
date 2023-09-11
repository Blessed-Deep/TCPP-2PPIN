import pandas as pd

# Read the Excel files
c_sheet1_df = pd.read_csv("datasets/corona_edges.csv")
c_sheet2_df = pd.read_excel("datasets/corona_nodes.xlsx")

i_sheet1_df = pd.read_csv("datasets/influenza_edges.csv")
i_sheet2_df = pd.read_excel("datasets/influenza_nodes.xlsx")

# Create a dictionary mapping values from Sheet 1 to values from Sheet 2

c_mapping_dict = dict(zip(c_sheet2_df["Node"], c_sheet2_df["corona_nodes"]))
i_mapping_dict = dict(zip(i_sheet2_df["Node"], i_sheet2_df["influenza_nodes"]))

# Replace values in Sheet 1 using the mapping dictionary

c_sheet1_df["V1"] = c_sheet1_df["V1"].map(c_mapping_dict)
c_sheet1_df["V2"] = c_sheet1_df["V2"].map(c_mapping_dict)

i_sheet1_df["V1"] = i_sheet1_df["V1"].map(i_mapping_dict)
i_sheet1_df["V2"] = i_sheet1_df["V2"].map(i_mapping_dict)

# Save the modified DataFrame back to the Excel file or to a new file
c_sheet1_df.to_excel("datasets/corona_edges_modified.xlsx", index=False)
i_sheet1_df.to_excel("datasets/influenza_edges_modified.xlsx", index=False)