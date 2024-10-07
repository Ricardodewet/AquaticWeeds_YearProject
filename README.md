# AquaticWeeds_YearProject

This is the repository where the group members of the Aquatic Weeds Group 6 will collaborate on and save the code that is necessary to complete the project. 

It is recommended for each member to have the [GitHub Desktop application](https://desktop.github.com/download/) installed on their personal computer to make the pull & push actions easier. 

Please leave comments while you are coding so that whoever wants to pick up where you left off can do so without any struggles. Also, specify in the details block what you have done and give a proper name to your update each time that you commit any new changes.

Thank you for your teamwork! Please ask for help where you need it. Let's do this thing!

## Project Overview

This project aims to predict the growth and spread of water hyacinth at Hartbeespoort Dam using machine learning models. By leveraging **Convolutional Neural Networks (CNNs)** for image classification and **Long Short-Term Memory (LSTM)** networks for time-series forecasting based on environmental data, we aim to provide accurate and reliable predictions.

## Project Structure

```
AquaticWeeds_YearProject/
│
├── data/                     # Data folder
│   ├── images/               # Folder for training images
│   └── environmental_data.csv # File containing environmental data
│
├── scripts/                  # Scripts for training and prediction
│   ├── train_cnn.py          # Script for training the CNN model
│   ├── train_lstm.py         # Script for training the LSTM model
│   └── prediction.py         # Script for making predictions
│
├── models/                   # Folder for storing trained models
│   ├── cnn_model.h5          # Trained CNN model
│   └── lstm_model.h5         # Trained LSTM model
│
└── requirements.txt          # File for listing project dependencies
```

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/your-repo/aquaticweeds_yearproject.git
```

### 2. Navigate to the Project Directory

Change to the project directory:

```bash
cd aquaticweeds_yearproject
```

### 3. Set Up the Virtual Environment

Create a virtual environment to manage dependencies:

```bash
python -m venv venv
```

Activate the virtual environment:

- **On Windows:**
  ```bash
  venv\Scripts\activate
  ```

- **On macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies

With the virtual environment activated, install the required Python libraries:

```bash
pip install -r requirements.txt
```

### 5. Prepare the Data

- **Images:** Place your training images in the `data/images/` folder. Ensure that images are properly labeled and formatted.
- **Environmental Data:** Ensure the `environmental_data.csv` file contains the required weather data with appropriate columns for analysis.

### 6. Train the Models

- Train the CNN model for image classification by running:

```bash
python scripts/train_cnn.py
```

- Train the LSTM model for environmental predictions by running:

```bash
python scripts/train_lstm.py
```

### 7. Make Predictions

Use the `prediction.py` script to make predictions based on new images and environmental data:

```bash
python scripts/prediction.py
```

## Models and Approach

### CNN Model (Convolutional Neural Network)

The CNN model processes high-resolution images of Hartbeespoort Dam to classify areas affected by water hyacinth.

### LSTM Model (Long Short-Term Memory)

The LSTM model is used for predicting future hyacinth spread based on historical environmental data (temperature, wind speed, humidity).

## Dependencies

The project requires the following Python libraries:

- tensorflow
- numpy
- pandas
- scikit-learn
- matplotlib (optional, for data visualization)

## Contributing

To contribute to the project, please follow these steps:

1. Fork the repository.
2. Create your feature branch:

   ```bash
   git checkout -b feature-name
   ```

3. Commit your changes:

   ```bash
   git commit -m "Add feature"
   ```

4. Push to the branch:

   ```bash
   git push origin feature-name
   ```

5. Submit a pull request.
