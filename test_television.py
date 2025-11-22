from television import Television


def test_init_values():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_power_toggle():
    tv = Television()
    tv.power()
    assert "Power = True" in str(tv)
    tv.power()
    assert "Power = False" in str(tv)


def test_channel_up_wrap():
    tv = Television()
    tv.power()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert "Channel = 0" in str(tv) or "Channel = 1" in str(tv)


def test_volume_up_unmute():
    tv = Television()
    tv.power()
    tv.mute()
    tv.volume_up()
    assert "Volume = 1" in str(tv)
