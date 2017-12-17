from psonic.samples.guitars import *


def test_guitars():
    sounds = get_sounds()
    assert isinstance(sounds, dict)
    results = [sound for name, sound in sounds.items()]
    for sound in results:
        assert isinstance(sound, Sample)
