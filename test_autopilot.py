import pytest

def is_good_accuracy(accuracy):
    return accuracy >= 80.0

@pytest.mark.parametrize("accuracy, expected", [
    (95.0, True),
    (80.0, True),
    (79.9, False),
    (50.0, False),
    (100.0, True)
])
def test_accuracy(accuracy, expected):
    assert is_good_accuracy(accuracy) == expected

from unittest.mock import MagicMock

def send_security_alert(ip, email_service):
    response = email_service.send(ip)
    return response

def test_security_alert():
   
    mock = MagicMock()
    mock.send.return_value = "Security alert sent!"
    result = send_security_alert("192.168.1.1", mock)
    assert result == "Security alert sent!"
    mock.send.assert_called_once_with("192.168.1.1")

test_security_alert()
print("Mock test passed!")    