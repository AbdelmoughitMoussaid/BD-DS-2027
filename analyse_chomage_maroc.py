import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset_chomage_maroc_2022_2025.csv")

print("Données :")
print(df)
print("\nVariation du taux national 2022-2025 :",
      round(df.loc[df.annee==2025, "chomage_national_pct"].iloc[0]
            - df.loc[df.annee==2022, "chomage_national_pct"].iloc[0], 1), "point(s)")

plt.figure(figsize=(8, 4.5))
plt.plot(df["annee"], df["chomage_national_pct"], marker="o", label="National")
plt.plot(df["annee"], df["chomage_jeunes_15_24_pct"], marker="o", label="Jeunes 15-24 ans")
plt.plot(df["annee"], df["chomage_femmes_pct"], marker="o", label="Femmes")
plt.xlabel("Année")
plt.ylabel("Taux de chômage (%)")
plt.title("Évolution du chômage au Maroc (2022-2025)")
plt.xticks(df["annee"])
plt.legend()
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig("graphique_taux_chomage.png", dpi=180)
plt.show()

plt.figure(figsize=(8, 4.5))
plt.bar(df["annee"].astype(str), df["emplois_agriculture"]/1000)
plt.axhline(0, linewidth=0.8)
plt.xlabel("Année")
plt.ylabel("Création/perte d'emplois (milliers)")
plt.title("Variation annuelle de l'emploi dans l'agriculture")
plt.tight_layout()
plt.savefig("graphique_agriculture.png", dpi=180)
plt.show()
