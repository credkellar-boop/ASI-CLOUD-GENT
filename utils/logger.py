import logging
import json
import sys
from datetime import datetime

class StructuredJsonFormatter(logging.Formatter):
    def format(self, record):
        log_packet = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "logger_name": record.name
        }
        if hasattr(record, "security_event"):
            log_packet["security_event"] = record.security_event
        return json.dumps(log_packet)

def setup_production_logger(name: str = "asi_agent") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Avoid duplicate handlers if re-initialized
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(StructuredJsonFormatter())
        logger.addHandler(handler)
        
    return logger
