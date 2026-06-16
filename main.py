from uagents import Bureau
import config
from agents.storage_agent import storage_agent

# If you create more agents (e.g., an analytics agent), add them to this bureau
bureau = Bureau(port=config.PORT)
bureau.add(storage_agent)

if __name__ == "__main__":
    print("🚀 Initializing ASI Cloud Agent Ecosystem...")
    bureau.run()
