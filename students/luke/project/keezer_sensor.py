#!/usr/bin/env python3


class KSensor:
    """ Sensor class for keezer management project """


    def __init__(self):
        """ Register self with driver """
        pass


    def poll_sensor(self):
        """ Return sensor reading """
        return True


if __name__ == "__main__":
    sns = KSensor()
    assert(sns.poll_sensor())
