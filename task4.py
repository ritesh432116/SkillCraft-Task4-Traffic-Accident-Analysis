import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("--- Step 1: Loading data (Fast Mode) ---")
# Pehle 5000 rows utha rahe hain taaki process fast ho
df = pd.read_csv("accident_data.csv", nrows=5000)
print("Data loaded successfully!\n")

print("--- Step 2: Processing Graphs ---")

# 1. Time of Day Graph (Bar Chart)
plt.figure(figsize=(10, 5))
# time_of_day column ke hisab se count plot
sns.countplot(x='time_of_day', data=df, palette='magma')
plt.title("Accidents Distribution by Time of Day", fontsize=12, fontweight='bold')
plt.xlabel("Time of Day")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=15) # Naamo ko thoda tircha karne ke liye taaki saaf dikhein
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show() # Yeh pehla graph screen par dikhayega

# 2. Weather Conditions Graph (Bar Chart)
plt.figure(figsize=(10, 5))
weather_counts = df['weather'].value_counts().head(5)
sns.barplot(x=weather_counts.index, y=weather_counts.values, palette='viridis')
plt.title("Top Weather Conditions During Accidents", fontsize=12, fontweight='bold')
plt.xlabel("Weather Condition")
plt.ylabel("Number of Accidents")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show() # Yeh doosra graph dikhayega

# 3. Lighting Conditions Graph (Pie Chart)
plt.figure(figsize=(8, 8))
lighting_counts = df['lighting'].value_counts().head(5)
plt.pie(lighting_counts.values, labels=lighting_counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'), startangle=140)
plt.title("Accidents by Lighting Conditions", fontsize=12, fontweight='bold')
plt.show() # Yeh teesra graph dikhayega

print("--- Done! All graphs generated successfully ---")