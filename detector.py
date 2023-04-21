import datetime
import numpy as np
from collections import deque
from sklearn.ensemble import IsolationForest


class AdvancedAnomalyDetector:
    def __init__(self, threshold=10, time_window=60, train_interval=30, max_samples=1000):
        self.threshold = threshold
        self.time_window = time_window
        self.event_queue = deque()
        self.samples = deque(maxlen=max_samples)
        self.train_interval = train_interval
        self.last_trained = datetime.datetime.now()
        self.model = None

    def _train_model(self):
        if len(self.samples) < self.threshold * 2:
            return

        feature_matrix = np.array(self.samples)
        self.model = IsolationForest(contamination=float(self.threshold) / len(self.samples))
        self.model.fit(feature_matrix)

    def add_event(self, feature_vector):
        current_time = datetime.datetime.now()
        self.event_queue.append((current_time, feature_vector))
        self.samples.append(feature_vector)

        while (current_time - self.event_queue[0][0]).seconds > self.time_window:
            self.event_queue.popleft()

        if (current_time - self.last_trained).seconds > self.train_interval:
            self._train_model()
            self.last_trained = current_time

        if self.model is not None:
            prediction = self.model.predict([feature_vector])
            if prediction[0] == -1:
                print("Anomaly detected: unusual event pattern!")
                self.event_queue.clear()


