import joblib
import numpy as np

# Load the pre-trained model
model = joblib.load('svm_model.joblib')

import pandas as pd
from sklearn.preprocessing import StandardScaler

# Define categorical columns
cat_columns = ['blue', 'dual_sim', 'four_g', 'three_g', 'touch_screen', 'wifi']

def preprocess_features(data):
    df = pd.DataFrame([data])
    
    # Convert binary columns to a decimal feature
    def binary_to_decimal(row):
        binary_string = ''.join(str(int(x)) for x in row[cat_columns])
        return int(binary_string, 2)
    
    df['feature'] = df[cat_columns].apply(binary_to_decimal, axis=1)
    
    # Create new features
    df['pixel_area'] = df['px_height'] * df['px_width']
    df['screen_area'] = df['sc_h'] * df['sc_w']
    df['pcfc'] = df['pc'] * df['fc']
    
    # Drop unnecessary columns
    df.drop(['pc', 'fc', 'sc_h', 'sc_w', 'px_height', 'px_width', 'clock_speed', 'n_cores', 'blue', 'dual_sim', 'four_g', 'three_g', 'touch_screen', 'wifi'], axis=1, inplace=True)
    
    return df

def scale_features(df):
    # Define integer features for scaling
    integer_features = ['battery_power', 'pcfc', 'feature', 'ram', 'pixel_area', 'int_memory', 'mobile_wt', 'screen_area', 'talk_time']
    
    # Initialize the scaler
    scaler = StandardScaler()
    
    # Scale the integer features
    df[integer_features] = scaler.fit_transform(df[integer_features])
    
    return df

def predict_price(data):
    # Implement your prediction logic here
    prediction = model.predict(data)
    return prediction