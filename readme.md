# Student Performance Indicator
 

 ## Overview
 

 This project aims to predict student performance based on various factors. It includes data ingestion, data transformation, model training, and prediction pipelines.
 

 ## Project Structure
 

 ```
 .
 ├── .gitignore
 ├── app.py                       # Flask application for prediction
 ├── requirements.txt             # Project dependencies
 ├── setup.py                     # Installation script
 ├── artifacts/                   # Contains data, models, and preprocessors
 ├── logs/                        # Log files
 ├── notebook/                    # Jupyter notebooks for EDA and model training
 ├── src/                         # Source code
 │   ├── components/              # Data ingestion, transformation, and model training components
 │   ├── pipeline/                # Training and prediction pipelines
 │   ├── exception.py             # Custom exception handling
 │   ├── logger.py                # Logging functionality
 │   └── utils.py                 # Utility functions
 └── student_performance_indicator.egg-info/
 ```
 

 ## Setup
 

 1.  Clone the repository:
 

  ```bash
  git clone [<repository\_url>](https://github.com/Himank-Khatri/Student-Performance-Indicator)
  ```
 

 2.  Create a virtual environment:
 

  ```bash
  conda create -n student\_performance python=3.8
  conda activate student\_performance
  ```
 

 3.  Install the dependencies:
 

  ```bash
  pip install -r requirements.txt
  ```
 

 ## Usage
 

 1.  **Data Preparation:**
 

  -   The dataset `StudentsPerformance.csv` is located in the `notebook/data/` directory.
 

 2.  **Training the Model:**
 

  -   Run the training pipeline:
 

  ```bash
  python src/pipeline/train_pipeline.py
  ```
 

 3.  **Making Predictions:**
 

  -   Run the prediction pipeline using the Flask application:
 

  ```bash
  python app.py
  ```
 

  -   Access the application in your browser at `http://127.0.0.1:5000`
 

 ## Notebooks
 

 -   `1. EDA.ipynb`: Exploratory Data Analysis notebook.
 -   `2. model_training.ipynb`: Model training and evaluation notebook.
 

 ## Artifacts
 

 -   `artifacts/data.csv`: Processed data used for training.
 -   `artifacts/model.pkl`: Trained model.
 -   `artifacts/preprocessor.pkl`: Preprocessor object.
 

 ## Logging
 

 -   Log files are stored in the `logs/` directory.
 

 ## License
 

 This project is licensed under the [MIT License](LICENSE).
