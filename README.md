# Real-Time-Fall-Detection-Using-AI
This project implements a real-time fall detection system using smartwatch sensor data and machine learning algorithms to monitor Activities of Daily Living (ADL) and detect fall events. Upon detection, the system sends instant alerts to caregivers or emergency contacts, enhancing safety for elderly or at-risk individuals.

🚀 Features
Real-time monitoring of motion data from smartwatch sensors (accelerometer, gyroscope)
Intelligent classification of ADL vs. fall events using ML models
Instant alert generation via Firebase and Android notifications
High accuracy with low false positives through feature engineering and model tuning
Lightweight and efficient for continuous background operation

🧠 Tech Stack
Python, scikit-learn, NumPy, Pandas
Bluetooth communication for smartwatch data acquisition
Firebase for real-time alert delivery
Android app for caregiver notifications
Optional: TensorFlow/Keras for deep learning models

📊 Methodology
Data Collection: Gathered motion data from smartwatch sensors during various ADL and simulated fall scenarios.
Preprocessing: Filtered noise, segmented time windows, and extracted statistical and frequency-domain features.
Model Training: Trained ML models (e.g., SVM, Decision Tree) to classify fall vs. non-fall events.
Deployment: Integrated model into a real-time pipeline with alerting mechanism.

📦 How to Run
Connect smartwatch and start data streaming via Bluetooth.
Run the Python script to process incoming data and classify activity.
If a fall is detected, an alert is sent via Firebase to the caregiver’s Android device.

📌 Applications
Elderly care and assisted living
Remote health monitoring
Workplace safety in hazardous environments
