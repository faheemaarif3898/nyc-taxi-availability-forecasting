# NYC Taxi Availability Forecasting (Zone-Level)

## Overview
This project focuses on forecasting short-term taxi availability in New York City using historical NYC Yellow Taxi trip data.  
Rather than attempting to predict individual driver behavior, the project models **zone-level taxi availability** as a time-series forecasting problem.

Taxi availability is approximated using **drop-off events**, since a taxi becomes available immediately after completing a trip.

---

## Dataset Description
The dataset used is the NYC Yellow Taxi Trip dataset, which contains records of completed taxi trips including:
- pickup and drop-off timestamps
- drop-off latitude and longitude
- trip-level metadata

Important limitations of the dataset:
- No driver identifiers
- No online/offline status
- No explicit idle-time information

As a result, driver-level availability cannot be modeled directly.  
This project instead focuses on **aggregate supply patterns**.

---

## Problem Formulation
The forecasting task is defined as:

> Given historical drop-off patterns in a specific zone, predict how many taxis will become available in that zone after a fixed future time window.

Key design decisions:
- Availability is defined using **future drop-off counts**
- Forecasting is performed at the **zone + time-bin level**
- The prediction horizon is **30 minutes**

---

## Data Aggregation and Time Binning
- Drop-off timestamps are converted into fixed **15-minute time bins**
- Trips are aggregated by:
  - drop-off latitude
  - drop-off longitude
  - time bin
- Each row represents the number of taxis becoming available in a zone during that interval

Time binning aligns the data with real-world operational dynamics and removes second-level noise.

---

## Target Construction
The target variable is constructed by shifting aggregated drop-off counts forward in time:

- Target = number of drop-offs in the next 30 minutes
- Implemented as a forward shift of two 15-minute bins

This converts historical observations into a supervised forecasting problem without inventing labels.

---

## Feature Engineering
Only features with clear temporal or spatial relevance were included:

### Lag Features
Lagged drop-off counts capture short-term system memory:
- `lag_1` → previous 15 minutes
- `lag_2` → previous 30 minutes
- `lag_4` → previous 1 hour
- `lag_8` → previous 2 hours

These encode inertia and momentum in taxi supply patterns.

### Time-Based Features
- hour of day
- day of week
- weekend indicator

These capture daily and weekly periodicity in demand and supply.

### Spatial Features
- drop-off latitude
- drop-off longitude

Spatial features allow the model to learn zone-specific behavior without requiring explicit zone identifiers.

---

## Model
The final model used is **LightGBMRegressor**, chosen for its effectiveness on tabular data with temporal features.

Reasons for choosing LightGBM:
- Handles nonlinear interactions efficiently
- Scales well with large datasets
- Performs well for short-horizon forecasting tasks

---

## Evaluation Strategy
- Time-based train–validation split
- No random splitting to avoid data leakage
- Evaluation metrics:
  - Mean Absolute Error (MAE)
  - Root Mean Squared Error (RMSE)

The model is evaluated only on future time windows relative to training data.

---

## Key Learnings
This project demonstrates:
- How to derive meaningful prediction targets from incomplete real-world data
- The importance of aligning data granularity with the prediction task
- Why temporal structure must be explicitly encoded for tree-based models
- How increasing the forecasting horizon reveals deeper patterns beyond short-term persistence

---

## Project Structurenyc-taxi-availability-forecasting/ 
nyc-taxi-availability-forecasting/
│
├── src/
│   ├── config.py
│   ├── data_preparation.py
│   ├── feature_engineering.py
│   ├── model.py
│   ├── train.py
│   └── evaluate.py
│
├── README.md
└── run_pipeline.py
---

## Future Improvements
- Experiment with longer forecasting horizons (45–60 minutes)
- Incorporate rolling statistics
- Compare against classical time-series models
- Extend to multi-month datasets
