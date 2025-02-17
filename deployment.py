import streamlit as st
import pandas as pd
import pickle
import plotly.express as px
from PIL import Image

# Set the Streamlit app layout to wide
st.set_page_config(layout="wide")

# Load the saved model
model_filename = "xgb_final_model.pkl"
with open(model_filename, "rb") as file:
    xgb_model = pickle.load(file)

# Load the feature importance data
feature_importance_file = "feature_importance.xlsx"
feature_importance_df = pd.read_excel(feature_importance_file)

# Sidebar setup
st.sidebar.header("Player Input Features")

# Default input values (from the first row of your example data)
default_values = {
    "Rk": 1,
    "Age": 28,
    "Born": 1997,  # 2025 yılı göz önüne alındığında
    "MP": 30,
    "Starts": 25,
    "Min": 2700,
    "90s": 30.0,
    "Goals": 10,
    "Shots": 20,
    "SoT": 8,
    "SoT%": 40.0,
    "G/Sh": 0.5,
    "G/SoT": 1.0,
    "ShoDist": 18.0,
    "ShoFK": 2,
    "ShoPK": 1,
    "PKatt": 2,
    "PasTotCmp": 50,
    "PasTotAtt": 60,
    "PasTotCmp%": 83.3,
    "PasTotDist": 300,
    "PasTotPrgDist": 80,
    "PasShoCmp": 30,
    "PasShoAtt": 35,
    "PasShoCmp%": 85.7,
    "PasMedCmp": 40,
    "PasMedAtt": 50,
    "PasMedCmp%": 80.0,
    "PasLonCmp": 20,
    "PasLonAtt": 25,
    "PasLonCmp%": 80.0,
    "Assists": 5,
    "PasAss": 6,
    "Pas3rd": 10,
    "PPA": 4,
    "CrsPA": 3,
    "PasProg": 15,
    "PasAtt": 70,
    "PasLive": 65,
    "PasDead": 5,
    "PasFK": 2,
    "TB": 1,
    "Sw": 0,
    "PasCrs": 7,
    "TI": 2,
    "CK": 4,
    "CkIn": 2,
    "CkOut": 2,
    "CkStr": 0,
    "PasCmp": 55,
    "PasOff": 0,
    "PasBlocks": 1,
    "SCA": 10,
    "ScaPassLive": 5,
    "ScaPassDead": 3,
    "ScaDrib": 2,
    "ScaSh": 4,
    "ScaFld": 2,
    "ScaDef": 1,
    "GCA": 8,
    "GcaPassLive": 4,
    "GcaPassDead": 2,
    "GcaDrib": 2,
    "GcaSh": 1,
    "GcaFld": 0,
    "GcaDef": 0,
    "Tkl": 20,
    "TklWon": 15,
    "TklDef3rd": 8,
    "TklMid3rd": 7,
    "TklAtt3rd": 5,
    "TklDri": 4,
    "TklDriAtt": 6,
    "TklDri%": 66.7,
    "TklDriPast": 2,
    "Blocks": 3,
    "BlkSh": 2,
    "BlkPass": 1,
    "Int": 5,
    "Tkl+Int": 25,
    "Clr": 10,
    "Err": 1,
    "Touches": 300,
    "TouDefPen": 15,
    "TouDef3rd": 50,
    "TouMid3rd": 100,
    "TouAtt3rd": 70,
    "TouAttPen": 5,
    "TouLive": 200,
    "ToAtt": 10,
    "ToSuc": 6,
    "ToSuc%": 60.0,
    "ToTkl": 3,
    "ToTkl%": 30.0,
    "Carries": 40,
    "CarTotDist": 500,
    "CarPrgDist": 100,
    "CarProg": 30,
    "Car3rd": 20,
    "CPA": 5,
    "CarMis": 2,
    "CarDis": 1,
    "Rec": 45,
    "RecProg": 20,
    "CrdY": 3,
    "CrdR": 0,
    "2CrdY": 0,
    "Fls": 5,
    "Fld": 8,
    "Off": 2,
    "Crs": 10,
    "TklW": 15,  # TklWon ile benzer olabilir
    "PKwon": 1,
    "PKcon": 1,
    "OG": 0,
    "Recov": 10,
    "AerWon": 8,
    "AerLost": 4,
    "AerWon%": 66.7
}


# Input fields in the sidebar with default values
player_inputs = {}
for col, default in default_values.items():
    if col == "Comp_Premier League":  # Boolean input
        player_inputs[col] = st.sidebar.selectbox(f"{col}", [True, False], index=int(default))
    else:  # Numeric input
        player_inputs[col] = st.sidebar.number_input(f"{col}", value=float(default))

# Convert inputs into a DataFrame for prediction
input_df = pd.DataFrame([player_inputs])

# Main page setup
st.title("Player Market Value Prediction")

# Create two columns for layout
left_col, right_col = st.columns(2)

# Left column: Feature Importance
with left_col:
    st.subheader("Feature Importance")
    fig = px.bar(
        feature_importance_df.sort_values("Feature Importance Score", ascending=True),
        x="Feature Importance Score",
        y="Variable",
        orientation="h",
        title="Feature Importance",
        labels={"Variable": "Features", "Feature Importance Score": "Importance"},
        width=700,  # Set custom width
        height=500  # Set custom height
    )
    st.plotly_chart(fig, use_container_width=False)  # Disable container width to respect custom size

# Right column: Prediction Result
with right_col:
    st.subheader("Predicted Market Value")
    if st.button("Predict Market Value"):
        # Make prediction
        prediction = xgb_model.predict(input_df)[0]
        st.success(f"Predicted Market Value: €{prediction:,.2f}")
    else:
        st.info("Enter inputs on the left and click 'Predict Market Value'.")


# python -m streamlit run deployment.py
