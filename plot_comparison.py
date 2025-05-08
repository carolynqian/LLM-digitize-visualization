# Basic Streamlit example (install with: pip install streamlit)
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pandas as pd
from model_data_dict import all_model_data
st.title("LLM Plot Digitization Evaluation")

# Select which graph to display
graph_selection = st.selectbox(
    "Select Graph", 
    all_model_data.keys()
)

# Load appropriate data and images based on selection
img_path = all_model_data[graph_selection]['metadata']['img_path']
x_range = all_model_data[graph_selection]['metadata']['x_range']
y_range = all_model_data[graph_selection]['metadata']['y_range']
x_label = all_model_data[graph_selection]['metadata']['x_label']
y_label = all_model_data[graph_selection]['metadata']['y_label']
model_data = all_model_data[graph_selection]['model_data']

# Load the image
img = mpimg.imread(img_path)

# Create multiselect for model selection
selected_models = st.multiselect(
    "Select Models to Display",
    list(model_data.keys()),
    default=list(model_data.keys())[0]
)

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(img, extent=[x_range[0], x_range[1], y_range[0], y_range[1]], 
          aspect='auto', alpha=0.5, zorder=0)

# Plot selected models
for model in selected_models:
    data = model_data[model]
    ax.scatter(data['x'], data['y'], s=50, label=model)

ax.set_xlim(x_range)
ax.set_ylim(y_range)
ax.set_xlabel(x_label)  # Example x-axis label
ax.set_ylabel(y_label)       # Example y-axis label
ax.legend()

# Display the plot
st.pyplot(fig)

# Display data as table
st.subheader("Data Table")
for model in selected_models:
    data = model_data[model]
    df = pd.DataFrame({
        'X': data['x'],
        'Y': data['y']
    })
    st.write(f"**{model}**")
    st.dataframe(df, use_container_width=True)

# Optional: Show error metrics
if st.checkbox("Show Error Metrics"):
    error_metrics = {
        # Your error calculations
    }
    st.write(error_metrics)