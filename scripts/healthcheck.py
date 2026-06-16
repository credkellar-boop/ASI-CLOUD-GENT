import sys
import httpx

def run_container_healthcheck():
    """Hits the management server's internal status route to verify container health."""
    try:
        # Check standard endpoint configured inside local server setup
        response = httpx.get("http://127.0.0.1:8000/status", timeout=2.0)
        if response.status_code == 200:
            sys.exit(0)  # Container is healthy
        sys.exit(1)      # Container server encountered errors
    except Exception:
        sys.exit(1)      # Management API is completely unresponsive

if __name__ == "__main__":
    run_container_healthcheck()
