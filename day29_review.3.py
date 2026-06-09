class ModelRegistry:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ModelRegistry, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "models"):
            self.models = []

    def add_model(self, model_name):
        self.models.append(model_name)

    def get_models(self):
        return self.models

registry1 = ModelRegistry()
registry2 = ModelRegistry()

registry1.add_model("RandomForest")
registry2.add_model("XGBoost")

print(registry1.get_models())
print(registry2.get_models())
print(registry1 is registry2)