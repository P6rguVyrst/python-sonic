from psonic.samples.tabla import *

def test_tabla():
    sounds = get_sounds()
    assert isinstance(sounds, dict)
    results = [sound for name, sound in sounds.items()]
    for sound in results:
        assert isinstance(sound, Sample)
