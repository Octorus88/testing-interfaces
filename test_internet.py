import socket
import pytest
import requests

REMOTE_HOST = '8.8.8.8'
URL = 'http://google.com'
LOCALHOST = '127.0.0.1'
PORT = 53
STATUS_CODE = 200


@pytest.fixture
def connection():
    return socket.create_connection((REMOTE_HOST, PORT))


def test_iface_info():
    iface_list = socket.if_nameindex()
    assert iface_list


def test_tcp_conn(connection):
    assert connection
    connection.close()


def test_http_status_code():
    response = requests.get(URL)
    assert response.status_code == STATUS_CODE
