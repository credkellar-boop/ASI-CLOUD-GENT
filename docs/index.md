# Welcome to the ASI Cloud Agent Ecosystem

This project implements an enterprise-ready, autonomous cloud worker built atop the Fetch.ai `uagents` framework for the Artificial Superintelligence (ASI) Alliance network. 

## Core Capabilities
- **Partitioned Local Storage:** Segregated execution logs for complete audit isolation.
- **90-Day Auto-Purge:** Automatic background garbage disposal tracking file ages down to the second.
- **Symmetric Data Encryption:** In-memory AES-256 Fernet protections for user records at rest.
- **Internal CSPM Auditor:** Scheduled infrastructure posture analysis to safeguard runtime configurations.

## System Prerequisites
Ensure you have the following installed on your host system:
- Python 3.11 or higher
- Docker & Docker Compose (Optional for containerized runtimes)
- A valid Fetch.ai Agentverse account (For mailbox proxy deployment)
