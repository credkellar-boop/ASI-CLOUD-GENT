# ASI Autonomous Cloud Agent Ecosystem

An autonomous cloud agent built on top of the Fetch.ai `uagents` framework for the **Artificial Superintelligence (ASI) Alliance** network. This agent contains localized partitioned storage clusters and a rolling 90-day automatic data retention and garbage purging engine.

## 🗄️ Storage Partitioning Layout
- `sent_info`: Tracks outgoing message payloads and confirmations.
- `received_info`: Logs inbound command payloads.
- `user_import_logs`: Dedicated isolated space for direct user log imports.
- `action_logs`: Operational system execution trace steps.

## 🚀 Getting Started

1. Clone this repository and run the automated setup utility script:
   ```bash
   chmod +x setup.sh
   ./setup.sh
