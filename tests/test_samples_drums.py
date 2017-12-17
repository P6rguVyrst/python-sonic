from psonic.samples.drums import *


def test_drums():
    sounds = get_sounds()
    assert isinstance(sounds, dict)
    results = [sound for name, sound in sounds.items()]
    for sound in results:
        assert isinstance(sound, Sample)
