import time

def test_retention_logic():
    """Verifies that the retention arithmetic correctly identifies and filters expired timestamps."""
    retention_ttl = 90 * 24 * 60 * 60  # 90 days in seconds
    now = time.time()
    
    fresh_entry = {"timestamp": now - 3600, "data": "1 hour old"}
    expired_entry = {"timestamp": now - (retention_ttl + 100), "data": "Over 90 days old"}
    
    mock_storage = [fresh_entry, expired_entry]
    
    # Simulate cleanup loop logic
    filtered_storage = [item for item in mock_storage if (now - item["timestamp"]) < retention_ttl]
    
    assert len(filtered_storage) == 1
    assert filtered_storage[0]["data"] == "1 hour old"
    print("✅ Retention mathematical filter test passed successfully.")
