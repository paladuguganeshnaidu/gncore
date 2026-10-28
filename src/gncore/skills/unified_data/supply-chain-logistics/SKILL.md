---
name: supply-chain-logistics
description: "Plan demand, sourcing, suppliers, inventory, warehouses, transport, resilience, and supply-chain performance."
license: MIT
---

# GNCore Supply Chain and Logistics

## Select the work from the user's intent

Establish SKU or shipment grain, planning horizon, demand variability, lead times, service targets, constraints, and cost basis. Trace dependencies across suppliers, inventory, warehouses, transport, and customers. Optimize the end-to-end outcome rather than one isolated metric.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Check units, calendars, stock balances, lead-time assumptions, service-cost tradeoffs, capacity, and disruption scenarios. Separate forecast demand from confirmed orders.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `supply-demand` | Build a demand view with documented inputs, scenarios, and error checks. |
| `supply-sourcing` | Compare sourcing options for cost, quality, lead time, resilience, and compliance. |
| `supply-supplier` | Review supplier performance with agreed measures and corrective actions. |
| `supply-inventory` | Identify inventory imbalances without hiding service risk. |
| `supply-warehouse` | Improve warehouse flow, safety, accuracy, and workload visibility. |
| `supply-transport` | Plan shipments with constraints, service, cost, and exception handling visible. |
| `supply-resilience` | Assess disruption exposure, early signals, and mitigation options. |
| `supply-control-tower` | Triage exceptions by impact, owner, and next update. |
| `supply-procurement` | Reconcile orders, receipts, invoices, and supplier records with traceable exceptions. |
| `supply-sustainability` | Review sustainability claims with boundaries, evidence, and data-quality limits. |

## Focused procedures

### Demand Planning (`supply-demand`)

Define item/location/time grain, reconcile history, flag promotions/stockouts, compare baselines, backtest horizons, show uncertainty and overrides.

### Sourcing Strategy (`supply-sourcing`)

Use comparable landed costs, verify evidence, map dependencies and concentration risk, document tradeoffs, route restricted decisions to legal/procurement.

### Supplier Performance Review (`supply-supplier`)

Define denominators, reconcile systems, honor exclusions, include supplier context, and track accountable owners/dates.

### Inventory Optimization (`supply-inventory`)

Use current lead times and demand distributions, distinguish stock types, model carrying/shortage costs, validate service assumptions.

### Warehouse Operations (`supply-warehouse`)

Map handoffs, protect worker safety/accessibility, measure baseline, test with operators, monitor quality and fatigue.

### Transportation Planning (`supply-transport`)

Validate dimensions, capacity, cutoffs, service and regulatory limits, compare total cost, and avoid invented carrier commitments.

### Supply Chain Risk Review (`supply-resilience`)

Map critical tiers and single points, date evidence, separate likelihood/impact, test scenarios, set triggers, disclose visibility limits.

### Supply Chain Exception Review (`supply-control-tower`)

Deduplicate alerts, validate identifiers/timestamps, prioritize by supplied rules, assign next action, escalate safety/compliance issues.

### Purchase Order Reconciliation (`supply-procurement`)

Match stable identifiers/tolerances, handle partial receipts and units, preserve originals, reconcile totals, route mismatches to approvers.

### Supply Chain Sustainability Review (`supply-sustainability`)

Define scope and functional unit, trace primary/estimated data, check allocation and double counting, disclose uncertainty, avoid unsupported claims.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [cbrock84/headcount / supply-chain-and-logistics](research/cbrock84-headcount-supply-chain-and-logistics/GUIDE.md): MIT.
- [travisjneuman/.claude / supply-chain-optimizer](research/travisjneuman-.claude-supply-chain-optimizer/GUIDE.md): MIT.
- [kishorkukreja/awesome-supply-chain / pharmacy-supply-chain](research/kishorkukreja-awesome-supply-chain-pharmacy-supply-chain/GUIDE.md): MIT.
- [kishorkukreja/awesome-supply-chain / food-beverage-supply-chain](research/kishorkukreja-awesome-supply-chain-food-beverage-supply-chain/GUIDE.md): MIT.
- [kishorkukreja/awesome-supply-chain / pharmaceutical-supply-chain](research/kishorkukreja-awesome-supply-chain-pharmaceutical-supply-chain/GUIDE.md): MIT.
- [kishorkukreja/awesome-supply-chain / hospital-logistics](research/kishorkukreja-awesome-supply-chain-hospital-logistics/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
