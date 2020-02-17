import get_temp
import get_time


def tst1():
    gt1 = get_time.get_time()
    assert str(gt1)
    assert len(gt1) == 5


def tst2():
    gt2 = get_temp.get_temperature()
    assert int(gt2)


def test_temp():
    tst1()
    tst2()
