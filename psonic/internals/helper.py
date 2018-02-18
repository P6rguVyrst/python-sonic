from psonic.synthesizers import SAW

class ActiveSettings(object):
    def __init__(self, current_synth=SAW):
        print(f'using synth {current_synth}')
        self._current_synth = current_synth
    @property
    def current_synth(self):
        return self._current_synth
    def __get__(self):
        print(f'returning {self._current_synth}')
        return self._current_synth
    def __set__(self, synth):
        print(f'setting {synth}')
        self._current_synth = synth



