from setuptools import setup

setup(
    name='midi_rec_service',
    version='0.0.1',
    packages=['midi_rec_service', 'midi_rec_service.CK_rec'],
    install_requires=[
        'python-rtmidi',
        'mido'
    ],
    entry_points={
        'console_scripts': [
            'midirec = midi_rec_service.midisrv:main'
        ]
    }
)