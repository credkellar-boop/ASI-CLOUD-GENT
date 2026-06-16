from uagents import Protocol
from uagents import Model

class IncidentAlert(Model):
    severity: str
    component: str
    issue_details: str

alert_proto = Protocol(name="SystemAlertProtocol", version="1.0.0")
