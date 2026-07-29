# ADR-R1-007 — Storefront Repository and API Boundary

## Status

PROPOSED

## Context

`ysim-storefront` is an existing Next.js repository with proven product presentation, checkout experience, GPay work and Gigago integration lessons.

Release 1 requires YSim Platform to own Order, Payment, Procurement, Fulfillment, eSIM Asset and Commission. WooCommerce remains a transitional content and SEO system.

## Decision

`ysim-storefront` remains a separate repository and acts as a channel client of YSim Platform APIs.

The Storefront must not be the canonical owner of commercial or fulfillment state.

## Storefront responsibilities

- Marketing pages.
- Product presentation.
- SEO.
- Destination browsing.
- Localized customer experience.
- Cart and checkout UI.
- Payment redirection UI.
- Customer navigation to Portal.
- Reference QR entry experience.

## Platform responsibilities

- Canonical Product Offer.
- Price Book and Pricing Quote.
- Agency Offer and Reference Artifact.
- Checkout Session.
- Sales Order.
- Payment.
- Procurement.
- Fulfillment.
- eSIM Asset.
- Delivery state.
- Commission.
- Operations and Audit.

## WooCommerce transition

WooCommerce may continue to own:

- Marketing content.
- SEO metadata.
- Images.
- Slugs.
- Editorial content.

WooCommerce must not be authoritative for:

- Order status.
- Payment status.
- Fulfillment status.
- Commission.
- eSIM Asset.

No bidirectional synchronization is allowed for those states.

## API rules

- Storefront receives price from a signed Pricing Quote.
- Storefront cannot submit trusted selling price or commission.
- Reference QR commercial fields are resolved server-side.
- Storefront uses public channel APIs and authenticated customer APIs.
- API contracts are explicitly versioned.
- Correlation ID is propagated.
- Customer-visible errors are localized.
- Secrets and provider credentials never reach the browser.

## Checkout integrity

At checkout confirmation, Platform validates:

- Product Offer.
- Market.
- Currency.
- Pricing Quote.
- Agency attribution.
- Payment-provider eligibility.
- Quote expiration.

Browser data is treated as untrusted.

## Deployment independence

Storefront and Platform may deploy independently when API compatibility is preserved.

A breaking API change requires:

- New contract version.
- Storefront migration.
- Compatibility period.
- Coordinated removal.

## Consequences

### Positive

- Preserves proven Storefront work.
- Allows channel independence.
- Keeps core commerce canonical in Platform.
- Supports future embedded and agency channels.

### Negative

- Requires API compatibility management.
- Local end-to-end development spans two repositories.
- Content and commercial data require clear references.

## Rejected alternatives

### Move Storefront into the platform monorepo immediately

Rejected for Release 1 because it adds migration work without improving the core business path.

### Continue creating canonical orders in WooCommerce

Rejected because YSim Platform must own commerce and distribution state from Release 1.
