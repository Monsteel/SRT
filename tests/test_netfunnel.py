import pytest

from SRT.netfunnel import NetFunnelHelper, SRTNetFunnelError


@pytest.fixture(scope="module")
def helper():
    return NetFunnelHelper()


def test_get_netfunnel_key_success(helper):
    try:
        key = helper.get_netfunnel_key(True)
    except SRTNetFunnelError as e:
        raise AssertionError()
    assert key is not None


def test_set_complete_success(helper):
    key = helper.get_netfunnel_key(True)
    try:
        helper.set_complete(key)
    except SRTNetFunnelError as e:
        raise AssertionError()
    assert True
