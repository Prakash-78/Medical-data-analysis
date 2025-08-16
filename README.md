# Medical-data-analysis
This project analyzes patient health data to visualize key indicators and uncover correlations related to cardiovascular disease. It follows the structure of the freeCodeCamp Medical Data Visualizer project.

📊 Features
BMI Calculation & Overweight Flag Adds an overweight column based on BMI > 25.

Data Normalization Converts cholesterol and gluc values to binary:

0 = good

1 = bad (values > 1)

Categorical Plot Uses sns.catplot() to show counts of health indicators (cholesterol, gluc, smoke, alco, active, overweight) split by cardio status.

Heatmap Visualization Cleans data by removing outliers and incorrect entries, then plots a correlation matrix using sns.heatmap().

🧪 Data Cleaning Rules
ap_lo must be ≤ ap_hi

Height and weight must be within the 2.5th–97.5th percentile range

📁 Files
medical_examination.csv: Input dataset

medical_data_visualizer.py: Main script

test_module.py: Unit tests

📷 Visual Outputs
draw_cat_plot(): Bar chart of categorical features

draw_heat_map(): Correlation heatmap of cleaned data
