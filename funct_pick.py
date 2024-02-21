# script_to_create_pickles.py
import pickle
import cv2  # Import the cv2 module

from preprocessing import retinex_transform, edge_enhancement, wavelet_fusion, preprocess_rgb

# Save preprocessing pipeline for multispectral images
preprocessing_pipeline_multispectral = [retinex_transform, edge_enhancement, wavelet_fusion, cv2.resize]
with open('preprocessing_pipeline_multispectral.pkl', 'wb') as f:
    pickle.dump(preprocessing_pipeline_multispectral, f)

# Save preprocessing pipeline for RGB images
preprocessing_pipeline_rgb = [preprocess_rgb]
with open('preprocessing_pipeline_rgb.pkl', 'wb') as f:
    pickle.dump(preprocessing_pipeline_rgb, f)

print("Preprocessing pipelines saved successfully.")
