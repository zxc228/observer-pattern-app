from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, state):
        pass

class ConcreteObserver(Observer):
    def __init__(self, name, output_label, app_instance) -> None:
        self.name = name
        self.output_label = output_label
        self.app_instance = app_instance

    def update(self, state):
        message = f'{self.name} updated to state: {state}'
        print(message)
        self.output_label.config(text=message)
        self.app_instance.log_to_console(message)

