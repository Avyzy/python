class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        '''set Tv with defualt settings'''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        '''turning tv off and on'''
        self.__status = not self.__status

    def mute(self):
        '''mutes and unmutes when tv is on'''
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        '''channel goes up in number an resets when it hits max'''
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        '''channel goes down in number and go back to top when it hits min'''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        '''turns volume up only when unmuted'''
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        '''turns volume down only when unmuted'''
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        '''returns a tring with power, channel and volume'''
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
