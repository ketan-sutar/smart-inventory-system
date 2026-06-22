from .models import AuditLog


def create_audit_log(
    user,
    action,
    entity,
    entity_id,
    description
):

    AuditLog.objects.create(
        user=user,
        action=action,
        entity=entity,
        entity_id=entity_id,
        description=description
    )