# System Architecture Blueprint

The ecosystem operates asynchronously by deploying independent protocol bundles inside a unified execution thread managed via the `uagents` Bureau module.

## Protocol Topology

1. **Storage Lifecycle Protocol (`protocols/storage_protocol.py`):** Coordinates inbound queries and structures data mutations inside `ctx.storage`.
2. **System Alert Protocol (`protocols/alert_protocol.py`):** Acts as an internal emergency bus. When validation steps or compliance audits fail, it handles asynchronous notifications.

## Data Persistence Flow
Every message transaction, user log import, or runtime action follows this linear pipeline:
`Inbound Network Packet` ➔ `Schema Validation` ➔ `Fernet Symmetric Encryption` ➔ `Storage Allocation Partition` ➔ `90-day TLL Garbage Filter Clock`.
