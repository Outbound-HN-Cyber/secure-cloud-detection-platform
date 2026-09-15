# Architecture

## High-level architecture

```text
                    Security Events
                          │
                          ▼
                 ┌─────────────────┐
                 │ Event Ingestion │
                 │     Service     │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Event Validation│
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │    Detection    │
                 │     Engine      │
                 └────────┬────────┘
                          │
                    Suspicious?
                     /        \
                   No          Yes
                   │            │
                   │            ▼
                   │    ┌───────────────┐
                   │    │  Risk Scoring │
                   │    └───────┬───────┘
                   │            │
                   │            ▼
                   │    ┌───────────────┐
                   │    │ Security Alert│
                   │    └───────┬───────┘
                   │            │
                   └──────┬─────┘
                          │
                          ▼
                   ┌─────────────┐
                   │     API     │
                   └──────┬──────┘
                          │
                          ▼
                    Dashboard / 
                    Security Team
```

## Components

### Event ingestion

Receives structured security events from simulated applications and services.

### Event validation

Validates the structure and content of incoming events before processing.

### Detection engine

Evaluates events against security detection rules.

### Risk scoring

Prioritises detections according to severity, confidence and contextual information.

### Alerting

Produces structured alerts containing the detection, severity, evidence and recommended response.

### API

Provides controlled access to events and alerts.

### Infrastructure

The platform will initially run locally using Docker and will subsequently be deployed using infrastructure as code.

## Engineering principles

The system will prioritise:

* Secure-by-design development
* Least privilege
* Separation of responsibilities
* Input validation
* Automated testing
* Reproducible infrastructure
* Observability
* Maintainability
