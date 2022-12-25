# Research-Renewables_Matching

## Data Input

### Generator Data
- data/real_generation.csv - Formatted version of the original generation data
- data/real_generation_2x.csv - 2x scaled version of the original generation data
- data/real_generation_3x.csv - 3x scaled version of the original generation data
- data/real_generation_4x.csv - 4x scaled version of the original generation data

### Consumption Data
- data/real_consumption_all.csv - Formatted version of original consumption data
- data/real_consumption_minimal.csv - Selected and combined some datacenters to reduce difference in mean and median between datacenters and generators

## Data Output and Results
- try2/experience_ALGO_HARDWARE_DATASET_SCALING_PENALTY - Checkpoints for the trained models
- data/results/NUM_D NUM_G SCALING PENALTY raw.csv - Raw data and results from model evaluation
- data/results/NUM_D NUM_G SCALING PENALTY fig.csv - Data used to plot figures

## Model Training
- try2/run_gpu_A2C.py - Script used to train model
- try2/multi_env_single.py - Environment used for training

### Usage
- Example to use different algorithm is commented out as an example
- load a checkpoint uncomment the experience path and trainer.restore() lines
- To change model configs, add to the config dictionary

## Model Evaluation
- try2/rllib_eval_2.py - Script to drive model evaluation
- try2/multi_env_single_eval_2.py - Modified copy of multi_env_single to output raw evaluation data
- try2/figure_values.py - Script to convert raw evaluation data into statistics for plotting figures
