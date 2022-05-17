import usb.core
import usb.util
import pytest


@pytest.fixture
def device():
    return usb.core.find(idVendor=0x8457, idProduct=0x10263)


@pytest.fixture
def interface(device):
    cfg = device.get_active_configuration()
    intf = cfg[(0, 0)]
    return intf


@pytest.fixture
def endpoint(interface):
    ep = usb.util.find_descriptor(
        interface,
        custom_match= \
            lambda e: \
                usb.util.endpoint_direction(e.bEndpointAddress) == \
                usb.util.ENDPOINT_OUT)
    return ep


def test_device(device):
    assert device


def test_interface(interface):
    assert interface


def test_endpoint(endpoint):
    assert endpoint


def test_write(endpoint):
    endpoint.write('test')
