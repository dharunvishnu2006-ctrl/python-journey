class SignatureStrategy:
    def detect(self):
        return "Signature scan: Known threat found!"

class BehaviorStrategy:
    def detect(self):
        return "Behavior scan: Anomaly detected!"

class MLStrategy:
    def detect(self):
        return "ML scan: Predicted threat with 95% confidence!"
    
class ThreatDetector:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def run_detection(self):
        return self.strategy.detect()

detector = ThreatDetector(SignatureStrategy())
print(detector.run_detection())
detector.set_strategy(BehaviorStrategy())
print(detector.run_detection())
detector.set_strategy(MLStrategy())
print(detector.run_detection())