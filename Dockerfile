FROM python:3.12-slim

WORKDIR /anomaly_detection_app

COPY requirements.txt /anomaly_detection_app/
COPY data_generator.py /anomaly_detection_app/
COPY data_preprocess.py /anomaly_detection_app/
COPY train_pipeline.py /anomaly_detection_app/
COPY app.py /anomaly_detection_app/


RUN pip install -r /anomaly_detection_app/requirements.txt

EXPOSE 8000

CMD ["bash"]