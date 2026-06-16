#!/bin/bash

echo "⚙️ Setting up your ASI Cloud Agent workspace..."

# Create Python virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install requirements
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
else
    echo "⚠️ requirements.txt not found. Installing core packages..."
    pip install uagents python-dotenv
    pip freeze > requirements.txt
fi

# Initialize environment file if missing
if [ ! -f .env ]; then
    echo "Creating .env configuration from template..."
    echo 'ASI_AGENT_SEED="generate_a_random_secure_seed_phrase_here"' > .env
    echo 'AGENT_PORT=8000' >> .env
    echo 'AGENT_ENDPOINT="http://127.0.0.1:8000/submit"' >> .env
fi

echo "✅ Environment configured! Run 'source .venv/bin/activate && python main.py' to launch."
