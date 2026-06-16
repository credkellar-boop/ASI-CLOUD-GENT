import os
import sys
import socket
import config

def run_infrastructure_audit() -> dict:
    """
    Scans the agent's internal configuration state and local environment
    to generate a defensive security compliance report.
    """
    report = {
        "compliant": True,
        "critical_findings": 0,
        "warnings": 0,
        "checks": []
    }
    
    # 1. Check for Default Seed Usage
    if config.AGENT_SEED == "default_fallback_seed_phrase_change_me":
        report["checks"].append({
            "id": "SEC-001",
            "name": "Cryptographic Seed Status",
            "status": "FAIL",
            "severity": "CRITICAL",
            "description": "Agent is running on a generic fallback seed phrase. Credentials vulnerable."
        })
        report["critical_findings"] += 1
        report["compliant"] = False
    else:
        report["checks"].append({
            "id": "SEC-001",
            "name": "Cryptographic Seed Status",
            "status": "PASS",
            "severity": "CRITICAL",
            "description": "Unique cryptographic seed string detected."
        })

    # 2. Audit Exposure of Communication Port
    if config.PORT == 8000:
        report["checks"].append({
            "id": "SEC-002",
            "name": "Network Port Allocation",
            "status": "WARN",
            "severity": "LOW",
            "description": "Agent is running on standard default port 8000. Consider obscure mapping in production."
        })
        report["warnings"] += 1
    
    # 3. Verify .env File Access Restrictions
    if os.path.exists(".env"):
        # Check permissions on Unix-like environments
        if sys.platform != "win32":
            file_mode = os.stat(".env").st_mode & 0o777
            if file_mode > 0o600:  # More permissive than owner read/write only
                report["checks"].append({
                    "id": "SEC-003",
                    "name": "Environment File Permissions",
                    "status": "WARN",
                    "severity": "MEDIUM",
                    "description": f"Local .env file permissions are too loose ({oct(file_mode)}). Restrict to owner read/write."
                })
                report["warnings"] += 1
                
    # 4. Check Endpoint Transport Security
    if config.ENDPOINT.startswith("http://"):
        report["checks"].append({
            "id": "SEC-004",
            "name": "Transport Layer Security",
            "status": "FAIL",
            "severity": "HIGH",
            "description": "Agent endpoint utilizes unencrypted HTTP protocol. Network packets can be sniffed."
        })
        report["critical_findings"] += 1
        report["compliant"] = False

    return report
