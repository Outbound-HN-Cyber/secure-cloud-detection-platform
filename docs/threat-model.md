Initial Threat Model
Assets

The primary assets are:

Security event data
Detection rules
Security alerts
Authentication credentials
API access
Infrastructure configuration
Audit information
Threats
Threat	Target	Potential impact	Initial mitigation
Spoofed events	Event ingestion	False detections or missed attacks	Authentication and validation
Malicious event data	Event ingestion	Application compromise	Strict input validation
Alert tampering	Alert storage/API	Loss of detection integrity	Access controls and audit logging
Unauthorised API access	API	Exposure of security information	Authentication and authorisation
Credential exposure	Application	Unauthorised access	Environment-based secrets
Denial of service	API	Loss of detection capability	Rate limiting and resource controls
Privilege escalation	Application	Unauthorised actions	Least privilege
Dependency compromise	Application	Supply-chain risk	Dependency scanning and pinned versions
Container compromise	Runtime	Application/infrastructure compromise	Minimal images and container scanning
Security priorities

The highest priorities for the initial implementation are:

Protect the integrity of security events.
Prevent unauthorised access to security alerts.
Prevent credentials and secrets from entering source control.
Validate untrusted input.
Detect suspicious behaviour reliably.
Automate security testing.

The threat model will be updated as the architecture develops.