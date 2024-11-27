from marcin_project import main


def test_main(spark):  # use pytester fixture
    taxis = main.get_taxis(spark)
    assert taxis.count() > 5
