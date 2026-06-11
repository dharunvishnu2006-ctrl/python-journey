import pytest

def is_suspicious(request_count):
    return request_count > 1000

def test_suspicious_high():
    assert is_suspicious(1500) == True

def test_suspicious_low():
    assert is_suspicious(200) == False

@pytest.mark.parametrize("count, expected", [
    (1500, True),
    (200, False),
    (1000, False),
    (1001, True),
    (0, False)
])
def test_suspicious_parametrize(count, expected):
    assert is_suspicious(count) == expected

from unittest.mock import patch, MagicMock

def send_alert(ip, alert_service):
    response = alert_service.send(ip)
    return response

def test_send_alert():
    mock_service = MagicMock()
    mock_service.send.return_value = "Alert sent!"

    result = send_alert("192.168.1.1", mock_service)

    assert result == "Alert sent!"
    mock_service.send.assert_called_once_with("192.168.1.1")
    print("Mock test passed!")

test_send_alert()