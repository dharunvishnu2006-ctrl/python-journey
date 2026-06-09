class NetworkThreat:
    def detect(self):
        return "Network Attack Detected! Block IP immediately!"

class MalwareThreat:
    def detect(self):
        return "Malware Detected! Quarantine system!"

class SQLInjection:
    def detect(self):
        return "SQL Injection Detected! Block query!"

class ThreatFactory:
    def create_threat(self, threat_type):
        if threat_type == "network":
            return NetworkThreat()
        elif threat_type == "malware":
            return MalwareThreat()
        elif threat_type == "sql":
            return SQLInjection()
        else:
            return None

factory = ThreatFactory()
threat = factory.create_threat("network")
print(threat.detect())

threat2 = factory.create_threat("sql")
print(threat2.detect())        

class DatabaseConnection:
    _instance = None 
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("New DB Connection Created!")
        else:
            print("Reusing existing connection!")
        return cls._instance

db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1 is db2)  

class AlertSystem:
    def __init__(self):
        self.observers = []
    
    def subscribe(self, observer):
        self.observers.append(observer)
    
    def notify_all(self, threat):
        for observer in self.observers:
            observer.alert(threat)

class EmailAlert:
    def alert(self, threat):
        print(f"EMAIL: {threat} detected!")

class SMSAlert:
    def alert(self, threat):
        print(f"SMS: {threat} detected!")

class DashboardAlert:
    def alert(self, threat):
        print(f"DASHBOARD: {threat} detected!")

alert_system = AlertSystem()
alert_system.subscribe(EmailAlert())
alert_system.subscribe(SMSAlert())
alert_system.subscribe(DashboardAlert())

alert_system.notify_all("SQL Injection")

class RandomForestStrategy:
    def train(self, data):
        return f"Training with Random Forest on {len(data)} samples!"

class XGBoostStrategy:
    def train(self, data):
        return f"Training with XGBoost on {len(data)} samples!"

class NeuralNetStrategy:
    def train(self, data):
        return f"Training with Neural Network on {len(data)} samples!"

class AutoPilotML:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy):
        self.strategy = strategy
        print("Strategy switched!")
    
    def run_training(self, data):
        return self.strategy.train(data)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

autopilot = AutoPilotML(RandomForestStrategy())
print(autopilot.run_training(data))

autopilot.set_strategy(XGBoostStrategy())
print(autopilot.run_training(data))

autopilot.set_strategy(NeuralNetStrategy())
print(autopilot.run_training(data))