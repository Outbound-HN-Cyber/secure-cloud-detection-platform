from datetime import datetime

from security_platform.models.event import SecurityEvent


def test_security_event_can_be_created():
    event = SecurityEvent(
        timestamp=datetime.now(),
        source_ip="192.168.1.10",
        username="test-user",
        event_type="login",
        status="failed",
    )

    assert event.username == "test-user"
    assert event.status == "failed"