# GNCore Skill Catalog and Usage Guide

GNCore 4.0.0 includes **403 skills** across **30 domain packs**. Each domain pack has ten workflows. This page is generated from the built-in catalog; rerun `python scripts/generate_skill_catalog.py` after catalog changes.

## How to use a skill

1. Search by task: `gncore search "clean data"` or `gncore search CEO strategy`.
2. Install the listed skill ID for your assistant and scope. Example: `gncore install company-ceo --apps vscode-codex --scope workspace`.
3. In an assistant that supports native skill invocation, start the request with its slash name, such as `/company-ceo`, then describe the outcome, context, constraints, and acceptance checks.
4. Review the assistant's changes and evidence. Skills guide the assistant; they do not execute independently or guarantee an outcome.

Use `gncore list apps` to check target keys and `gncore doctor` / `gncore validate --apps <key>` to inspect an installation. Replace `vscode-codex` with a key from `gncore list apps`; use `--scope user` for user-wide installation.

## Domain packs

### Company Leadership (`company-leadership`)

Executive and C-suite workflows for company direction, governance, and operating decisions.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `company-ceo` | `/company-ceo` | CEO Decision Brief | Prepare an evidence-led CEO brief for a company-level decision. | `gncore install company-ceo --apps vscode-codex --scope workspace` |
| `company-cfo` | `/company-cfo` | CFO Review | Review financial performance, liquidity, and capital choices for executive decisions. | `gncore install company-cfo --apps vscode-codex --scope workspace` |
| `company-coo` | `/company-coo` | COO Operating Review | Diagnose operational performance and turn bottlenecks into accountable actions. | `gncore install company-coo --apps vscode-codex --scope workspace` |
| `company-cto` | `/company-cto` | CTO Technology Review | Assess technology direction, engineering execution, and technical risk for leadership. | `gncore install company-cto --apps vscode-codex --scope workspace` |
| `company-cpo` | `/company-cpo` | Chief Product Officer Review | Align product portfolio decisions with customer evidence and company outcomes. | `gncore install company-cpo --apps vscode-codex --scope workspace` |
| `company-cmo` | `/company-cmo` | Chief Marketing Officer Review | Evaluate marketing strategy, brand health, and growth investment for executives. | `gncore install company-cmo --apps vscode-codex --scope workspace` |
| `company-chro` | `/company-chro` | Chief People Officer Review | Review workforce health, organization design, and talent risks with appropriate privacy. | `gncore install company-chro --apps vscode-codex --scope workspace` |
| `company-ciso` | `/company-ciso` | Chief Information Security Officer Review | Brief executives on cyber risk, exposure, and risk-reduction decisions. | `gncore install company-ciso --apps vscode-codex --scope workspace` |
| `company-board` | `/company-board` | Board Materials Review | Prepare or review board-level materials for clarity, governance, and decision quality. | `gncore install company-board --apps vscode-codex --scope workspace` |
| `company-executive-team` | `/company-executive-team` | Executive Team Alignment | Resolve cross-functional decisions into shared priorities, owners, and measurable commitments. | `gncore install company-executive-team --apps vscode-codex --scope workspace` |

### Business Strategy (`business-strategy`)

Company strategy, market positioning, portfolio choices, and strategic execution.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `strategy-market-entry` | `/strategy-market-entry` | Market Entry Strategy | Evaluate entry into a new market using evidence, economics, and staged commitments. | `gncore install strategy-market-entry --apps vscode-codex --scope workspace` |
| `strategy-portfolio` | `/strategy-portfolio` | Portfolio Prioritization | Rank business initiatives by strategic value, evidence, capacity, and opportunity cost. | `gncore install strategy-portfolio --apps vscode-codex --scope workspace` |
| `strategy-competitive` | `/strategy-competitive` | Competitive Analysis | Compare competitors using verifiable evidence and decision-relevant positioning. | `gncore install strategy-competitive --apps vscode-codex --scope workspace` |
| `strategy-business-model` | `/strategy-business-model` | Business Model Review | Map a business model and test whether its value creation and capture are sustainable. | `gncore install strategy-business-model --apps vscode-codex --scope workspace` |
| `strategy-scenario` | `/strategy-scenario` | Strategic Scenario Planning | Build plausible scenarios and decision triggers for uncertain business conditions. | `gncore install strategy-scenario --apps vscode-codex --scope workspace` |
| `strategy-okrs` | `/strategy-okrs` | Strategy to OKRs | Translate strategic intent into measurable outcomes and aligned quarterly objectives. | `gncore install strategy-okrs --apps vscode-codex --scope workspace` |
| `strategy-pricing` | `/strategy-pricing` | Pricing Strategy | Analyze pricing architecture, willingness-to-pay evidence, and margin consequences. | `gncore install strategy-pricing --apps vscode-codex --scope workspace` |
| `strategy-risk` | `/strategy-risk` | Enterprise Risk Assessment | Prioritize strategic risks by likelihood, impact, exposure, and mitigation evidence. | `gncore install strategy-risk --apps vscode-codex --scope workspace` |
| `strategy-ma` | `/strategy-ma` | M&A Opportunity Screen | Screen an acquisition or partnership opportunity against strategic and financial criteria. | `gncore install strategy-ma --apps vscode-codex --scope workspace` |
| `strategy-transformation` | `/strategy-transformation` | Business Transformation Plan | Design a staged transformation with outcomes, governance, adoption, and measurable benefits. | `gncore install strategy-transformation --apps vscode-codex --scope workspace` |

### Product Management (`product-management`)

Product discovery, roadmaps, requirements, launch readiness, and lifecycle decisions.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `product-opportunity` | `/product-opportunity` | Product Opportunity Brief | Turn customer and business evidence into a scoped product opportunity. | `gncore install product-opportunity --apps vscode-codex --scope workspace` |
| `product-requirements` | `/product-requirements` | Product Requirements | Write testable product requirements and acceptance criteria for a scoped feature. | `gncore install product-requirements --apps vscode-codex --scope workspace` |
| `product-roadmap` | `/product-roadmap` | Product Roadmap | Build an outcome-led roadmap that exposes dependencies, confidence, and trade-offs. | `gncore install product-roadmap --apps vscode-codex --scope workspace` |
| `product-discovery-sprint` | `/product-discovery-sprint` | Product Discovery Sprint | Plan a short discovery cycle that resolves the riskiest product assumptions. | `gncore install product-discovery-sprint --apps vscode-codex --scope workspace` |
| `product-prioritization` | `/product-prioritization` | Feature Prioritization | Prioritize feature requests using customer value, evidence, cost, and strategic fit. | `gncore install product-prioritization --apps vscode-codex --scope workspace` |
| `product-experiment` | `/product-experiment` | Product Experiment Design | Design product experiments with a clear hypothesis, metric, guardrails, and decision rule. | `gncore install product-experiment --apps vscode-codex --scope workspace` |
| `product-launch` | `/product-launch` | Product Launch Readiness | Coordinate launch readiness across product, engineering, support, sales, and communications. | `gncore install product-launch --apps vscode-codex --scope workspace` |
| `product-feedback` | `/product-feedback` | Customer Feedback Synthesis | Synthesize product feedback into traceable themes without overstating frequency. | `gncore install product-feedback --apps vscode-codex --scope workspace` |
| `product-lifecycle` | `/product-lifecycle` | Product Lifecycle Review | Assess adoption, retention, quality, and investment choices for an existing product. | `gncore install product-lifecycle --apps vscode-codex --scope workspace` |
| `product-metrics` | `/product-metrics` | Product Metrics Definition | Define a product metric with an unambiguous event, population, denominator, and owner. | `gncore install product-metrics --apps vscode-codex --scope workspace` |

### Project and Program Management (`project-program-management`)

Project planning, cross-team delivery, dependencies, status, and recovery.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `project-charter` | `/project-charter` | Project Charter | Create a concise project charter with outcome, scope, ownership, constraints, and decision gates. | `gncore install project-charter --apps vscode-codex --scope workspace` |
| `project-plan` | `/project-plan` | Delivery Plan | Build an executable delivery plan with milestones, dependencies, owners, and evidence. | `gncore install project-plan --apps vscode-codex --scope workspace` |
| `project-status` | `/project-status` | Project Status Brief | Produce a truthful project status update with progress, forecast, risks, and asks. | `gncore install project-status --apps vscode-codex --scope workspace` |
| `project-risk-log` | `/project-risk-log` | Project Risk Log | Create and maintain actionable project risks, issues, assumptions, and dependencies. | `gncore install project-risk-log --apps vscode-codex --scope workspace` |
| `project-recovery` | `/project-recovery` | Project Recovery Plan | Recover a troubled project by identifying root causes and rebaselining achievable outcomes. | `gncore install project-recovery --apps vscode-codex --scope workspace` |
| `project-meeting` | `/project-meeting` | Decision Meeting Preparation | Prepare a meeting agenda and decision record that uses participant time effectively. | `gncore install project-meeting --apps vscode-codex --scope workspace` |
| `project-dependency` | `/project-dependency` | Dependency Coordination | Map and resolve cross-team dependencies before they become delivery blockers. | `gncore install project-dependency --apps vscode-codex --scope workspace` |
| `project-capacity` | `/project-capacity` | Capacity and Resource Plan | Match project demand to available skills, capacity, and protected operational work. | `gncore install project-capacity --apps vscode-codex --scope workspace` |
| `project-retro` | `/project-retro` | Project Retrospective | Run a blameless retrospective that yields specific, owned process improvements. | `gncore install project-retro --apps vscode-codex --scope workspace` |
| `project-closure` | `/project-closure` | Project Closure and Handoff | Close a project with accepted deliverables, operational ownership, records, and lessons. | `gncore install project-closure --apps vscode-codex --scope workspace` |

### Business Operations (`business-operations`)

Repeatable company operations, service quality, process design, and operational control.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `operations-process-map` | `/operations-process-map` | Process Mapping | Map a business process from trigger to outcome and expose waste and control gaps. | `gncore install operations-process-map --apps vscode-codex --scope workspace` |
| `operations-sop` | `/operations-sop` | Standard Operating Procedure | Write an actionable SOP with prerequisites, steps, decision points, and recovery paths. | `gncore install operations-sop --apps vscode-codex --scope workspace` |
| `operations-kpi` | `/operations-kpi` | Operations KPI Review | Analyze operational KPIs against service outcomes, baselines, and capacity limits. | `gncore install operations-kpi --apps vscode-codex --scope workspace` |
| `operations-quality` | `/operations-quality` | Service Quality Improvement | Reduce recurring service defects through root-cause analysis and controlled countermeasures. | `gncore install operations-quality --apps vscode-codex --scope workspace` |
| `operations-capacity` | `/operations-capacity` | Capacity and Queue Planning | Forecast service capacity and queues with explicit demand, throughput, and uncertainty. | `gncore install operations-capacity --apps vscode-codex --scope workspace` |
| `operations-control` | `/operations-control` | Operational Control Design | Design practical controls that prevent or detect costly process failures. | `gncore install operations-control --apps vscode-codex --scope workspace` |
| `operations-incident` | `/operations-incident` | Business Operations Incident | Coordinate a non-technical operational incident and restore service with clear ownership. | `gncore install operations-incident --apps vscode-codex --scope workspace` |
| `operations-vendor` | `/operations-vendor` | Vendor Operations Review | Review vendor delivery against service commitments, risks, dependencies, and corrective actions. | `gncore install operations-vendor --apps vscode-codex --scope workspace` |
| `operations-continuity` | `/operations-continuity` | Business Continuity Plan | Prepare a business continuity response for essential processes and credible disruption scenarios. | `gncore install operations-continuity --apps vscode-codex --scope workspace` |
| `operations-automation` | `/operations-automation` | Operations Automation Case | Assess whether an operational task is ready for safe automation and quantify its value. | `gncore install operations-automation --apps vscode-codex --scope workspace` |

### Sales and Revenue (`sales-revenue`)

Pipeline management, account planning, proposals, forecasting, and revenue operations.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `sales-account-plan` | `/sales-account-plan` | Strategic Account Plan | Create an account plan based on customer outcomes, stakeholders, risks, and verified activity. | `gncore install sales-account-plan --apps vscode-codex --scope workspace` |
| `sales-discovery` | `/sales-discovery` | Sales Discovery | Prepare neutral discovery questions that uncover customer needs, impact, constraints, and decision process. | `gncore install sales-discovery --apps vscode-codex --scope workspace` |
| `sales-qualification` | `/sales-qualification` | Opportunity Qualification | Assess opportunity fit and deal risk using transparent qualification evidence. | `gncore install sales-qualification --apps vscode-codex --scope workspace` |
| `sales-pipeline` | `/sales-pipeline` | Pipeline Review | Inspect pipeline quality and next-step integrity to improve forecast and coaching. | `gncore install sales-pipeline --apps vscode-codex --scope workspace` |
| `sales-forecast` | `/sales-forecast` | Revenue Forecast | Build a revenue forecast with explicit assumptions, scenarios, and confidence. | `gncore install sales-forecast --apps vscode-codex --scope workspace` |
| `sales-proposal` | `/sales-proposal` | Customer Proposal | Draft a customer proposal tied to stated needs, outcomes, scope, assumptions, and evidence. | `gncore install sales-proposal --apps vscode-codex --scope workspace` |
| `sales-negotiation` | `/sales-negotiation` | Commercial Negotiation Preparation | Prepare negotiation options and concession boundaries grounded in approved commercial policy. | `gncore install sales-negotiation --apps vscode-codex --scope workspace` |
| `sales-objection` | `/sales-objection` | Customer Objection Response | Answer a sales objection with accurate evidence and a useful next question. | `gncore install sales-objection --apps vscode-codex --scope workspace` |
| `sales-territory` | `/sales-territory` | Territory and Coverage Plan | Balance account coverage and sales capacity across a territory using transparent criteria. | `gncore install sales-territory --apps vscode-codex --scope workspace` |
| `sales-renewal` | `/sales-renewal` | Renewal and Expansion Plan | Protect a renewal by connecting adoption, realized outcomes, risks, and agreed next value. | `gncore install sales-renewal --apps vscode-codex --scope workspace` |

### Marketing and Growth (`marketing-growth`)

Positioning, campaigns, content, lifecycle, demand generation, and marketing measurement.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `marketing-positioning` | `/marketing-positioning` | Positioning and Messaging | Develop evidence-based positioning for a defined audience and competitive context. | `gncore install marketing-positioning --apps vscode-codex --scope workspace` |
| `marketing-campaign` | `/marketing-campaign` | Campaign Plan | Plan a campaign with audience, offer, channels, budget, measurement, and approval gates. | `gncore install marketing-campaign --apps vscode-codex --scope workspace` |
| `marketing-content` | `/marketing-content` | Marketing Content Brief | Brief content creators with audience need, purpose, evidence, voice, format, and success criteria. | `gncore install marketing-content --apps vscode-codex --scope workspace` |
| `marketing-seo` | `/marketing-seo` | Search Content Audit | Audit search content for intent match, accuracy, technical discoverability, and useful next actions. | `gncore install marketing-seo --apps vscode-codex --scope workspace` |
| `marketing-lifecycle` | `/marketing-lifecycle` | Lifecycle Messaging | Design lifecycle messages that help users reach a meaningful product outcome. | `gncore install marketing-lifecycle --apps vscode-codex --scope workspace` |
| `marketing-attribution` | `/marketing-attribution` | Marketing Attribution Review | Interpret marketing contribution while exposing attribution model limitations and incrementality. | `gncore install marketing-attribution --apps vscode-codex --scope workspace` |
| `marketing-brand` | `/marketing-brand` | Brand Consistency Review | Review brand execution for message consistency, audience fit, accessibility, and evidence. | `gncore install marketing-brand --apps vscode-codex --scope workspace` |
| `marketing-social` | `/marketing-social` | Social Media Plan | Create a platform-aware social plan with useful content, response ownership, and risk controls. | `gncore install marketing-social --apps vscode-codex --scope workspace` |
| `marketing-budget` | `/marketing-budget` | Marketing Budget Allocation | Allocate marketing budget using marginal returns, uncertainty, and strategic coverage. | `gncore install marketing-budget --apps vscode-codex --scope workspace` |
| `marketing-launch` | `/marketing-launch` | Go-to-Market Launch | Coordinate market launch readiness across product, pricing, channels, enablement, and customer support. | `gncore install marketing-launch --apps vscode-codex --scope workspace` |

### Finance and Accounting (`finance-accounting`)

Budgeting, forecasting, reporting, bookkeeping controls, and financial analysis support.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `finance-budget` | `/finance-budget` | Budget Build | Build a traceable budget from operational drivers, assumptions, owners, and approved targets. | `gncore install finance-budget --apps vscode-codex --scope workspace` |
| `finance-forecast` | `/finance-forecast` | Rolling Forecast | Update a rolling forecast from actuals and current business drivers without hiding variance. | `gncore install finance-forecast --apps vscode-codex --scope workspace` |
| `finance-variance` | `/finance-variance` | Financial Variance Analysis | Explain financial variance by volume, price, mix, timing, and one-time effects. | `gncore install finance-variance --apps vscode-codex --scope workspace` |
| `finance-cashflow` | `/finance-cashflow` | Cash Flow and Runway | Model cash needs and runway using explicit receipts, obligations, and timing scenarios. | `gncore install finance-cashflow --apps vscode-codex --scope workspace` |
| `finance-unit-economics` | `/finance-unit-economics` | Unit Economics | Calculate unit economics with consistent cohort, cost allocation, and contribution assumptions. | `gncore install finance-unit-economics --apps vscode-codex --scope workspace` |
| `finance-month-close` | `/finance-month-close` | Month-End Close Checklist | Coordinate a complete month-end close with reconciliations, owners, evidence, and review. | `gncore install finance-month-close --apps vscode-codex --scope workspace` |
| `finance-controls` | `/finance-controls` | Financial Controls Review | Review financial process controls for authorization, reconciliation, evidence, and segregation. | `gncore install finance-controls --apps vscode-codex --scope workspace` |
| `finance-investment-case` | `/finance-investment-case` | Investment Business Case | Build a decision-ready capital request with costs, benefits, alternatives, and sensitivity. | `gncore install finance-investment-case --apps vscode-codex --scope workspace` |
| `finance-expense` | `/finance-expense` | Expense Policy Review | Assess expense submissions against supplied policy with consistent evidence and escalation. | `gncore install finance-expense --apps vscode-codex --scope workspace` |
| `finance-report` | `/finance-report` | Financial Report Review | Review a financial report for arithmetic, consistency, labels, source traceability, and decision clarity. | `gncore install finance-report --apps vscode-codex --scope workspace` |

### People and Human Resources (`people-human-resources`)

Hiring, onboarding, development, performance, workforce planning, and employee operations.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `people-role-design` | `/people-role-design` | Role Design | Define a role around outcomes, decision rights, essential skills, and fair selection criteria. | `gncore install people-role-design --apps vscode-codex --scope workspace` |
| `people-job-post` | `/people-job-post` | Job Description | Draft an inclusive, accurate job description from an approved role profile. | `gncore install people-job-post --apps vscode-codex --scope workspace` |
| `people-interview` | `/people-interview` | Structured Interview Plan | Create a structured interview plan with job-related questions and consistent evaluation anchors. | `gncore install people-interview --apps vscode-codex --scope workspace` |
| `people-onboarding` | `/people-onboarding` | Employee Onboarding Plan | Plan a role-specific onboarding path with access, learning, relationships, and early outcomes. | `gncore install people-onboarding --apps vscode-codex --scope workspace` |
| `people-development` | `/people-development` | Development Plan | Create a practical employee development plan linked to goals, strengths, and supported practice. | `gncore install people-development --apps vscode-codex --scope workspace` |
| `people-performance` | `/people-performance` | Performance Review Support | Organize performance evidence into a fair, specific, and balanced review draft. | `gncore install people-performance --apps vscode-codex --scope workspace` |
| `people-workforce-plan` | `/people-workforce-plan` | Workforce Plan | Forecast workforce capacity and skills against business demand and approved scenarios. | `gncore install people-workforce-plan --apps vscode-codex --scope workspace` |
| `people-engagement` | `/people-engagement` | Engagement Survey Analysis | Analyze employee feedback responsibly while protecting confidentiality and avoiding false precision. | `gncore install people-engagement --apps vscode-codex --scope workspace` |
| `people-policy` | `/people-policy` | HR Policy Draft Review | Review an HR policy draft for clarity, internal consistency, accessibility, and escalation needs. | `gncore install people-policy --apps vscode-codex --scope workspace` |
| `people-offboarding` | `/people-offboarding` | Employee Offboarding Checklist | Coordinate a respectful offboarding with access, knowledge transfer, property, records, and final responsibilities. | `gncore install people-offboarding --apps vscode-codex --scope workspace` |

### Customer Success and Support (`customer-success-support`)

Customer onboarding, support triage, service recovery, knowledge, and retention workflows.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `customer-onboarding` | `/customer-onboarding` | Customer Onboarding Plan | Guide a customer to a defined first outcome with owners, milestones, and adoption signals. | `gncore install customer-onboarding --apps vscode-codex --scope workspace` |
| `customer-support-triage` | `/customer-support-triage` | Support Case Triage | Classify a support issue by impact, urgency, reproducibility, and routing evidence. | `gncore install customer-support-triage --apps vscode-codex --scope workspace` |
| `customer-reply` | `/customer-reply` | Customer Support Reply | Draft a clear customer reply that addresses the issue, next action, and known limits. | `gncore install customer-reply --apps vscode-codex --scope workspace` |
| `customer-escalation` | `/customer-escalation` | Customer Escalation Brief | Prepare an escalation brief with impact, timeline, evidence, owner, and decision request. | `gncore install customer-escalation --apps vscode-codex --scope workspace` |
| `customer-health` | `/customer-health` | Customer Health Review | Assess customer health from transparent adoption, outcome, relationship, and support signals. | `gncore install customer-health --apps vscode-codex --scope workspace` |
| `customer-renewal` | `/customer-renewal` | Customer Renewal Risk | Build a renewal action plan grounded in value realization, stakeholder needs, and contract facts. | `gncore install customer-renewal --apps vscode-codex --scope workspace` |
| `customer-knowledge` | `/customer-knowledge` | Support Knowledge Article | Write a tested support article that resolves a common issue with clear prerequisites and recovery. | `gncore install customer-knowledge --apps vscode-codex --scope workspace` |
| `customer-voice` | `/customer-voice` | Voice of Customer Synthesis | Combine customer evidence into actionable themes with source coverage and counterexamples. | `gncore install customer-voice --apps vscode-codex --scope workspace` |
| `customer-service-recovery` | `/customer-service-recovery` | Service Recovery Plan | Restore trust after a service failure through verified facts, ownership, and follow-through. | `gncore install customer-service-recovery --apps vscode-codex --scope workspace` |
| `customer-success-qbr` | `/customer-success-qbr` | Customer Business Review | Prepare a customer review that connects usage, outcomes, open risks, and next-period goals. | `gncore install customer-success-qbr --apps vscode-codex --scope workspace` |

### Legal and Compliance Support (`legal-compliance`)

Organize legal and compliance work for review by authorized professionals; not a substitute for counsel.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `legal-contract-intake` | `/legal-contract-intake` | Contract Review Intake | Extract obligations, deadlines, and questions from a supplied contract for counsel review. | `gncore install legal-contract-intake --apps vscode-codex --scope workspace` |
| `legal-obligation-map` | `/legal-obligation-map` | Obligation Tracker | Turn contract or policy text into traceable obligations, owners, dates, and evidence. | `gncore install legal-obligation-map --apps vscode-codex --scope workspace` |
| `legal-policy-gap` | `/legal-policy-gap` | Compliance Gap Assessment | Compare supplied controls or evidence against a named policy or framework requirement. | `gncore install legal-policy-gap --apps vscode-codex --scope workspace` |
| `legal-privacy-intake` | `/legal-privacy-intake` | Privacy Review Intake | Structure a privacy review by mapping purpose, data, access, retention, and user impact. | `gncore install legal-privacy-intake --apps vscode-codex --scope workspace` |
| `legal-regulatory-watch` | `/legal-regulatory-watch` | Regulatory Change Brief | Summarize a supplied regulatory update and identify affected business processes for expert review. | `gncore install legal-regulatory-watch --apps vscode-codex --scope workspace` |
| `legal-incident-hold` | `/legal-incident-hold` | Legal Hold Coordination Checklist | Organize a preservation checklist from authorized instructions without altering source records. | `gncore install legal-incident-hold --apps vscode-codex --scope workspace` |
| `legal-marketing-claims` | `/legal-marketing-claims` | Marketing Claims Review | Trace public claims to substantiation and flag claims needing legal or regulatory review. | `gncore install legal-marketing-claims --apps vscode-codex --scope workspace` |
| `legal-entity-records` | `/legal-entity-records` | Corporate Records Checklist | Organize entity governance records and upcoming filing or approval actions from supplied records. | `gncore install legal-entity-records --apps vscode-codex --scope workspace` |
| `legal-dispute-chronology` | `/legal-dispute-chronology` | Dispute Chronology | Build a source-linked chronology from supplied dispute materials for counsel review. | `gncore install legal-dispute-chronology --apps vscode-codex --scope workspace` |
| `legal-review-memo` | `/legal-review-memo` | Legal Review Memo Support | Draft a neutral issue-and-evidence memo for a qualified lawyer to review. | `gncore install legal-review-memo --apps vscode-codex --scope workspace` |

### Procurement and Vendor Management (`procurement-vendor`)

Responsible sourcing, vendor selection, contract administration, and supplier performance.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `procurement-requirements` | `/procurement-requirements` | Procurement Requirements | Translate a business need into measurable, vendor-neutral procurement requirements. | `gncore install procurement-requirements --apps vscode-codex --scope workspace` |
| `procurement-rfp` | `/procurement-rfp` | RFP Package | Prepare a fair request for proposal with scope, scoring, schedule, and response instructions. | `gncore install procurement-rfp --apps vscode-codex --scope workspace` |
| `procurement-scorecard` | `/procurement-scorecard` | Vendor Scorecard | Score supplier proposals against published criteria with evidence and consistent normalization. | `gncore install procurement-scorecard --apps vscode-codex --scope workspace` |
| `procurement-total-cost` | `/procurement-total-cost` | Total Cost of Ownership | Compare vendor options across implementation, usage, support, renewal, exit, and risk costs. | `gncore install procurement-total-cost --apps vscode-codex --scope workspace` |
| `procurement-due-diligence` | `/procurement-due-diligence` | Supplier Due Diligence | Coordinate risk-based supplier due diligence across security, privacy, finance, and continuity. | `gncore install procurement-due-diligence --apps vscode-codex --scope workspace` |
| `procurement-negotiation` | `/procurement-negotiation` | Supplier Negotiation Plan | Prepare negotiation priorities and fallback options within approved procurement authority. | `gncore install procurement-negotiation --apps vscode-codex --scope workspace` |
| `procurement-onboarding` | `/procurement-onboarding` | Supplier Onboarding | Coordinate supplier onboarding with least-privilege access, ownership, and required control evidence. | `gncore install procurement-onboarding --apps vscode-codex --scope workspace` |
| `procurement-performance` | `/procurement-performance` | Supplier Performance Review | Review vendor service against contracted outcomes, service levels, and corrective actions. | `gncore install procurement-performance --apps vscode-codex --scope workspace` |
| `procurement-renewal` | `/procurement-renewal` | Vendor Renewal Review | Make a renewal decision using value, risk, alternatives, usage, and notice deadlines. | `gncore install procurement-renewal --apps vscode-codex --scope workspace` |
| `procurement-exit` | `/procurement-exit` | Supplier Exit Plan | Plan a controlled supplier transition that protects service, data, access, and records. | `gncore install procurement-exit --apps vscode-codex --scope workspace` |

### Entrepreneurship and New Ventures (`entrepreneurship`)

Validate new business ideas, launch plans, early economics, and founder decisions.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `venture-idea` | `/venture-idea` | Venture Idea Screen | Screen a venture idea by customer problem, alternatives, evidence, and founder constraints. | `gncore install venture-idea --apps vscode-codex --scope workspace` |
| `venture-customer-interview` | `/venture-customer-interview` | Customer Interview Guide | Prepare non-leading interviews that test customer behavior and unmet needs. | `gncore install venture-customer-interview --apps vscode-codex --scope workspace` |
| `venture-mvp` | `/venture-mvp` | Minimum Viable Product Scope | Choose the smallest product experiment that can test a critical venture assumption. | `gncore install venture-mvp --apps vscode-codex --scope workspace` |
| `venture-business-model` | `/venture-business-model` | Venture Business Model | Map the venture's customer, value, channel, cost, revenue, and operating assumptions. | `gncore install venture-business-model --apps vscode-codex --scope workspace` |
| `venture-business-plan` | `/venture-business-plan` | Business Plan Draft | Create a decision-focused business plan with evidence, assumptions, execution, and capital needs. | `gncore install venture-business-plan --apps vscode-codex --scope workspace` |
| `venture-fundraise` | `/venture-fundraise` | Fundraising Preparation | Organize fundraising narrative, evidence, materials, and diligence readiness. | `gncore install venture-fundraise --apps vscode-codex --scope workspace` |
| `venture-runway` | `/venture-runway` | Founder Runway Scenarios | Model startup runway and options under base, downside, and financing scenarios. | `gncore install venture-runway --apps vscode-codex --scope workspace` |
| `venture-go-to-market` | `/venture-go-to-market` | Early Go-to-Market Test | Design a low-cost channel test for an early product with a measurable learning objective. | `gncore install venture-go-to-market --apps vscode-codex --scope workspace` |
| `venture-founder-agreement` | `/venture-founder-agreement` | Founder Alignment Checklist | Surface founder-role, decision, equity, vesting, and conflict questions for professional review. | `gncore install venture-founder-agreement --apps vscode-codex --scope workspace` |
| `venture-pivot-review` | `/venture-pivot-review` | Pivot or Persevere Review | Decide whether to continue, adjust, or stop a venture hypothesis from observed evidence. | `gncore install venture-pivot-review --apps vscode-codex --scope workspace` |

### Software Engineering (`software-engineering`)

Software architecture, implementation, code review, maintenance, and release quality.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `software-feature` | `/software-feature` | Software Feature Delivery | Deliver a scoped software feature using local conventions and verifiable acceptance criteria. | `gncore install software-feature --apps vscode-codex --scope workspace` |
| `software-architecture` | `/software-architecture` | Software Architecture Decision | Compare architecture options against constraints, operations, reversibility, and lifecycle cost. | `gncore install software-architecture --apps vscode-codex --scope workspace` |
| `software-code-review` | `/software-code-review` | Software Code Review | Review a code change for correctness, security, maintainability, and missing regression coverage. | `gncore install software-code-review --apps vscode-codex --scope workspace` |
| `software-debugging` | `/software-debugging` | Software Debugging | Diagnose a software failure from reproducible evidence and verify the smallest safe fix. | `gncore install software-debugging --apps vscode-codex --scope workspace` |
| `software-refactor` | `/software-refactor` | Safe Refactoring | Refactor a bounded code area while preserving its documented behavior and public contracts. | `gncore install software-refactor --apps vscode-codex --scope workspace` |
| `software-api-contract` | `/software-api-contract` | Software API Contract | Define and verify an API contract across request, response, errors, versioning, and consumers. | `gncore install software-api-contract --apps vscode-codex --scope workspace` |
| `software-dependency` | `/software-dependency` | Dependency Change Review | Assess and implement a dependency change with compatibility, security, and rollback evidence. | `gncore install software-dependency --apps vscode-codex --scope workspace` |
| `software-performance` | `/software-performance` | Software Performance Optimization | Find a measured software bottleneck and optimize it without regressing correctness. | `gncore install software-performance --apps vscode-codex --scope workspace` |
| `software-migration` | `/software-migration` | Software Migration Plan | Plan a staged migration with compatibility gates, data safety, and rollback criteria. | `gncore install software-migration --apps vscode-codex --scope workspace` |
| `software-release` | `/software-release` | Software Release Candidate | Prepare a software release with reproducible artifacts, verified changes, and rollback readiness. | `gncore install software-release --apps vscode-codex --scope workspace` |

### Data Analytics and Intelligence (`data-analytics`)

Business intelligence, data quality, metrics, dashboards, and decision analysis.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `analytics-question` | `/analytics-question` | Analytics Question Plan | Translate a business question into a measurable analysis plan and data requirements. | `gncore install analytics-question --apps vscode-codex --scope workspace` |
| `analytics-data-audit` | `/analytics-data-audit` | Data Quality Audit | Audit analytical data for missingness, duplication, validity, freshness, and grain. | `gncore install analytics-data-audit --apps vscode-codex --scope workspace` |
| `analytics-sql` | `/analytics-sql` | Business SQL Analysis | Write a traceable SQL analysis with correct grain, joins, time handling, and reconciliation. | `gncore install analytics-sql --apps vscode-codex --scope workspace` |
| `analytics-dashboard` | `/analytics-dashboard` | Decision Dashboard | Design a dashboard around a recurring decision with clear metrics, filters, and data freshness. | `gncore install analytics-dashboard --apps vscode-codex --scope workspace` |
| `analytics-metric-tree` | `/analytics-metric-tree` | Metric Tree | Decompose a business outcome into leading drivers and measurable operational inputs. | `gncore install analytics-metric-tree --apps vscode-codex --scope workspace` |
| `analytics-cohort` | `/analytics-cohort` | Cohort Analysis | Compare cohort behavior with consistent definitions, exposure windows, and censoring treatment. | `gncore install analytics-cohort --apps vscode-codex --scope workspace` |
| `analytics-experiment` | `/analytics-experiment` | Business Experiment Analysis | Analyze an experiment with assignment, exposure, predeclared outcomes, and uncertainty checks. | `gncore install analytics-experiment --apps vscode-codex --scope workspace` |
| `analytics-forecast` | `/analytics-forecast` | Business Forecast Analysis | Build a business forecast from history, drivers, scenarios, and out-of-sample checks. | `gncore install analytics-forecast --apps vscode-codex --scope workspace` |
| `analytics-insight-brief` | `/analytics-insight-brief` | Executive Analytics Brief | Turn analysis into a concise decision brief with traceable evidence and caveats. | `gncore install analytics-insight-brief --apps vscode-codex --scope workspace` |
| `analytics-data-contract` | `/analytics-data-contract` | Analytics Data Contract | Specify ownership, schema, quality, freshness, and change handling for an analytics dataset. | `gncore install analytics-data-contract --apps vscode-codex --scope workspace` |

### AI and Machine Learning (`ai-machine-learning`)

Machine learning, model training, evaluation, LLM, retrieval, and responsible release workflows.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `ml-problem-framing` | `/ml-problem-framing` | ML Problem Framing | Decide whether a machine learning approach fits the task, data, constraints, and failure costs. | `gncore install ml-problem-framing --apps vscode-codex --scope workspace` |
| `ml-dataset-audit` | `/ml-dataset-audit` | ML Dataset Audit | Audit dataset provenance, schema, representativeness, label quality, leakage, and split strategy. | `gncore install ml-dataset-audit --apps vscode-codex --scope workspace` |
| `ml-preprocessing-pipeline` | `/ml-preprocessing-pipeline` | ML Preprocessing Pipeline | Build deterministic preprocessing that prevents leakage and preserves training-to-serving parity. | `gncore install ml-preprocessing-pipeline --apps vscode-codex --scope workspace` |
| `ml-model-train` | `/ml-model-train` | ML Model Training Run | Implement a reproducible model training run with configuration, baseline, checkpoints, and evaluation. | `gncore install ml-model-train --apps vscode-codex --scope workspace` |
| `ml-model-evaluation` | `/ml-model-evaluation` | ML Model Evaluation | Evaluate model quality, uncertainty, subgroup behavior, and representative errors against a baseline. | `gncore install ml-model-evaluation --apps vscode-codex --scope workspace` |
| `ml-model-improvement` | `/ml-model-improvement` | ML Improvement Loop | Improve a model through controlled experiments with a fixed evaluation protocol and root-cause analysis. | `gncore install ml-model-improvement --apps vscode-codex --scope workspace` |
| `ml-llm-evaluation` | `/ml-llm-evaluation` | LLM Evaluation Suite | Evaluate an LLM feature with representative tasks, rubrics, adversarial cases, latency, and cost. | `gncore install ml-llm-evaluation --apps vscode-codex --scope workspace` |
| `ml-rag` | `/ml-rag` | RAG Grounding Workflow | Build and evaluate retrieval-augmented answers with source access controls and abstention. | `gncore install ml-rag --apps vscode-codex --scope workspace` |
| `ml-finetuning` | `/ml-finetuning` | Model Fine-Tuning Plan | Assess fine-tuning suitability and prepare a controlled, leakage-safe fine-tuning workflow. | `gncore install ml-finetuning --apps vscode-codex --scope workspace` |
| `ml-release-monitor` | `/ml-release-monitor` | Model Release and Monitoring | Prepare a model release with provenance, compatibility, rollback, and drift monitoring gates. | `gncore install ml-release-monitor --apps vscode-codex --scope workspace` |

### Cybersecurity (`cybersecurity`)

Defensive security engineering, threat analysis, incident response, and security assurance.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `cyber-threat-model` | `/cyber-threat-model` | Threat Model | Map assets, trust boundaries, threats, controls, and residual risk for a bounded system. | `gncore install cyber-threat-model --apps vscode-codex --scope workspace` |
| `cyber-secure-code` | `/cyber-secure-code` | Secure Code Review | Review a code change for exploitable input, identity, authorization, secret, and data-flow flaws. | `gncore install cyber-secure-code --apps vscode-codex --scope workspace` |
| `cyber-vulnerability-triage` | `/cyber-vulnerability-triage` | Vulnerability Triage | Prioritize a reported vulnerability using affected assets, exploitability, exposure, and impact evidence. | `gncore install cyber-vulnerability-triage --apps vscode-codex --scope workspace` |
| `cyber-incident-response` | `/cyber-incident-response` | Cyber Incident Response | Coordinate defensive incident response with containment, evidence preservation, and recovery gates. | `gncore install cyber-incident-response --apps vscode-codex --scope workspace` |
| `cyber-identity-access` | `/cyber-identity-access` | Identity and Access Review | Review identities and permissions for least privilege, lifecycle, ownership, and audit evidence. | `gncore install cyber-identity-access --apps vscode-codex --scope workspace` |
| `cyber-cloud-review` | `/cyber-cloud-review` | Cloud Security Review | Assess cloud configuration against an explicit threat model and approved security baseline. | `gncore install cyber-cloud-review --apps vscode-codex --scope workspace` |
| `cyber-security-controls` | `/cyber-security-controls` | Security Control Evidence | Map supplied evidence to security control requirements with traceable, bounded conclusions. | `gncore install cyber-security-controls --apps vscode-codex --scope workspace` |
| `cyber-phishing` | `/cyber-phishing` | Phishing Response Triage | Triage a suspected phishing report and provide safe containment and user guidance. | `gncore install cyber-phishing --apps vscode-codex --scope workspace` |
| `cyber-secret-response` | `/cyber-secret-response` | Exposed Secret Response | Respond to a potentially exposed credential without echoing or spreading the secret. | `gncore install cyber-secret-response --apps vscode-codex --scope workspace` |
| `cyber-security-test-plan` | `/cyber-security-test-plan` | Authorized Security Test Plan | Define a bounded security test plan with written authorization, targets, limits, and stop conditions. | `gncore install cyber-security-test-plan --apps vscode-codex --scope workspace` |

### Cloud, DevOps, and SRE (`cloud-devops-sre`)

Infrastructure, delivery automation, service reliability, cost, and production operations.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `cloud-architecture-review` | `/cloud-architecture-review` | Cloud Architecture Review | Compare cloud designs against workload, reliability, security, cost, and operational constraints. | `gncore install cloud-architecture-review --apps vscode-codex --scope workspace` |
| `cloud-infrastructure-code` | `/cloud-infrastructure-code` | Infrastructure as Code | Author or review infrastructure changes with plan inspection, least privilege, and rollback. | `gncore install cloud-infrastructure-code --apps vscode-codex --scope workspace` |
| `cloud-ci-cd` | `/cloud-ci-cd` | CI/CD Pipeline | Improve a delivery pipeline with reproducibility, least privilege, useful gates, and rollback. | `gncore install cloud-ci-cd --apps vscode-codex --scope workspace` |
| `cloud-container` | `/cloud-container` | Container Build and Hardening | Build a reproducible container with a minimal attack surface and reliable runtime behavior. | `gncore install cloud-container --apps vscode-codex --scope workspace` |
| `cloud-kubernetes` | `/cloud-kubernetes` | Kubernetes Workload Review | Review Kubernetes workloads for availability, resource bounds, identity, health, and rollout safety. | `gncore install cloud-kubernetes --apps vscode-codex --scope workspace` |
| `cloud-slo` | `/cloud-slo` | SLO and Error Budget | Define service-level indicators and objectives that reflect user-visible reliability. | `gncore install cloud-slo --apps vscode-codex --scope workspace` |
| `cloud-observability` | `/cloud-observability` | Service Observability | Instrument service behavior with actionable metrics, structured logs, and traces. | `gncore install cloud-observability --apps vscode-codex --scope workspace` |
| `cloud-incident` | `/cloud-incident` | SRE Incident Management | Manage a reliability incident through impact assessment, safe mitigation, verification, and learning. | `gncore install cloud-incident --apps vscode-codex --scope workspace` |
| `cloud-capacity` | `/cloud-capacity` | Capacity and Load Plan | Plan service capacity using measured demand, bottleneck data, growth uncertainty, and failure headroom. | `gncore install cloud-capacity --apps vscode-codex --scope workspace` |
| `cloud-cost` | `/cloud-cost` | Cloud Cost Optimization | Reduce measurable infrastructure spend while protecting service objectives and recovery options. | `gncore install cloud-cost --apps vscode-codex --scope workspace` |

### Quality Engineering and Testing (`quality-engineering`)

Test design, automation, release assurance, defect analysis, and quality improvement.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `qa-test-strategy` | `/qa-test-strategy` | Test Strategy | Choose a risk-based test mix that verifies behavior at the lowest effective level. | `gncore install qa-test-strategy --apps vscode-codex --scope workspace` |
| `qa-test-design` | `/qa-test-design` | Test Case Design | Turn a behavior contract into clear positive, negative, boundary, and state-transition tests. | `gncore install qa-test-design --apps vscode-codex --scope workspace` |
| `qa-automation` | `/qa-automation` | Test Automation | Build maintainable test automation with stable setup, deterministic data, and actionable failures. | `gncore install qa-automation --apps vscode-codex --scope workspace` |
| `qa-e2e` | `/qa-e2e` | End-to-End User Journey Test | Verify a critical user journey across the application with realistic but isolated data. | `gncore install qa-e2e --apps vscode-codex --scope workspace` |
| `qa-api-contract` | `/qa-api-contract` | API Contract Testing | Check API compatibility, validation, authorization, and error contracts between services. | `gncore install qa-api-contract --apps vscode-codex --scope workspace` |
| `qa-performance` | `/qa-performance` | Performance Test Plan | Measure a service against representative load, latency, throughput, and resource objectives. | `gncore install qa-performance --apps vscode-codex --scope workspace` |
| `qa-accessibility` | `/qa-accessibility` | Accessibility Test Pass | Test a flow for keyboard operation, semantics, focus, labels, zoom, and assistive technology support. | `gncore install qa-accessibility --apps vscode-codex --scope workspace` |
| `qa-defect-triage` | `/qa-defect-triage` | Defect Triage | Classify and prioritize a defect using reproducibility, user impact, scope, and workaround evidence. | `gncore install qa-defect-triage --apps vscode-codex --scope workspace` |
| `qa-release-gate` | `/qa-release-gate` | Release Quality Gate | Evaluate release evidence against agreed quality gates and make residual risk visible. | `gncore install qa-release-gate --apps vscode-codex --scope workspace` |
| `qa-flaky-test` | `/qa-flaky-test` | Flaky Test Investigation | Find the cause of an intermittent test failure and confirm a stable correction. | `gncore install qa-flaky-test --apps vscode-codex --scope workspace` |

### Design, UX, and Accessibility (`design-ux`)

User research, interface design, content hierarchy, design systems, and usability validation.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `design-ux-audit` | `/design-ux-audit` | UX Usability Audit | Audit a user flow for task clarity, feedback, recovery, cognitive load, and accessibility. | `gncore install design-ux-audit --apps vscode-codex --scope workspace` |
| `design-user-flow` | `/design-user-flow` | User Flow Design | Map a user journey with entry points, decisions, states, errors, and successful completion. | `gncore install design-user-flow --apps vscode-codex --scope workspace` |
| `design-wireframe` | `/design-wireframe` | Wireframe Specification | Specify a wireframe around user priorities, information hierarchy, and responsive states. | `gncore install design-wireframe --apps vscode-codex --scope workspace` |
| `design-minimal` | `/design-minimal` | Minimalist UI Direction | Create a restrained interface with clear hierarchy, intentional whitespace, and accessible controls. | `gncore install design-minimal --apps vscode-codex --scope workspace` |
| `design-expressive` | `/design-expressive` | Expressive UI Direction | Create a distinctive, layered interface without sacrificing navigation, readability, or accessibility. | `gncore install design-expressive --apps vscode-codex --scope workspace` |
| `design-system-component` | `/design-system-component` | Design System Component | Specify a reusable design-system component with API, states, semantics, and adoption guidance. | `gncore install design-system-component --apps vscode-codex --scope workspace` |
| `design-content` | `/design-content` | UX Content Design | Write interface text that helps users understand choices, status, errors, and recovery. | `gncore install design-content --apps vscode-codex --scope workspace` |
| `design-prototype` | `/design-prototype` | Prototype Test Plan | Create a prototype test plan that resolves a specific interaction or comprehension question. | `gncore install design-prototype --apps vscode-codex --scope workspace` |
| `design-accessibility` | `/design-accessibility` | Accessible Interaction Design | Design keyboard, screen-reader, motion, contrast, and touch behavior into an interaction. | `gncore install design-accessibility --apps vscode-codex --scope workspace` |
| `design-handoff` | `/design-handoff` | Design to Engineering Handoff | Prepare a design handoff with behavior, states, assets, responsive rules, and unresolved questions. | `gncore install design-handoff --apps vscode-codex --scope workspace` |

### Microsoft Word and DOCX Documents (`word-documents`)

Create, revise, format, redline, and verify Word documents and DOCX deliverables.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `word-draft` | `/word-draft` | Draft a Word Document | Create a structured Word document from a brief, source material, and intended audience. | `gncore install word-draft --apps vscode-codex --scope workspace` |
| `word-edit` | `/word-edit` | Edit and Restructure DOCX | Edit an existing Word document for clarity and structure while preserving required content. | `gncore install word-edit --apps vscode-codex --scope workspace` |
| `word-format` | `/word-format` | Word Formatting Repair | Repair Word styles, spacing, headers, pagination, tables, and section layout. | `gncore install word-format --apps vscode-codex --scope workspace` |
| `word-redline` | `/word-redline` | Word Tracked Changes Review | Prepare or review DOCX edits with traceable changes and comments for human approval. | `gncore install word-redline --apps vscode-codex --scope workspace` |
| `word-accessibility` | `/word-accessibility` | Accessible Word Document | Improve DOCX structure and accessibility for navigation, screen readers, and document reuse. | `gncore install word-accessibility --apps vscode-codex --scope workspace` |
| `word-template` | `/word-template` | Word Template Design | Create a reusable Word template with stable styles, fields, sections, and usage rules. | `gncore install word-template --apps vscode-codex --scope workspace` |
| `word-report` | `/word-report` | Word Report Production | Produce a sourced report in Word with executive summary, evidence, findings, and appendices. | `gncore install word-report --apps vscode-codex --scope workspace` |
| `word-merge` | `/word-merge` | Word Document Merge | Combine supplied DOCX materials into one coherent document without losing provenance or structure. | `gncore install word-merge --apps vscode-codex --scope workspace` |
| `word-forms` | `/word-forms` | Word Form Design | Design a fillable Word form with clear labels, logical completion order, and safe review. | `gncore install word-forms --apps vscode-codex --scope workspace` |
| `word-review` | `/word-review` | Word Final Proof and QA | Proofread a final DOCX for content consistency, references, fields, and page-level layout. | `gncore install word-review --apps vscode-codex --scope workspace` |

### PDF Documents (`pdf-documents`)

Extract, create, combine, review, secure, and validate PDF files.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `pdf-extract` | `/pdf-extract` | PDF Text and Table Extraction | Extract text or tables from a supplied PDF while preserving page references and uncertainty. | `gncore install pdf-extract --apps vscode-codex --scope workspace` |
| `pdf-create` | `/pdf-create` | Create a PDF Deliverable | Create a clean PDF from approved source content and verify its page layout and metadata. | `gncore install pdf-create --apps vscode-codex --scope workspace` |
| `pdf-accessibility` | `/pdf-accessibility` | Accessible PDF Review | Review or improve PDF tags, reading order, headings, links, tables, and alternative text. | `gncore install pdf-accessibility --apps vscode-codex --scope workspace` |
| `pdf-merge` | `/pdf-merge` | Merge PDFs | Combine approved PDFs in a defined order while preserving page integrity and source provenance. | `gncore install pdf-merge --apps vscode-codex --scope workspace` |
| `pdf-split` | `/pdf-split` | Split PDF by Page or Section | Split a PDF into named outputs using explicit page ranges or verified section boundaries. | `gncore install pdf-split --apps vscode-codex --scope workspace` |
| `pdf-form` | `/pdf-form` | PDF Form Workflow | Inspect or create a fillable PDF form with labeled fields and reliable save behavior. | `gncore install pdf-form --apps vscode-codex --scope workspace` |
| `pdf-ocr` | `/pdf-ocr` | Scanned PDF OCR | Make a scanned PDF searchable with OCR and verify text against original page images. | `gncore install pdf-ocr --apps vscode-codex --scope workspace` |
| `pdf-redaction` | `/pdf-redaction` | PDF Redaction Review | Apply and verify permanent redaction to specifically authorized PDF content. | `gncore install pdf-redaction --apps vscode-codex --scope workspace` |
| `pdf-review` | `/pdf-review` | PDF Content and Layout Review | Review PDF content, links, references, page numbering, and rendered layout before delivery. | `gncore install pdf-review --apps vscode-codex --scope workspace` |
| `pdf-signature` | `/pdf-signature` | PDF Signature Workflow Support | Prepare a PDF for an authorized signature workflow and verify fields and final artifact integrity. | `gncore install pdf-signature --apps vscode-codex --scope workspace` |

### Presentations and PowerPoint (`presentations-powerpoint`)

Plan, create, edit, and inspect persuasive, accessible presentation decks and PPTX files.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `ppt-storyline` | `/ppt-storyline` | Presentation Storyline | Turn an audience, decision, and evidence set into a coherent presentation narrative. | `gncore install ppt-storyline --apps vscode-codex --scope workspace` |
| `ppt-create` | `/ppt-create` | Create a PowerPoint Deck | Create a presentation deck from a brief and source material with a clear storyline and consistent design. | `gncore install ppt-create --apps vscode-codex --scope workspace` |
| `ppt-executive` | `/ppt-executive` | Executive Presentation | Prepare an executive deck that leads with decisions, implications, risks, and evidence. | `gncore install ppt-executive --apps vscode-codex --scope workspace` |
| `ppt-data-story` | `/ppt-data-story` | Data Story Presentation | Explain data in slides with faithful charts, denominators, uncertainty, and a decision-relevant takeaway. | `gncore install ppt-data-story --apps vscode-codex --scope workspace` |
| `ppt-visual-design` | `/ppt-visual-design` | Presentation Visual Design | Improve slide hierarchy, typography, color, alignment, and visual consistency without weakening content. | `gncore install ppt-visual-design --apps vscode-codex --scope workspace` |
| `ppt-edit` | `/ppt-edit` | Edit an Existing PPTX | Revise an existing deck while preserving intended content, theme, and editable structure. | `gncore install ppt-edit --apps vscode-codex --scope workspace` |
| `ppt-speaker-notes` | `/ppt-speaker-notes` | Speaker Notes and Talk Track | Write speaker notes that support a timed presentation without duplicating slide text. | `gncore install ppt-speaker-notes --apps vscode-codex --scope workspace` |
| `ppt-accessibility` | `/ppt-accessibility` | Accessible Presentation | Review a presentation for reading order, contrast, meaningful text, captions, and accessible charts. | `gncore install ppt-accessibility --apps vscode-codex --scope workspace` |
| `ppt-template` | `/ppt-template` | PowerPoint Template Design | Create a reusable PowerPoint template with reliable masters, layouts, typography, and color tokens. | `gncore install ppt-template --apps vscode-codex --scope workspace` |
| `ppt-deck-qa` | `/ppt-deck-qa` | PowerPoint Deck QA | Run a final slide-by-slide quality pass on a saved presentation and its exported PDF. | `gncore install ppt-deck-qa --apps vscode-codex --scope workspace` |

### Spreadsheets and Excel (`spreadsheets`)

Create, analyze, validate, and present spreadsheet workbooks with reliable formulas and data controls.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `sheet-model` | `/sheet-model` | Spreadsheet Model Design | Structure a spreadsheet model with clear inputs, calculations, outputs, and traceable assumptions. | `gncore install sheet-model --apps vscode-codex --scope workspace` |
| `sheet-formula-audit` | `/sheet-formula-audit` | Spreadsheet Formula Audit | Audit workbook formulas for broken references, inconsistencies, hard-codes, and calculation errors. | `gncore install sheet-formula-audit --apps vscode-codex --scope workspace` |
| `sheet-clean` | `/sheet-clean` | Spreadsheet Data Cleaning | Clean tabular spreadsheet data with explicit rules and before/after reconciliation. | `gncore install sheet-clean --apps vscode-codex --scope workspace` |
| `sheet-analysis` | `/sheet-analysis` | Spreadsheet Data Analysis | Answer an analytical question from workbook data with transparent formulas and checks. | `gncore install sheet-analysis --apps vscode-codex --scope workspace` |
| `sheet-dashboard` | `/sheet-dashboard` | Spreadsheet Dashboard | Build a decision-focused spreadsheet dashboard with stable formulas, labels, filters, and accessible visuals. | `gncore install sheet-dashboard --apps vscode-codex --scope workspace` |
| `sheet-pivot` | `/sheet-pivot` | Pivot Table Analysis | Create or review pivot analyses with verified source range, grouping, aggregation, and filter behavior. | `gncore install sheet-pivot --apps vscode-codex --scope workspace` |
| `sheet-forecast` | `/sheet-forecast` | Spreadsheet Forecast Model | Build or audit a forecast workbook with driver-based assumptions, scenarios, and error checks. | `gncore install sheet-forecast --apps vscode-codex --scope workspace` |
| `sheet-reconcile` | `/sheet-reconcile` | Spreadsheet Reconciliation | Reconcile two data sources with stable keys, exception categories, and totals control. | `gncore install sheet-reconcile --apps vscode-codex --scope workspace` |
| `sheet-automation` | `/sheet-automation` | Spreadsheet Automation | Automate repetitive workbook transformations with idempotent runs and safe output handling. | `gncore install sheet-automation --apps vscode-codex --scope workspace` |
| `sheet-presentation` | `/sheet-presentation` | Spreadsheet Presentation Cleanup | Prepare a workbook for review or print with consistent formats, frozen headers, page setup, and clear labels. | `gncore install sheet-presentation --apps vscode-codex --scope workspace` |

### Research and Market Intelligence (`research-market-intelligence`)

Source-led research, literature review, market sizing, synthesis, and evidence management.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `research-question` | `/research-question` | Research Question Design | Frame a researchable question with scope, definitions, evidence criteria, and a useful decision. | `gncore install research-question --apps vscode-codex --scope workspace` |
| `research-source-audit` | `/research-source-audit` | Source Quality Audit | Evaluate sources for authority, method, date, provenance, conflicts, and fitness for a claim. | `gncore install research-source-audit --apps vscode-codex --scope workspace` |
| `research-literature-review` | `/research-literature-review` | Literature Review | Synthesize a literature set with methods, findings, disagreement, and evidence gaps visible. | `gncore install research-literature-review --apps vscode-codex --scope workspace` |
| `research-market-size` | `/research-market-size` | Market Sizing | Estimate a market using transparent bottom-up or top-down assumptions and sensitivity ranges. | `gncore install research-market-size --apps vscode-codex --scope workspace` |
| `research-customer` | `/research-customer` | Customer and Market Research | Combine customer evidence and market signals into actionable, bounded insights. | `gncore install research-customer --apps vscode-codex --scope workspace` |
| `research-competitor` | `/research-competitor` | Competitive Research Brief | Prepare a dated competitor brief from verifiable product, pricing, and positioning evidence. | `gncore install research-competitor --apps vscode-codex --scope workspace` |
| `research-evidence-map` | `/research-evidence-map` | Evidence Map | Organize claims, sources, strength, disagreement, and missing evidence for a decision area. | `gncore install research-evidence-map --apps vscode-codex --scope workspace` |
| `research-survey` | `/research-survey` | Survey Design and Review | Design a survey with neutral wording, clear constructs, representative sampling, and privacy safeguards. | `gncore install research-survey --apps vscode-codex --scope workspace` |
| `research-brief` | `/research-brief` | Research Brief | Turn research into a concise, sourced brief with answer, confidence, implications, and open questions. | `gncore install research-brief --apps vscode-codex --scope workspace` |
| `research-monitor` | `/research-monitor` | Research Update Monitor | Track a defined topic for material source changes without overwhelming users with routine noise. | `gncore install research-monitor --apps vscode-codex --scope workspace` |

### Education and Learning (`education-learning`)

Curriculum, teaching materials, assessment, tutoring, accessibility, and learner feedback.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `education-learning-objectives` | `/education-learning-objectives` | Learning Objectives | Write measurable learning objectives aligned with learner needs, prerequisites, practice, and assessment. | `gncore install education-learning-objectives --apps vscode-codex --scope workspace` |
| `education-lesson` | `/education-lesson` | Lesson Plan | Plan a lesson with sequenced explanation, active practice, feedback, and accessible timing. | `gncore install education-lesson --apps vscode-codex --scope workspace` |
| `education-curriculum` | `/education-curriculum` | Curriculum Map | Organize a curriculum into coherent progression, prerequisite links, practice, and assessment. | `gncore install education-curriculum --apps vscode-codex --scope workspace` |
| `education-assessment` | `/education-assessment` | Assessment Design | Create an assessment aligned to learning outcomes with clear instructions and fair scoring. | `gncore install education-assessment --apps vscode-codex --scope workspace` |
| `education-rubric` | `/education-rubric` | Scoring Rubric | Develop a behavior-anchored rubric that supports consistent feedback and grading. | `gncore install education-rubric --apps vscode-codex --scope workspace` |
| `education-study-guide` | `/education-study-guide` | Study Guide | Create a focused study guide with key concepts, retrieval practice, examples, and self-check answers. | `gncore install education-study-guide --apps vscode-codex --scope workspace` |
| `education-tutor` | `/education-tutor` | Tutoring Session | Tutor a learner by diagnosing understanding, guiding practice, and adapting explanations. | `gncore install education-tutor --apps vscode-codex --scope workspace` |
| `education-content-accessibility` | `/education-content-accessibility` | Accessible Learning Material | Adapt learning content for accessible navigation, language, formats, and participation. | `gncore install education-content-accessibility --apps vscode-codex --scope workspace` |
| `education-feedback` | `/education-feedback` | Learner Feedback Synthesis | Synthesize learner feedback into evidence-based course improvements while protecting privacy. | `gncore install education-feedback --apps vscode-codex --scope workspace` |
| `education-course-review` | `/education-course-review` | Course Quality Review | Review a course for alignment among objectives, instruction, practice, assessment, workload, and accessibility. | `gncore install education-course-review --apps vscode-codex --scope workspace` |

### Healthcare Operations (`healthcare-operations`)

Administrative workflows for access, quality, privacy, and operational coordination; no clinical diagnosis or treatment.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `healthcare-intake` | `/healthcare-intake` | Healthcare Intake | Improve administrative intake completeness, routing, accessibility, and privacy. | `gncore install healthcare-intake --apps vscode-codex --scope workspace` |
| `healthcare-scheduling` | `/healthcare-scheduling` | Healthcare Scheduling | Coordinate appointments using supplied policies and patient preferences. | `gncore install healthcare-scheduling --apps vscode-codex --scope workspace` |
| `healthcare-operations-map` | `/healthcare-operations-map` | Healthcare Operations Map | Map administrative handoffs, delays, duplication, and ownership gaps. | `gncore install healthcare-operations-map --apps vscode-codex --scope workspace` |
| `healthcare-quality` | `/healthcare-quality` | Healthcare Quality Operations | Organize quality improvement with defined measures, owners, and review cycles. | `gncore install healthcare-quality --apps vscode-codex --scope workspace` |
| `healthcare-privacy` | `/healthcare-privacy` | Healthcare Privacy Review | Review artifacts for privacy exposure and minimum-necessary handling. | `gncore install healthcare-privacy --apps vscode-codex --scope workspace` |
| `healthcare-policy` | `/healthcare-policy` | Healthcare Policy Operations | Maintain operational policies with ownership, evidence, and review dates. | `gncore install healthcare-policy --apps vscode-codex --scope workspace` |
| `healthcare-patient-comms` | `/healthcare-patient-comms` | Patient Administrative Communications | Write clear non-clinical communications about administrative next steps. | `gncore install healthcare-patient-comms --apps vscode-codex --scope workspace` |
| `healthcare-audit` | `/healthcare-audit` | Healthcare Operations Audit | Review administrative controls and remediation with an evidence trail. | `gncore install healthcare-audit --apps vscode-codex --scope workspace` |
| `healthcare-capacity` | `/healthcare-capacity` | Healthcare Capacity Planning | Model service capacity using operational data and explicit assumptions. | `gncore install healthcare-capacity --apps vscode-codex --scope workspace` |
| `healthcare-improvement` | `/healthcare-improvement` | Healthcare Improvement Cycle | Plan and assess a bounded operational improvement with safeguards. | `gncore install healthcare-improvement --apps vscode-codex --scope workspace` |

### E-commerce and Retail (`ecommerce-retail`)

Catalog, merchandising, conversion, inventory, customer support, and retail operations.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `retail-catalog` | `/retail-catalog` | Product Catalog Quality | Improve product data completeness, consistency, and variant accuracy. | `gncore install retail-catalog --apps vscode-codex --scope workspace` |
| `retail-merchandising` | `/retail-merchandising` | Retail Merchandising | Align merchandising with customer intent, stock, margin, and brand. | `gncore install retail-merchandising --apps vscode-codex --scope workspace` |
| `retail-conversion` | `/retail-conversion` | Conversion Review | Diagnose page and checkout friction with evidence and prioritized experiments. | `gncore install retail-conversion --apps vscode-codex --scope workspace` |
| `retail-pricing` | `/retail-pricing` | Retail Pricing Analysis | Analyze prices, discounts, and margin with traceable sources. | `gncore install retail-pricing --apps vscode-codex --scope workspace` |
| `retail-inventory` | `/retail-inventory` | Retail Inventory Operations | Review inventory signals and replenishment exceptions. | `gncore install retail-inventory --apps vscode-codex --scope workspace` |
| `retail-campaign` | `/retail-campaign` | Retail Campaign Planning | Plan campaigns with stock, audience, creative, and measurement aligned. | `gncore install retail-campaign --apps vscode-codex --scope workspace` |
| `retail-reviews` | `/retail-reviews` | Customer Review Synthesis | Summarize reviews without fabricating or overstating customer evidence. | `gncore install retail-reviews --apps vscode-codex --scope workspace` |
| `retail-returns` | `/retail-returns` | Returns and Refund Analysis | Find return patterns while preserving policy and customer fairness. | `gncore install retail-returns --apps vscode-codex --scope workspace` |
| `retail-store-ops` | `/retail-store-ops` | Store Operations Playbook | Create store procedures with role ownership, safety checks, and escalation. | `gncore install retail-store-ops --apps vscode-codex --scope workspace` |
| `retail-qa` | `/retail-qa` | Commerce Experience QA | Test product, cart, checkout, device, and accessibility journeys. | `gncore install retail-qa --apps vscode-codex --scope workspace` |

### Business Communications (`business-communications`)

Executive writing, email, reports, policies, stakeholder updates, and crisis communications.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `comms-executive-brief` | `/comms-executive-brief` | Executive Brief | Create a concise decision brief with evidence, options, owner, and timing. | `gncore install comms-executive-brief --apps vscode-codex --scope workspace` |
| `comms-email` | `/comms-email` | Business Email | Draft audience-appropriate business email with a clear next action. | `gncore install comms-email --apps vscode-codex --scope workspace` |
| `comms-stakeholder-update` | `/comms-stakeholder-update` | Stakeholder Update | Report status, changes, blockers, decisions, and next steps. | `gncore install comms-stakeholder-update --apps vscode-codex --scope workspace` |
| `comms-policy` | `/comms-policy` | Internal Policy Draft | Draft policy with scope, rules, owner, exceptions, and review cadence. | `gncore install comms-policy --apps vscode-codex --scope workspace` |
| `comms-report` | `/comms-report` | Business Report | Connect evidence to conclusions and actions in a structured report. | `gncore install comms-report --apps vscode-codex --scope workspace` |
| `comms-crisis` | `/comms-crisis` | Crisis Communications | Prepare a factual holding statement and update plan for an incident. | `gncore install comms-crisis --apps vscode-codex --scope workspace` |
| `comms-edit` | `/comms-edit` | Clarity and Tone Edit | Edit writing for clarity, audience fit, accuracy, and consistent tone. | `gncore install comms-edit --apps vscode-codex --scope workspace` |
| `comms-meeting` | `/comms-meeting` | Meeting Brief and Minutes | Prepare agendas and decision-focused minutes with owners and follow-ups. | `gncore install comms-meeting --apps vscode-codex --scope workspace` |
| `comms-localization` | `/comms-localization` | Business Content Localization | Adapt content to a locale while preserving meaning, policy, and usability. | `gncore install comms-localization --apps vscode-codex --scope workspace` |
| `comms-quality` | `/comms-quality` | Communications Quality Check | Quality-check business communications before distribution. | `gncore install comms-quality --apps vscode-codex --scope workspace` |

### Supply Chain and Logistics (`supply-chain-logistics`)

Demand, sourcing, inventory, fulfillment, transport, resilience, and supplier performance.

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `supply-demand` | `/supply-demand` | Demand Planning | Build a demand view with documented inputs, scenarios, and error checks. | `gncore install supply-demand --apps vscode-codex --scope workspace` |
| `supply-sourcing` | `/supply-sourcing` | Sourcing Strategy | Compare sourcing options for cost, quality, lead time, resilience, and compliance. | `gncore install supply-sourcing --apps vscode-codex --scope workspace` |
| `supply-supplier` | `/supply-supplier` | Supplier Performance Review | Review supplier performance with agreed measures and corrective actions. | `gncore install supply-supplier --apps vscode-codex --scope workspace` |
| `supply-inventory` | `/supply-inventory` | Inventory Optimization | Identify inventory imbalances without hiding service risk. | `gncore install supply-inventory --apps vscode-codex --scope workspace` |
| `supply-warehouse` | `/supply-warehouse` | Warehouse Operations | Improve warehouse flow, safety, accuracy, and workload visibility. | `gncore install supply-warehouse --apps vscode-codex --scope workspace` |
| `supply-transport` | `/supply-transport` | Transportation Planning | Plan shipments with constraints, service, cost, and exception handling visible. | `gncore install supply-transport --apps vscode-codex --scope workspace` |
| `supply-resilience` | `/supply-resilience` | Supply Chain Risk Review | Assess disruption exposure, early signals, and mitigation options. | `gncore install supply-resilience --apps vscode-codex --scope workspace` |
| `supply-control-tower` | `/supply-control-tower` | Supply Chain Exception Review | Triage exceptions by impact, owner, and next update. | `gncore install supply-control-tower --apps vscode-codex --scope workspace` |
| `supply-procurement` | `/supply-procurement` | Purchase Order Reconciliation | Reconcile orders, receipts, invoices, and supplier records with traceable exceptions. | `gncore install supply-procurement --apps vscode-codex --scope workspace` |
| `supply-sustainability` | `/supply-sustainability` | Supply Chain Sustainability Review | Review sustainability claims with boundaries, evidence, and data-quality limits. | `gncore install supply-sustainability --apps vscode-codex --scope workspace` |

## Additional specialist skills

These skills complement the 30 domain packs and are grouped by their catalog category.

### ai-engineering

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `llm-app` | `/llm-app` | LLM Application Engineering | Implement reliable LLM features with structured outputs, bounded tools, privacy, and graceful failure handling. | `gncore install llm-app --apps vscode-codex --scope workspace` |
| `llm-evaluation` | `/llm-evaluation` | Evaluate an LLM Workflow | Measure an LLM feature with representative cases, explicit rubrics, failure analysis, and repeatable comparisons. | `gncore install llm-evaluation --apps vscode-codex --scope workspace` |
| `prompt-engineering` | `/prompt-engineering` | Prompt Engineering | Improve prompts against explicit tasks and evaluations while preserving tool and safety boundaries. | `gncore install prompt-engineering --apps vscode-codex --scope workspace` |
| `rag` | `/rag` | Retrieval-Augmented Generation | Build a grounded retrieval workflow with traceable sources, chunking tests, and abstention on missing evidence. | `gncore install rag --apps vscode-codex --scope workspace` |

### analytics

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `product-analytics` | `/product-analytics` | Product Analytics | Define product metrics and event instrumentation that answer a decision without collecting unnecessary data. | `gncore install product-analytics --apps vscode-codex --scope workspace` |

### automation

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `workflow-automation` | `/workflow-automation` | Workflow Automation | Automate a repetitive workflow with bounded inputs, safe retries, idempotency, and clear human checkpoints. | `gncore install workflow-automation --apps vscode-codex --scope workspace` |

### cloud

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `cloud-architecture` | `/cloud-architecture` | Cloud Architecture | Design a cloud deployment around explicit reliability, security, operations, and cost constraints. | `gncore install cloud-architecture --apps vscode-codex --scope workspace` |
| `cost-optimization` | `/cost-optimization` | Cloud Cost Optimization | Find measurable cloud cost reductions while protecting reliability and workload correctness. | `gncore install cost-optimization --apps vscode-codex --scope workspace` |

### content

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `content-strategy` | `/content-strategy` | Content Strategy | Plan clear, consistent content around a specific audience, task, evidence, and publishing goal. | `gncore install content-strategy --apps vscode-codex --scope workspace` |
| `documentation-translation` | `/documentation-translation` | Technical Localization | Adapt technical content across languages while preserving product meaning, UI limits, and verified terminology. | `gncore install documentation-translation --apps vscode-codex --scope workspace` |

### data

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `data-analysis` | `/data-analysis` | Data Analysis | Answer data questions with reproducible calculations, clear definitions, and honest uncertainty. | `gncore install data-analysis --apps vscode-codex --scope workspace` |
| `data-pipelines` | `/data-pipelines` | Data Pipeline Engineering | Build reliable, observable data pipelines with explicit schemas, retries, and idempotency. | `gncore install data-pipelines --apps vscode-codex --scope workspace` |

### data-engineering

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `data-governance` | `/data-governance` | Data Governance | Define practical ownership, quality, access, lineage, and retention controls for a data asset. | `gncore install data-governance --apps vscode-codex --scope workspace` |
| `data-pipeline` | `/data-pipeline` | Data Pipeline Engineering | Build observable, restartable pipelines with explicit schemas, idempotency, and data-quality checks. | `gncore install data-pipeline --apps vscode-codex --scope workspace` |
| `database-design` | `/database-design` | Database Design | Design safe relational data models, queries, and migrations that preserve integrity and performance. | `gncore install database-design --apps vscode-codex --scope workspace` |

### data-science

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `ab-testing` | `/ab-testing` | A/B Test Analysis | Analyze controlled experiments with valid assignment checks, predeclared metrics, and practical uncertainty. | `gncore install ab-testing --apps vscode-codex --scope workspace` |
| `analyze` | `/analyze` | Analyze Data | Answer a data question with reproducible analysis, explicit assumptions, and evidence tied to the provided data. | `gncore install analyze --apps vscode-codex --scope workspace` |
| `clean-data` | `/clean-data` | Clean a Dataset | Audit and clean a dataset with explicit, reversible rules for missing values, duplicates, types, and outliers. | `gncore install clean-data --apps vscode-codex --scope workspace` |
| `data-visualization` | `/data-visualization` | Data Visualization | Create clear charts that faithfully represent the underlying data and its uncertainty. | `gncore install data-visualization --apps vscode-codex --scope workspace` |
| `geospatial-analysis` | `/geospatial-analysis` | Geospatial Analysis | Analyze spatial data with explicit coordinate systems, units, geometry validity, and privacy controls. | `gncore install geospatial-analysis --apps vscode-codex --scope workspace` |
| `sql-analysis` | `/sql-analysis` | SQL Analysis | Write correct, reviewable SQL for analytics while guarding against join fanout and misleading aggregates. | `gncore install sql-analysis --apps vscode-codex --scope workspace` |
| `statistics` | `/statistics` | Statistical Analysis | Choose and interpret statistical methods with assumptions, uncertainty, and practical effects stated clearly. | `gncore install statistics --apps vscode-codex --scope workspace` |

### design

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `design-system` | `/design-system` | Design System Engineering | Extend a design system with accessible tokens and reusable components that fit existing conventions. | `gncore install design-system --apps vscode-codex --scope workspace` |
| `ux-research` | `/ux-research` | UX Research | Plan and synthesize ethical user research that ties observations to product decisions. | `gncore install ux-research --apps vscode-codex --scope workspace` |

### developer-tools

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `cli-design` | `/cli-design` | CLI Engineering | Design command-line tools with predictable arguments, clear errors, safe defaults, and scriptable output. | `gncore install cli-design --apps vscode-codex --scope workspace` |
| `git-workflow` | `/git-workflow` | Git Workflow Support | Prepare safe, reviewable Git changes with clear scope, tests, and commit history. | `gncore install git-workflow --apps vscode-codex --scope workspace` |

### devops

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `devops` | `/devops` | DevOps Engineering | Improve build and delivery workflows with reproducible steps, safe rollout, and actionable failure signals. | `gncore install devops --apps vscode-codex --scope workspace` |
| `docker` | `/docker` | Container Engineering | Build small, secure, reproducible containers with explicit runtime and health behavior. | `gncore install docker --apps vscode-codex --scope workspace` |
| `kubernetes` | `/kubernetes` | Kubernetes Engineering | Author Kubernetes resources with least privilege, clear health behavior, and safe rollout settings. | `gncore install kubernetes --apps vscode-codex --scope workspace` |
| `observability` | `/observability` | Observability Engineering | Instrument services with useful metrics, logs, and traces while controlling noise and sensitive data. | `gncore install observability --apps vscode-codex --scope workspace` |

### documentation

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `documentation-api` | `/documentation-api` | API Documentation | Document API behavior from the implementation and contract, with examples users can reproduce. | `gncore install documentation-api --apps vscode-codex --scope workspace` |
| `technical-writing` | `/technical-writing` | Technical Writing | Write accurate, task-oriented technical documentation with runnable examples and clear prerequisites. | `gncore install technical-writing --apps vscode-codex --scope workspace` |

### education

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `education-content` | `/education-content` | Learning Content Design | Create learning materials with measurable outcomes, sequenced practice, accessible examples, and answer checks. | `gncore install education-content --apps vscode-codex --scope workspace` |

### game-development

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `game-development` | `/game-development` | Game Development | Implement game features with deterministic state transitions, responsive input, and measurable performance. | `gncore install game-development --apps vscode-codex --scope workspace` |

### general

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `architecture` | `/architecture` | Architecture Designer | Defines system boundaries, interfaces, and implementation constraints. | `gncore install architecture --apps vscode-codex --scope workspace` |
| `documentation` | `/documentation` | Documentation Writer | Produces concise user and developer documentation that matches the implementation. | `gncore install documentation --apps vscode-codex --scope workspace` |
| `implementation` | `/implementation` | Implementation Builder | Writes production-grade code with minimal duplication and explicit types. | `gncore install implementation --apps vscode-codex --scope workspace` |
| `release` | `/release` | Release Manager | Coordinates versioning, packaging, and verification for shipping. | `gncore install release --apps vscode-codex --scope workspace` |
| `requirements` | `/requirements` | Requirements Clarifier | Collects scope, constraints, acceptance criteria, and open questions before implementation starts. | `gncore install requirements --apps vscode-codex --scope workspace` |
| `review` | `/review` | Code Reviewer | Finds defects, regressions, and missing coverage before release. | `gncore install review --apps vscode-codex --scope workspace` |
| `security` | `/security` | Security Reviewer | Assesses secrets handling, unsafe file access, and privilege boundaries. | `gncore install security --apps vscode-codex --scope workspace` |
| `testing` | `/testing` | Testing Specialist | Designs and validates tests for the changed slice. | `gncore install testing --apps vscode-codex --scope workspace` |

### machine-learning

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `computer-vision` | `/computer-vision` | Computer Vision | Build vision workflows with robust image handling, leakage-safe splits, and task-appropriate evaluation. | `gncore install computer-vision --apps vscode-codex --scope workspace` |
| `data-preparation` | `/data-preparation` | ML Data Preparation | Prepare reproducible model datasets while preventing leakage and preserving provenance. | `gncore install data-preparation --apps vscode-codex --scope workspace` |
| `deep-learning` | `/deep-learning` | Deep Learning Engineering | Develop deep learning code with explicit tensor shapes, stable optimization, and reproducible evaluation. | `gncore install deep-learning --apps vscode-codex --scope workspace` |
| `evaluate` | `/evaluate` | Evaluate a Model | Evaluate model quality with leakage-safe splits, task-appropriate metrics, baselines, and error analysis. | `gncore install evaluate --apps vscode-codex --scope workspace` |
| `experiment-tracking` | `/experiment-tracking` | Reproducible ML Experiments | Make model experiments traceable across code, data, configuration, environment, and artifacts. | `gncore install experiment-tracking --apps vscode-codex --scope workspace` |
| `feature-engineering` | `/feature-engineering` | Feature Engineering | Build features that are valid at prediction time and reproducible across training and inference. | `gncore install feature-engineering --apps vscode-codex --scope workspace` |
| `feature-engineering-practice` | `/feature-engineering-practice` | Feature Engineering Practice | Create leakage-safe, interpretable features that match the model's serving-time information. | `gncore install feature-engineering-practice --apps vscode-codex --scope workspace` |
| `fine-tuning` | `/fine-tuning` | Model Fine-Tuning | Plan or implement a parameter-efficient or full fine-tuning workflow with controlled data and cost. | `gncore install fine-tuning --apps vscode-codex --scope workspace` |
| `hardware-ml` | `/hardware-ml` | Edge and Hardware-Constrained ML | Adapt inference to constrained hardware using measured latency, memory, and accuracy tradeoffs. | `gncore install hardware-ml --apps vscode-codex --scope workspace` |
| `improve` | `/improve` | Improve a Machine Learning Model | Find evidence-based model improvements through error analysis and controlled experiments against a fixed baseline. | `gncore install improve --apps vscode-codex --scope workspace` |
| `machine-learning` | `/machine-learning` | Machine Learning Workflow | Develop a scoped machine learning feature, from data inspection and baseline selection through evaluation. | `gncore install machine-learning --apps vscode-codex --scope workspace` |
| `ml-experiment-tracking` | `/ml-experiment-tracking` | Machine Learning Experiment Tracking | Make model experiments comparable with consistent splits, metrics, configuration, and artifact provenance. | `gncore install ml-experiment-tracking --apps vscode-codex --scope workspace` |
| `mlops` | `/mlops` | MLOps and Model Release | Package, register, and monitor models with reproducible artifacts and explicit release gates. | `gncore install mlops --apps vscode-codex --scope workspace` |
| `model-card` | `/model-card` | Model Documentation | Document a model's intended use, data provenance, evaluation, limitations, and deployment assumptions. | `gncore install model-card --apps vscode-codex --scope workspace` |
| `model-evaluation` | `/model-evaluation` | Model Evaluation | Evaluate model quality with valid splits, suitable metrics, uncertainty, and error analysis. | `gncore install model-evaluation --apps vscode-codex --scope workspace` |
| `model-serving` | `/model-serving` | Model Serving and Inference APIs | Package model inference behind a reliable API with validation, resource limits, and observable behavior. | `gncore install model-serving --apps vscode-codex --scope workspace` |
| `model-training` | `/model-training` | Model Training | Set up or improve a reproducible model training run with clear configuration, checkpoints, and evaluation. | `gncore install model-training --apps vscode-codex --scope workspace` |
| `nlp` | `/nlp` | Natural Language Processing | Build NLP pipelines that respect language, label quality, privacy, and task-specific evaluation. | `gncore install nlp --apps vscode-codex --scope workspace` |
| `preprocess` | `/preprocess` | Preprocess Machine Learning Data | Design a repeatable preprocessing pipeline that preserves schema, prevents leakage, and records transformations. | `gncore install preprocess --apps vscode-codex --scope workspace` |
| `pytorch-training` | `/pytorch-training` | PyTorch Training | Implement PyTorch training loops with correct device, optimizer, checkpoint, and evaluation handling. | `gncore install pytorch-training --apps vscode-codex --scope workspace` |
| `tensorflow-training` | `/tensorflow-training` | TensorFlow and Keras Training | Build TensorFlow/Keras training workflows with explicit data, callbacks, and evaluation behavior. | `gncore install tensorflow-training --apps vscode-codex --scope workspace` |
| `time-series` | `/time-series` | Time-Series Modeling | Analyze and forecast time-indexed data with temporal splits, leakage controls, and useful uncertainty. | `gncore install time-series --apps vscode-codex --scope workspace` |
| `train` | `/train` | Train a Machine Learning Model | Build and run a reproducible model training workflow with a baseline, tracked configuration, and held-out evaluation. | `gncore install train --apps vscode-codex --scope workspace` |

### mobile-development

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `mobile-app` | `/mobile-app` | Mobile App Engineering | Implement mobile features with reliable navigation, offline behavior, accessibility, and platform conventions. | `gncore install mobile-app --apps vscode-codex --scope workspace` |

### operations

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `incident-response` | `/incident-response` | Incident Response | Triage incidents from evidence, reduce impact safely, and preserve a clear timeline and follow-up. | `gncore install incident-response --apps vscode-codex --scope workspace` |

### product

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `product-discovery` | `/product-discovery` | Product Discovery | Turn a product idea into a testable problem statement, user evidence plan, and scoped first release. | `gncore install product-discovery --apps vscode-codex --scope workspace` |

### professional-services

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `finance-analysis` | `/finance-analysis` | Financial Analysis Support | Structure financial calculations and scenarios with transparent inputs, formulas, and sensitivity ranges. | `gncore install finance-analysis --apps vscode-codex --scope workspace` |
| `legal-document-review` | `/legal-document-review` | Legal Document Review Support | Summarize a legal document's structure and flag questions for qualified counsel without giving definitive legal advice. | `gncore install legal-document-review --apps vscode-codex --scope workspace` |

### python

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `python-debugging` | `/python-debugging` | Python Debugging | Find the root cause of Python failures using reproducible evidence and the narrowest fix. | `gncore install python-debugging --apps vscode-codex --scope workspace` |
| `python-library` | `/python-library` | Python Library Engineering | Design maintainable Python packages with stable APIs, typing, packaging, and clear examples. | `gncore install python-library --apps vscode-codex --scope workspace` |
| `python-migration` | `/python-migration` | Python Upgrade and Migration | Migrate Python code or dependencies in a controlled way with compatibility evidence and a rollback path. | `gncore install python-migration --apps vscode-codex --scope workspace` |
| `python-packaging` | `/python-packaging` | Python Packaging | Package a Python library with clear APIs, reproducible builds, supported versions, and clean installation behavior. | `gncore install python-packaging --apps vscode-codex --scope workspace` |
| `python-performance` | `/python-performance` | Python Performance | Profile Python hotspots and improve measured runtime or memory without changing semantics. | `gncore install python-performance --apps vscode-codex --scope workspace` |

### quality-assurance

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `accessibility-audit` | `/accessibility-audit` | Accessibility Audit | Inspect a user flow for keyboard, screen reader, visual, and cognitive accessibility barriers. | `gncore install accessibility-audit --apps vscode-codex --scope workspace` |
| `e2e-testing` | `/e2e-testing` | End-to-End Testing | Create stable end-to-end coverage for critical user journeys with reliable setup and useful diagnostics. | `gncore install e2e-testing --apps vscode-codex --scope workspace` |
| `performance-audit` | `/performance-audit` | Performance Audit | Find and verify the largest performance bottlenecks before changing code or infrastructure. | `gncore install performance-audit --apps vscode-codex --scope workspace` |
| `requirements-to-tests` | `/requirements-to-tests` | Requirements to Acceptance Tests | Turn requirements into observable acceptance cases that cover success, failure, boundaries, and permissions. | `gncore install requirements-to-tests --apps vscode-codex --scope workspace` |
| `test-strategy` | `/test-strategy` | Test Strategy | Choose a balanced test plan that catches important failures at the lowest practical level. | `gncore install test-strategy --apps vscode-codex --scope workspace` |

### release-engineering

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `release-readiness` | `/release-readiness` | Release Readiness Review | Check a release candidate against explicit acceptance, compatibility, security, rollback, and communication gates. | `gncore install release-readiness --apps vscode-codex --scope workspace` |

### research

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `research-synthesis` | `/research-synthesis` | Research Synthesis | Synthesize supplied or sourced evidence with provenance, disagreement, and uncertainty kept visible. | `gncore install research-synthesis --apps vscode-codex --scope workspace` |

### security

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `privacy-review` | `/privacy-review` | Privacy Review | Reduce privacy risk by tracing personal data, purpose, access, retention, and user control. | `gncore install privacy-review --apps vscode-codex --scope workspace` |
| `security-review` | `/security-review` | Security Review | Review a scoped change for exploitable weaknesses and give prioritized, verifiable fixes. | `gncore install security-review --apps vscode-codex --scope workspace` |
| `web-application-security` | `/web-application-security` | Web Application Security | Review web changes for concrete access-control, injection, session, and data-exposure risks. | `gncore install web-application-security --apps vscode-codex --scope workspace` |
| `web-security` | `/web-security` | Web Security Engineering | Review web features for input, session, authorization, and output-handling vulnerabilities. | `gncore install web-security --apps vscode-codex --scope workspace` |

### testing

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `end-to-end-testing` | `/end-to-end-testing` | End-to-End Testing | Validate critical user journeys across the running application with stable, accessible assertions. | `gncore install end-to-end-testing --apps vscode-codex --scope workspace` |
| `integration-testing` | `/integration-testing` | Integration Testing | Verify interactions between real components while isolating external services and state. | `gncore install integration-testing --apps vscode-codex --scope workspace` |
| `performance-testing` | `/performance-testing` | Performance and Load Testing | Design controlled load tests that measure latency, throughput, and saturation safely. | `gncore install performance-testing --apps vscode-codex --scope workspace` |
| `test-automation` | `/test-automation` | Test Automation Engineering | Create maintainable CI test workflows with clear triggers, artifacts, and failure signals. | `gncore install test-automation --apps vscode-codex --scope workspace` |
| `unit-testing` | `/unit-testing` | Unit Testing | Write fast, deterministic unit tests around public behavior and edge cases. | `gncore install unit-testing --apps vscode-codex --scope workspace` |
| `web-testing` | `/web-testing` | Web Application Testing | Select and implement browser-level tests for important user journeys and regressions. | `gncore install web-testing --apps vscode-codex --scope workspace` |

### web-design

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `ui-maximalism` | `/ui-maximalism` | Maximalist Interface Design | Create expressive, layered interfaces while preserving hierarchy, readability, and usable controls. | `gncore install ui-maximalism --apps vscode-codex --scope workspace` |
| `ui-minimalism` | `/ui-minimalism` | Minimalist Interface Design | Create restrained interfaces with clear hierarchy, generous space, and only essential controls. | `gncore install ui-minimalism --apps vscode-codex --scope workspace` |

### web-development

| Skill ID | Slash name | Skill | Use it for | Install example |
| --- | --- | --- | --- | --- |
| `api-design` | `/api-design` | API Design | Design stable APIs with clear contracts, validation, compatibility, and error semantics. | `gncore install api-design --apps vscode-codex --scope workspace` |
| `backend-api` | `/backend-api` | Backend API Engineering | Design and implement reliable backend endpoints, validation, and service boundaries. | `gncore install backend-api --apps vscode-codex --scope workspace` |
| `django-engineering` | `/django-engineering` | Django Engineering | Implement Django features with correct ORM, migrations, permissions, and request handling. | `gncore install django-engineering --apps vscode-codex --scope workspace` |
| `fastapi-engineering` | `/fastapi-engineering` | FastAPI Engineering | Build typed FastAPI endpoints with explicit validation, dependency boundaries, and OpenAPI behavior. | `gncore install fastapi-engineering --apps vscode-codex --scope workspace` |
| `frontend-engineering` | `/frontend-engineering` | Frontend Engineering | Implement focused frontend features with strong state, component, and browser behavior. | `gncore install frontend-engineering --apps vscode-codex --scope workspace` |
| `responsive-accessibility` | `/responsive-accessibility` | Responsive and Accessible Web UI | Build responsive interfaces that work with keyboard, screen readers, zoom, and touch. | `gncore install responsive-accessibility --apps vscode-codex --scope workspace` |
| `seo-audit` | `/seo-audit` | SEO Audit | Improve technical and content discoverability using crawlable structure and verifiable search metadata. | `gncore install seo-audit --apps vscode-codex --scope workspace` |
| `web-development` | `/web-development` | Web Development | Plan and implement a focused web feature using the repository's existing framework, patterns, and tests. | `gncore install web-development --apps vscode-codex --scope workspace` |
| `web-performance` | `/web-performance` | Web Performance Tuning | Find and fix measured frontend performance bottlenecks without degrading behavior. | `gncore install web-performance --apps vscode-codex --scope workspace` |

## Other targets

GNCore adapters currently include:

- `vscode-chat` — VS Code Chat / Copilot skills
- `vscode-codex` — VS Code Codex skills
- `vscode-claude-code` — VS Code Claude Code skills
- `antigravity` — Google Antigravity
- `github-copilot-chat` — GitHub Copilot Chat
- `claude-desktop` — Claude Desktop managed bundle
- `claude-code` — Claude Code
- `cursor` — Cursor managed bundle
- `windsurf` — Windsurf managed bundle
- `continue-dev` — Continue.dev managed bundle
- `gemini-cli` — Gemini CLI skills
- `openai-codex-cli` — OpenAI Codex CLI

For hosted ChatGPT Skills, export one skill per ZIP and upload it in ChatGPT: `gncore export --app chatgpt --skills company-ceo --output company-ceo.zip`.

Domain and specialist entries use the same shared inspect → plan → implement → test → fix → retest → report contract. The applicable checks depend on the task and the assistant's available tools; the assistant must report checks it did not run.
