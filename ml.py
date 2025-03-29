import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
data = pd.read_csv('datas.csv')

# Strip any leading/trailing whitespace from column names
data.columns = data.columns.str.strip()

# Fill missing values with 0 (for MYILADUTHURAI)
data.fillna(0, inplace=True)

# Select features and target variable
X = data[['Total Accidents 2021', 'Total Accidents 2022']]
y = data['Total Accidents 2023']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Function to generate and save the graph
def generate_graph(location_name):
    location_data = data[data['Location'] == location_name]
    if location_data.empty:
        return False
    
    # Predict the total accidents for 2023
    predicted_accidents = model.predict([location_data[['Total Accidents 2021', 'Total Accidents 2022']].values[0]])
    
    # Data for the bar chart
    years = ['2021', '2022', '2023']
    accidents = [location_data['Total Accidents 2021'].values[0], location_data['Total Accidents 2022'].values[0], predicted_accidents[0]]
    
    # Plotting the data as a bar chart
    plt.figure(figsize=(10, 6))
    bars = plt.bar(years, accidents, color=['skyblue', 'lightgreen', 'salmon'])
    
    # Add labels and title
    plt.title(f'Accident Trend in {location_name}', fontsize=16, fontweight='bold')
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Total Accidents', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Add value labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', 
                 ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    # Save the graph as an image
    plt.savefig('static/graph.png')
    plt.close()
    
    return True