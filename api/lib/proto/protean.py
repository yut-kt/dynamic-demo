from abc import abstractmethod


class Protean:
    @abstractmethod
    def speak_word(self):
        raise NotImplementedError()
