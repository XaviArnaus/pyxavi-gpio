from pyxavi import Config
from pyxavi_gpio.eink import EinkDisplay

# The config is meant to be a file, defined by `filename`.
#   But can also be used from a var defined by `params`, useful for tests.
#   It must be at least one of both.
#
# The Config expects definitions for the Display.
#   Otherwise, everything gets mocked by default.
#   Beware, the mocking creates PNG files, so you need write access to the disk.
CONFIG = {}


def create_config(params=CONFIG) -> Config:
    return Config(params=params)


def test_instantiate_minimal():
    instance = EinkDisplay(config=create_config())

    assert isinstance(instance, EinkDisplay)


def test_draw_test():
    instance = EinkDisplay(config=create_config())

    instance.test()
