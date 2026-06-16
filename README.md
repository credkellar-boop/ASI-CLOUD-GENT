# 🤖 ASI Autonomous Cloud Agent Ecosystem

[![GitHub License](https://img.shields.io/github/license/credkellar-boop/ASI-CLOUD-GENT?color=blue&style=for-the-badge)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.11+-purple?style=for-the-badge&logo=python)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-uAgents-orange?style=for-the-badge)](https://fetch.ai/)
[![CI Status](https://img.shields.io/github/actions/workflow/status/credkellar-boop/ASI-CLOUD-GENT/ci.yml?branch=main&style=for-the-badge&logo=github-actions)](../../actions)
[![Security](https://img.shields.io/badge/Security-Bandit%20Passed-brightgreen?style=for-the-badge&logo=shield)](../../actions)

An enterprise-ready, autonomous cloud worker built atop the **Fetch.ai uagents framework** for the **Artificial Superintelligence (ASI) Alliance** network. This system delivers decentralized storage orchestration, secure local file partitioning, a rolling 90-day automatic data purging engine, and real-time management via WebSockets.

---

## 🛠️ Tech Stack Matrix

| Layer | Technologies |
| :--- | :--- |
| **Core Framework** | Python 3.11+, Fetch.ai `uagents` SDK, `uagents-ai` |
| **API & Control Plane** | FastAPI, Uvicorn, WebSockets (ASGI), Pydantic v2 |
| **Data & Cryptography** | Cryptography (`Fernet` AES-256 Symmetric Encryption), Local JSON Partitions, SQLite3 Cold Archive |
| **DevOps & Infrastructure** | Docker, Docker Compose, Kubernetes (Deployments, Services, Secrets) |
| **Testing & CI/CD** | Pytest, Pytest-Cov, GitHub Actions, Bandit (SAST), Pre-Commit, Black |

---

## 📐 System Architecture

The ecosystem splits operational logic into separate protocol boundaries handled concurrently inside a central execution runtime loop.

```text
                  [ Inbound Network Requests ]
                                │
                                ▼
                       ┌─────────────────┐
                       │   FastAPI API   │ ──(WebSocket Streaming)──► Live UI
                       │  & Rate Limiter │
                       └─────────────────┘
                                │
                                ▼
             ┌─────────────────────────────────────┐
             │   uAgents Bureau Execution Engine   │
             └─────────────────────────────────────┘
                 │                             │
                 ▼                             ▼
     ┌──────────────────────┐       ┌──────────────────────┐
     │  Storage Lifecycle   │       │ System Alert Bus     │
     │  Protocol            │       │ Protocol             │
     └──────────────────────┘       └──────────────────────┘
                 │                             │
        (AES-256 Encryption)                   ▼
                 │                   [ External Webhooks ]
                 ▼                       (Slack, Teams)
      ┌──────────────────────┐
      │  Partitioned Local   │
      │  Context Memory      │
      └──────────────────────┘
                 │
      (90-Day Purge & Cold DB)
                 │
                 ▼
     [ Local Cold Storage Archive ]
