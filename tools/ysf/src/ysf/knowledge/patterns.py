from __future__ import annotations

CAPABILITY_PATTERNS: dict[str, tuple[str, ...]] = {
    "platform-foundation": (
        "platform foundation",
        "shared kernel",
        "repository architecture",
        "module architecture",
        "configuration architecture",
        "deployment architecture",
    ),
    "identity-access": (
        "identity",
        "authentication",
        "authorization",
        "access control",
        "permission",
        "role",
        "security architecture",
    ),
    "organization-tenant": (
        "organization",
        "tenant",
        "inheritance",
        "partner",
        "agency",
    ),
    "product-catalog": (
        "product",
        "catalog",
        "package",
        "inventory",
        "resource",
        "esim stock",
    ),
    "pricing-commercial": (
        "pricing",
        "price",
        "commercial",
        "commission",
        "promotion",
    ),
    "commerce-experience-platform": (
        "commerce experience",
        "cxp",
        "storefront",
        "store builder",
        "theme",
        "publishing",
        "landing page",
    ),
    "checkout-order": (
        "checkout",
        "cart",
        "quote",
        "sales order",
        "order",
        "fulfillment",
    ),
    "payment-finance": (
        "payment",
        "billing",
        "ledger",
        "settlement",
        "financial",
    ),
    "crm-customer-care": (
        "crm",
        "customer care",
        "customer",
        "support",
        "ticket",
    ),
    "analytics-reporting": (
        "analytics",
        "reporting",
        "business intelligence",
        "dashboard",
        "metric",
        "kpi",
    ),
    "operations-monitoring": (
        "operations",
        "monitoring",
        "health",
        "observability",
        "scheduler",
        "background job",
        "incident",
    ),
    "ai-software-factory": (
        "ai factory",
        "software factory",
        "executable sprint",
        "prompt",
        "context resolution",
        "seed",
        "governance",
        "sprint",
        "implementation",
    ),
}


INTEGRATION_PATTERNS: dict[str, tuple[str, ...]] = {
    "gigago": ("gigago",),
    "onepay": ("onepay",),
    "gpay": ("gpay",),
    "paypal": ("paypal",),
    "airwallex": ("airwallex",),
    "google-oauth": (
        "google oauth",
        "gmail",
        "google login",
    ),
    "smtp-email": (
        "smtp",
        "email",
    ),
    "sms-gateway": (
        "sms",
    ),
}


DOCUMENT_SET_LAYER: dict[str, str] = {
    "AFM": "factory",
    "YADF": "factory",
    "AAP": "factory",
    "BRD": "business",
    "ABP": "architecture",
    "SGP": "governance",
    "ESP": "engineering",
    "DIP": "implementation",
    "ESPK": "execution",
    "ROP": "operations",
    "ROOT": "navigation",
}
