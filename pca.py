import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

# Load data from Excel files (replace with your actual file paths)
covid_scaled = pd.read_excel("outputs/corona_centrality_measures/corona_data_for_analysis/corona_centrality_scaled_data.xlsx")
influenza_scaled = pd.read_excel("outputs/influenza_centrality_measures/influenza_data_for_analysis/influenza_centrality_scaled_data.xlsx")

# Drop unnecessary columns
covid_scaled = covid_scaled.drop(['Node', 'corona_nodes'], axis=1)
influenza_scaled = influenza_scaled.drop(['Node', 'influenza_nodes'], axis=1)

# Renaming for large function name

corona_scaled.rename(columns={'approximate_current_flow_betweenness_centrality': 'aaprox_cf_betweenness'}, inplace=True)
corona_scaled.rename(columns={'Communicability_betweenness_centrality': 'comm_betweenness'}, inplace=True)

Functions = (covid_scaled.columns).tolist()

Functions = [func.replace('_centrality', '') for func in Functions]


# Perform PCA separately for each dataset
pca_covid = PCA()
pca_influenza = PCA()

pca_covid.fit(covid_scaled)
pca_influenza.fit(influenza_scaled)

# Get PCA components for each dataset
pca_components_covid = pca_covid.components_[0]
pca_components_influenza = pca_influenza.components_[0]

# Create a DataFrame for the visualization
visualization_df = pd.DataFrame({
    'Centrality Measure': Functions,
    'PCA Component (Corona)': pca_components_covid,
    'PCA Component (Influenza)': pca_components_influenza
})

# Create a heatmap-style visualization with rotated PCA values
plt.figure(figsize=(10, 6))
ax = sns.heatmap(data=visualization_df.set_index('Centrality Measure').T, cmap='coolwarm', annot=True,
                 fmt=".2f", cbar=False, annot_kws={"rotation": 90})
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)  # Reset xticklabels to horizontal
plt.title('PCA Components for Centrality Measures')

combined_filename = "figures/pca.png"
plt.savefig(combined_filename, dpi=300, bbox_inches='tight')

plt.show()