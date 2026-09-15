from dataclasses import dataclass
from datetime import datetime


@dataclass
class SecurityEvent:
    timestamp: datetime
    source_ip: str
    username: str
    event_type: str
    status: str