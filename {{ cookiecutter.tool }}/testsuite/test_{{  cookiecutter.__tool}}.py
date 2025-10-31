import pytest
import numpy as np

from grass.tools import Tools


def test_output_exists(session):
    tools = Tools(session=session, consistent_return_value=False)
    output = tools.{{ cookiecutter.__tool }}(input="data", output=np.array)
    assert np.any(np.isnan(output))
