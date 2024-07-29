# Installation des dépendances nécessaires
# Décommentez la ligne suivante si vous n'avez pas encore installé ces packages
# !pip install plotly pandas numpy

# Importation des bibliothèques nécessaires
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# Étape 1: Lire les données
# Assurez-vous que le chemin vers le fichier 'merged_output.txt' est correct
data_path = "merged_output.txt"
names = []
x_values = []
y1_values = []
y2_values = []
y3_values = []

# Lecture du fichier de données
with open(data_path, 'r') as file:
    lines = file.readlines()

# Étape 2: Extraire les données
for line in lines:
    parts = line.strip().split('|')
    if len(parts) < 3:
        continue
    
    player_info = parts[0].split(':')
    name = player_info[0]
    
    y_values = parts[1].split(':')
    if len(y_values) < 3:
        continue
    
    try:
        y1 = float(y_values[0].replace('"', ''))
        y2 = float(y_values[1].replace('"', ''))
        y3 = float(y_values[2].replace('"', ''))
        x = float(parts[2])
        
        # Ignorer les valeurs -1 et les valeurs < 200
        if y1 == -1 or y2 == -1 or y3 == -1 or x == -1:
            continue
        if y1 < 200 or y2 < 200 or y3 < 200 or x < 200:
            continue
        
        names.append(name)
        x_values.append(x)
        y1_values.append(y1)
        y2_values.append(y2)
        y3_values.append(y3)
    except ValueError:
        continue

# Étape 3: Créer un DataFrame pour faciliter la manipulation avec Plotly
df = pd.DataFrame({
    'Name': names,
    'X': x_values,
    'Y1': y1_values,
    'Y2': y2_values,
    'Y3': y3_values
})

# Étape 4: Calculer les coefficients directeurs et les afficher

# Calcul des coefficients directeurs (slopes)
slope_y1, intercept_y1 = np.polyfit(df['X'], df['Y1'], 1)
slope_y2, intercept_y2 = np.polyfit(df['X'], df['Y2'], 1)
slope_y3, intercept_y3 = np.polyfit(df['X'], df['Y3'], 1)

# Générer les lignes de tendance
line_y1 = slope_y1 * df['X'] + intercept_y1
line_y2 = slope_y2 * df['X'] + intercept_y2
line_y3 = slope_y3 * df['X'] + intercept_y3

# Plot for Y1 Values (Bullet Rating)
fig1 = go.Figure()
fig1.add_trace(go.Scatter(
    x=df['X'],
    y=df['Y1'],
    mode='markers',
    marker=dict(size=10, color='maroon'),  # Use maroon color for Y1
    text=df['Name'],
    name='Bullet Rating'
))
# Adding the trend line
fig1.add_trace(go.Scatter(
    x=df['X'],
    y=line_y1,
    mode='lines',
    marker=dict(color='black'),
    name=f'Trend Line (slope: {slope_y1:.2f})'
))
fig1.update_layout(
    title=f'Interactive Plot with Player Names for Bullet Rating (Slope: {slope_y1:.2f})',
    xaxis_title='FIDE Rating',
    yaxis_title='Bullet Rating',
    showlegend=True
)
fig1.show()

# Plot for Y2 Values (Blitz Rating)
fig2 = go.Figure()
fig2.add_trace(go.Scatter(
    x=df['X'],
    y=df['Y2'],
    mode='markers',
    marker=dict(size=10, color='yellow'),  # Use yellow color for Y2
    text=df['Name'],
    name='Blitz Rating'
))
# Adding the trend line
fig2.add_trace(go.Scatter(
    x=df['X'],
    y=line_y2,
    mode='lines',
    marker=dict(color='black'),
    name=f'Trend Line (slope: {slope_y2:.2f})'
))
fig2.update_layout(
    title=f'Interactive Plot with Player Names for Blitz Rating (Slope: {slope_y2:.2f})',
    xaxis_title='FIDE Rating',
    yaxis_title='Blitz Rating',
    showlegend=True
)
fig2.show()

# Plot for Y3 Values (Rapid Rating)
fig3 = go.Figure()
fig3.add_trace(go.Scatter(
    x=df['X'],
    y=df['Y3'],
    mode='markers',
    marker=dict(size=10, color='green'),  # Use green color for Y3
    text=df['Name'],
    name='Rapid Rating'
))
# Adding the trend line
fig3.add_trace(go.Scatter(
    x=df['X'],
    y=line_y3,
    mode='lines',
    marker=dict(color='black'),
    name=f'Trend Line (slope: {slope_y3:.2f})'
))
fig3.update_layout(
    title=f'Interactive Plot with Player Names for Rapid Rating (Slope: {slope_y3:.2f})',
    xaxis_title='FIDE Rating',
    yaxis_title='Rapid Rating',
    showlegend=True
)
fig3.show()
