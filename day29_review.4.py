class ModelTrainer:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify_all(self, name):
        for observer in self.observers:
            observer.alert(name)
class SlackAlert:
    def alert(self, name):
        print(f"SLACK: Model {name} training complete!")
class EmailAlert:
    def alert(self, name):
        print(f"EMAIL: Model {name} training complete!")
class LogAlert:
    def alert(self, name):
        print(f"LOG: Model {name} training complete!")

trainer = ModelTrainer()
trainer.subscribe(SlackAlert())
trainer.subscribe(EmailAlert())
trainer.subscribe(LogAlert())
trainer.notify_all("RandomForest")