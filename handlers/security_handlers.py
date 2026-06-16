from uagents import Context
from protocols.storage_protocol import storage_proto
from utils.security_auditor import run_infrastructure_audit
from utils.helpers import append_to_bucket

# Run a full infrastructure compliance audit every 12 hours
AUDIT_INTERVAL_SECONDS = 43200.0 

@storage_proto.on_interval(period=AUDIT_INTERVAL_SECONDS)
async def scheduled_security_scan(ctx: Context):
    ctx.logger.info("🛡️ Initiating scheduled internal infrastructure security audit...")
    
    # Run the configuration check
    audit_results = run_infrastructure_audit()
    
    # Log the output payload to your persistent storage architecture
    append_to_bucket(
        ctx=ctx,
        bucket_name="action_logs",
        action="SECURITY_COMPLIANCE_SCAN",
        metadata={
            "compliant": audit_results["compliant"],
            "critical_issues": audit_results["critical_findings"],
            "warnings_found": audit_results["warnings"],
            "full_log": audit_results["checks"]
        }
    )
    
    if not audit_results["compliant"]:
        ctx.logger.warning(
            f"⚠️ Security Audit Failed! Found {audit_results['critical_findings']} critical compliance errors."
        )
    else:
        ctx.logger.info("✅ Security Audit Passed. System meets baseline cloud posture requirements.")
