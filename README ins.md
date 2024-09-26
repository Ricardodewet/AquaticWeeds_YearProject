# Water Hyacinth Prediction Project

## Project Overview

This project aims to predict the growth and spread of water hyacinth at Hartbeespoort Dam using machine learning models. By leveraging **Convolutional Neural Networks (CNNs)** for image classification and **Long Short-Term Memory (LSTM)** networks for time-series forecasting based on environmental data, we aim to provide accurate and reliable predictions.

## Project Structure


## Setup Instructions
-----------------------------------------------------------------------------------------------------------
### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/water_hyacinth_project.git


-----------------------------------------------------------------------------------------------------------
# 2. Set Up the Virtual Environment

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
-----------------------------------------------------------------------------------------------------------
# 3. Install Dependencies

pip install -r requirements.txt
-----------------------------------------------------------------------------------------------------------
#4. Prepare the Data

Images: Place your training images in the data/images/ folder.
Environmental Data: Make sure the environmental_data.csv file contains the required weather data.
-----------------------------------------------------------------------------------------------------------
#5. Train the Models

Train the CNN model for image classification:

python scripts/train_cnn.py

# Train the LSTM model for environmental predictions:

python scripts/train_lstm.py
----------------------------------------------------------------------------------------------------------
#6. Make Predictions

Use the prediction.py script to make predictions based on new images and environmental data:

python scripts/prediction.py

----------------------------------------------------------------------------------------------------------

Models and Approach:

CNN Model (Convolutional Neural Network)
The CNN model processes high-resolution images of Hartbeespoort Dam to classify areas affected by water hyacinth.
LSTM Model (Long Short-Term Memory)
The LSTM model is used for predicting future hyacinth spread based on historical environmental data (temperature, wind speed, humidity).
-----------------------------------------------------------------------------------------------------------
Dependencies:

The project requires the following Python libraries:

tensorflow
numpy
pandas
scikit-learn
matplotlib (optional, for data visualization)
-----------------------------------------------------------------------------------------------------------

Contributing:

- Fork the repository
- Create your feature branch:
-git checkout -b feature-name
-Commit your changes:
-git commit -m "Add feature"
-Push to the branch:
-git push origin feature-name
-Submit a pull request