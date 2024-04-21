class Subject:
    def __init__(self) -> None:
        self._observers = []
        self._state = 0
    
    def attach (self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def deatach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._state)
    
    def set_state(self, value):
        self._state = value
        self.notify()