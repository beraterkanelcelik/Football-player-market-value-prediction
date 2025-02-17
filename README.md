# Football-player-market-value-prediction

This project is a Streamlit-based web application that predicts the market value of a player using a pre-trained XGBoost model. The app accepts various player statistics as input, outputs a predicted market value, and displays an interactive visualization of feature importance.

## Features

- **Player Input**: Easily input various player statistics via the sidebar.
- **Market Value Prediction**: Utilizes a pre-trained XGBoost model to predict the player's market value.
- **Feature Importance Visualization**: Displays an interactive bar chart (via Plotly) of the feature importance scores.
- **Interactive Web Interface**: Built with Streamlit for a user-friendly experience.

## Project Files

- **deployment.py**: Main Streamlit application that loads the model, reads input features, and displays predictions along with a feature importance chart.
- **xgb_final_model.pkl**: The pre-trained XGBoost model file used for prediction.
- **feature_importance.xlsx**: Excel file containing the feature importance data.
- **PlayerValueMarketPrediction.ipynb**: Jupyter Notebook used for training the model and experimenting with predictions.
- **player_data_with_pred.xlsx**, **player_market_values.csv**, **Player_Stats.csv**: Additional data files used in the project.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git

### Navigate into the project directory:
cd your-repo-name

### Install the required dependencies:
pip install -r requirements.txt

### Usage
Run the Streamlit application:
streamlit run deployment.py

### Interact with the app:
- Use the sidebar to input player statistics.
- Click the Predict Market Value button to generate a prediction.
- View the feature importance chart to see which variables most influence the prediction.
