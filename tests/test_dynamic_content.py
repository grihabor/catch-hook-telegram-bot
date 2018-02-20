import pytest

@pytest.mark.parametrize()
def test_dynamic_content():
    from catchbot.routes.content import get_dynamic_msg_content

    # get_dynamic_msg_content