from lmctv import determine_watch_method


def test_determine_watch_method():
    assert ('cablevision', None) == determine_watch_method('cablevision')
    assert ('verizon', None) == determine_watch_method('verizon')

    assert ('cablevision', 75) == determine_watch_method('75')
    assert ('cablevision', 76) == determine_watch_method('76')
    assert ('cablevision', 77) == determine_watch_method('77')

    assert ('verizon', 34) == determine_watch_method('34')
    assert ('verizon', 35) == determine_watch_method('35')
    assert ('verizon', 36) == determine_watch_method('36')

    assert ('online', None) == determine_watch_method('online')
    assert ('online', None) == determine_watch_method('site')
    assert ('online', None) == determine_watch_method('web')

    assert ('roku', None) == determine_watch_method('roku')
    assert ('roku', None) == determine_watch_method("I'm watching on Roku")
    assert ('roku', None) == determine_watch_method('on roku')

    assert ('youtube', None) == determine_watch_method('watching YouTube')
    assert ('youtube', None) == determine_watch_method('watching youtube')
