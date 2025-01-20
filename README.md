[Test task]

Logistic Regression model for anomaly detection in network traffic

1) Run container in interactive mode

2) Generate data with "python data_generator.py --num_samples 1000"

3) Train model with "python train_pipeline.py"

4) Check files updates: new directories encoders/ and models/ as well as new json file (generated data)

5) Finally run app in a container: "python app.py"

![Screenshot from 2025-01-20 13-49-32](https://github.com/user-attachments/assets/dbe182f3-78ac-4bbe-869e-f6ede00fde0d)

6) Send POST requests with /predict and /train

![Screenshot from 2025-01-20 13-49-52](https://github.com/user-attachments/assets/381e4b5b-ea07-4170-a7cb-a302278244c0)

7) Corresponding output from app in a container:

![Screenshot from 2025-01-20 13-49-43](https://github.com/user-attachments/assets/2dc82ddf-76a3-4d9d-b1ef-ed9f91cbbb98)

