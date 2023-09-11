import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
corona_scaled = pd.read_excel("outputs/corona_centrality_measures/corona_data_for_analysis/corona_centrality_scaled_data.xlsx")
influenza_scaled = pd.read_excel("outputs/influenza_centrality_measures/influenza_data_for_analysis/influenza_centrality_scaled_data.xlsx")

corona_scaled = corona_scaled.drop(['Node', 'corona_nodes'], axis=1)
influenza_scaled = influenza_scaled.drop(['Node', 'influenza_nodes'], axis=1)

corona_correlation = corona_scaled.corr()
influenza_correlation = influenza_scaled.corr()

fig, axs = plt.subplots(1, 2, figsize=(20, 6))

# Plot the corona correlation
axs[0].set_title('Corona Correlation',fontweight='bold')
sns.heatmap(corona_correlation, annot=False, cmap='coolwarm', ax=axs[0], linewidths=0)

# Plot the influenza correlation
axs[1].set_title('Influenza Correlation',fontweight='bold')
sns.heatmap(influenza_correlation, annot=False, cmap='coolwarm', ax=axs[1],linewidths=0)
plt.subplots_adjust(wspace=0.6)

combined_filename = "figures/dissimilarity_matrix_for_corona_and_influenza.png"
plt.savefig(combined_filename, dpi=300, bbox_inches='tight')


plt.show()