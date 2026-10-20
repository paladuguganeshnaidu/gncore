# GNCore Skill Catalog

GNCore 5.0.0 contains **403 portable skills** across **30 domain packs**. Each domain pack contains ten focused workflows.

GNCore is a skill library and export tool. It does not detect, configure, install into, or orchestrate AI applications. Export standard `SKILL.md` folders and copy them to an assistant's documented skills directory, or use `gncore show <skill-id>` to inspect a skill.

## Domain packs

### Company Leadership (`company-leadership`)

Executive and C-suite workflows for company direction, governance, and operating decisions.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `company-ceo` | `/company-ceo` | CEO Decision Brief | Prepare an evidence-led CEO brief for a company-level decision. |
| `company-cfo` | `/company-cfo` | CFO Review | Review financial performance, liquidity, and capital choices for executive decisions. |
| `company-coo` | `/company-coo` | COO Operating Review | Diagnose operational performance and turn bottlenecks into accountable actions. |
| `company-cto` | `/company-cto` | CTO Technology Review | Assess technology direction, engineering execution, and technical risk for leadership. |
| `company-cpo` | `/company-cpo` | Chief Product Officer Review | Align product portfolio decisions with customer evidence and company outcomes. |
| `company-cmo` | `/company-cmo` | Chief Marketing Officer Review | Evaluate marketing strategy, brand health, and growth investment for executives. |
| `company-chro` | `/company-chro` | Chief People Officer Review | Review workforce health, organization design, and talent risks with appropriate privacy. |
| `company-ciso` | `/company-ciso` | Chief Information Security Officer Review | Brief executives on cyber risk, exposure, and risk-reduction decisions. |
| `company-board` | `/company-board` | Board Materials Review | Prepare or review board-level materials for clarity, governance, and decision quality. |
| `company-executive-team` | `/company-executive-team` | Executive Team Alignment | Resolve cross-functional decisions into shared priorities, owners, and measurable commitments. |

### Business Strategy (`business-strategy`)

Company strategy, market positioning, portfolio choices, and strategic execution.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `strategy-market-entry` | `/strategy-market-entry` | Market Entry Strategy | Evaluate entry into a new market using evidence, economics, and staged commitments. |
| `strategy-portfolio` | `/strategy-portfolio` | Portfolio Prioritization | Rank business initiatives by strategic value, evidence, capacity, and opportunity cost. |
| `strategy-competitive` | `/strategy-competitive` | Competitive Analysis | Compare competitors using verifiable evidence and decision-relevant positioning. |
| `strategy-business-model` | `/strategy-business-model` | Business Model Review | Map a business model and test whether its value creation and capture are sustainable. |
| `strategy-scenario` | `/strategy-scenario` | Strategic Scenario Planning | Build plausible scenarios and decision triggers for uncertain business conditions. |
| `strategy-okrs` | `/strategy-okrs` | Strategy to OKRs | Translate strategic intent into measurable outcomes and aligned quarterly objectives. |
| `strategy-pricing` | `/strategy-pricing` | Pricing Strategy | Analyze pricing architecture, willingness-to-pay evidence, and margin consequences. |
| `strategy-risk` | `/strategy-risk` | Enterprise Risk Assessment | Prioritize strategic risks by likelihood, impact, exposure, and mitigation evidence. |
| `strategy-ma` | `/strategy-ma` | M&A Opportunity Screen | Screen an acquisition or partnership opportunity against strategic and financial criteria. |
| `strategy-transformation` | `/strategy-transformation` | Business Transformation Plan | Design a staged transformation with outcomes, governance, adoption, and measurable benefits. |

### Product Management (`product-management`)

Product discovery, roadmaps, requirements, launch readiness, and lifecycle decisions.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `product-opportunity` | `/product-opportunity` | Product Opportunity Brief | Turn customer and business evidence into a scoped product opportunity. |
| `product-requirements` | `/product-requirements` | Product Requirements | Write testable product requirements and acceptance criteria for a scoped feature. |
| `product-roadmap` | `/product-roadmap` | Product Roadmap | Build an outcome-led roadmap that exposes dependencies, confidence, and trade-offs. |
| `product-discovery-sprint` | `/product-discovery-sprint` | Product Discovery Sprint | Plan a short discovery cycle that resolves the riskiest product assumptions. |
| `product-prioritization` | `/product-prioritization` | Feature Prioritization | Prioritize feature requests using customer value, evidence, cost, and strategic fit. |
| `product-experiment` | `/product-experiment` | Product Experiment Design | Design product experiments with a clear hypothesis, metric, guardrails, and decision rule. |
| `product-launch` | `/product-launch` | Product Launch Readiness | Coordinate launch readiness across product, engineering, support, sales, and communications. |
| `product-feedback` | `/product-feedback` | Customer Feedback Synthesis | Synthesize product feedback into traceable themes without overstating frequency. |
| `product-lifecycle` | `/product-lifecycle` | Product Lifecycle Review | Assess adoption, retention, quality, and investment choices for an existing product. |
| `product-metrics` | `/product-metrics` | Product Metrics Definition | Define a product metric with an unambiguous event, population, denominator, and owner. |

### Project and Program Management (`project-program-management`)

Project planning, cross-team delivery, dependencies, status, and recovery.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `project-charter` | `/project-charter` | Project Charter | Create a concise project charter with outcome, scope, ownership, constraints, and decision gates. |
| `project-plan` | `/project-plan` | Delivery Plan | Build an executable delivery plan with milestones, dependencies, owners, and evidence. |
| `project-status` | `/project-status` | Project Status Brief | Produce a truthful project status update with progress, forecast, risks, and asks. |
| `project-risk-log` | `/project-risk-log` | Project Risk Log | Create and maintain actionable project risks, issues, assumptions, and dependencies. |
| `project-recovery` | `/project-recovery` | Project Recovery Plan | Recover a troubled project by identifying root causes and rebaselining achievable outcomes. |
| `project-meeting` | `/project-meeting` | Decision Meeting Preparation | Prepare a meeting agenda and decision record that uses participant time effectively. |
| `project-dependency` | `/project-dependency` | Dependency Coordination | Map and resolve cross-team dependencies before they become delivery blockers. |
| `project-capacity` | `/project-capacity` | Capacity and Resource Plan | Match project demand to available skills, capacity, and protected operational work. |
| `project-retro` | `/project-retro` | Project Retrospective | Run a blameless retrospective that yields specific, owned process improvements. |
| `project-closure` | `/project-closure` | Project Closure and Handoff | Close a project with accepted deliverables, operational ownership, records, and lessons. |

### Business Operations (`business-operations`)

Repeatable company operations, service quality, process design, and operational control.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `operations-process-map` | `/operations-process-map` | Process Mapping | Map a business process from trigger to outcome and expose waste and control gaps. |
| `operations-sop` | `/operations-sop` | Standard Operating Procedure | Write an actionable SOP with prerequisites, steps, decision points, and recovery paths. |
| `operations-kpi` | `/operations-kpi` | Operations KPI Review | Analyze operational KPIs against service outcomes, baselines, and capacity limits. |
| `operations-quality` | `/operations-quality` | Service Quality Improvement | Reduce recurring service defects through root-cause analysis and controlled countermeasures. |
| `operations-capacity` | `/operations-capacity` | Capacity and Queue Planning | Forecast service capacity and queues with explicit demand, throughput, and uncertainty. |
| `operations-control` | `/operations-control` | Operational Control Design | Design practical controls that prevent or detect costly process failures. |
| `operations-incident` | `/operations-incident` | Business Operations Incident | Coordinate a non-technical operational incident and restore service with clear ownership. |
| `operations-vendor` | `/operations-vendor` | Vendor Operations Review | Review vendor delivery against service commitments, risks, dependencies, and corrective actions. |
| `operations-continuity` | `/operations-continuity` | Business Continuity Plan | Prepare a business continuity response for essential processes and credible disruption scenarios. |
| `operations-automation` | `/operations-automation` | Operations Automation Case | Assess whether an operational task is ready for safe automation and quantify its value. |

### Sales and Revenue (`sales-revenue`)

Pipeline management, account planning, proposals, forecasting, and revenue operations.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `sales-account-plan` | `/sales-account-plan` | Strategic Account Plan | Create an account plan based on customer outcomes, stakeholders, risks, and verified activity. |
| `sales-discovery` | `/sales-discovery` | Sales Discovery | Prepare neutral discovery questions that uncover customer needs, impact, constraints, and decision process. |
| `sales-qualification` | `/sales-qualification` | Opportunity Qualification | Assess opportunity fit and deal risk using transparent qualification evidence. |
| `sales-pipeline` | `/sales-pipeline` | Pipeline Review | Inspect pipeline quality and next-step integrity to improve forecast and coaching. |
| `sales-forecast` | `/sales-forecast` | Revenue Forecast | Build a revenue forecast with explicit assumptions, scenarios, and confidence. |
| `sales-proposal` | `/sales-proposal` | Customer Proposal | Draft a customer proposal tied to stated needs, outcomes, scope, assumptions, and evidence. |
| `sales-negotiation` | `/sales-negotiation` | Commercial Negotiation Preparation | Prepare negotiation options and concession boundaries grounded in approved commercial policy. |
| `sales-objection` | `/sales-objection` | Customer Objection Response | Answer a sales objection with accurate evidence and a useful next question. |
| `sales-territory` | `/sales-territory` | Territory and Coverage Plan | Balance account coverage and sales capacity across a territory using transparent criteria. |
| `sales-renewal` | `/sales-renewal` | Renewal and Expansion Plan | Protect a renewal by connecting adoption, realized outcomes, risks, and agreed next value. |

### Marketing and Growth (`marketing-growth`)

Positioning, campaigns, content, lifecycle, demand generation, and marketing measurement.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `marketing-positioning` | `/marketing-positioning` | Positioning and Messaging | Develop evidence-based positioning for a defined audience and competitive context. |
| `marketing-campaign` | `/marketing-campaign` | Campaign Plan | Plan a campaign with audience, offer, channels, budget, measurement, and approval gates. |
| `marketing-content` | `/marketing-content` | Marketing Content Brief | Brief content creators with audience need, purpose, evidence, voice, format, and success criteria. |
| `marketing-seo` | `/marketing-seo` | Search Content Audit | Audit search content for intent match, accuracy, technical discoverability, and useful next actions. |
| `marketing-lifecycle` | `/marketing-lifecycle` | Lifecycle Messaging | Design lifecycle messages that help users reach a meaningful product outcome. |
| `marketing-attribution` | `/marketing-attribution` | Marketing Attribution Review | Interpret marketing contribution while exposing attribution model limitations and incrementality. |
| `marketing-brand` | `/marketing-brand` | Brand Consistency Review | Review brand execution for message consistency, audience fit, accessibility, and evidence. |
| `marketing-social` | `/marketing-social` | Social Media Plan | Create a platform-aware social plan with useful content, response ownership, and risk controls. |
| `marketing-budget` | `/marketing-budget` | Marketing Budget Allocation | Allocate marketing budget using marginal returns, uncertainty, and strategic coverage. |
| `marketing-launch` | `/marketing-launch` | Go-to-Market Launch | Coordinate market launch readiness across product, pricing, channels, enablement, and customer support. |

### Finance and Accounting (`finance-accounting`)

Budgeting, forecasting, reporting, bookkeeping controls, and financial analysis support.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `finance-budget` | `/finance-budget` | Budget Build | Build a traceable budget from operational drivers, assumptions, owners, and approved targets. |
| `finance-forecast` | `/finance-forecast` | Rolling Forecast | Update a rolling forecast from actuals and current business drivers without hiding variance. |
| `finance-variance` | `/finance-variance` | Financial Variance Analysis | Explain financial variance by volume, price, mix, timing, and one-time effects. |
| `finance-cashflow` | `/finance-cashflow` | Cash Flow and Runway | Model cash needs and runway using explicit receipts, obligations, and timing scenarios. |
| `finance-unit-economics` | `/finance-unit-economics` | Unit Economics | Calculate unit economics with consistent cohort, cost allocation, and contribution assumptions. |
| `finance-month-close` | `/finance-month-close` | Month-End Close Checklist | Coordinate a complete month-end close with reconciliations, owners, evidence, and review. |
| `finance-controls` | `/finance-controls` | Financial Controls Review | Review financial process controls for authorization, reconciliation, evidence, and segregation. |
| `finance-investment-case` | `/finance-investment-case` | Investment Business Case | Build a decision-ready capital request with costs, benefits, alternatives, and sensitivity. |
| `finance-expense` | `/finance-expense` | Expense Policy Review | Assess expense submissions against supplied policy with consistent evidence and escalation. |
| `finance-report` | `/finance-report` | Financial Report Review | Review a financial report for arithmetic, consistency, labels, source traceability, and decision clarity. |

### People and Human Resources (`people-human-resources`)

Hiring, onboarding, development, performance, workforce planning, and employee operations.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `people-role-design` | `/people-role-design` | Role Design | Define a role around outcomes, decision rights, essential skills, and fair selection criteria. |
| `people-job-post` | `/people-job-post` | Job Description | Draft an inclusive, accurate job description from an approved role profile. |
| `people-interview` | `/people-interview` | Structured Interview Plan | Create a structured interview plan with job-related questions and consistent evaluation anchors. |
| `people-onboarding` | `/people-onboarding` | Employee Onboarding Plan | Plan a role-specific onboarding path with access, learning, relationships, and early outcomes. |
| `people-development` | `/people-development` | Development Plan | Create a practical employee development plan linked to goals, strengths, and supported practice. |
| `people-performance` | `/people-performance` | Performance Review Support | Organize performance evidence into a fair, specific, and balanced review draft. |
| `people-workforce-plan` | `/people-workforce-plan` | Workforce Plan | Forecast workforce capacity and skills against business demand and approved scenarios. |
| `people-engagement` | `/people-engagement` | Engagement Survey Analysis | Analyze employee feedback responsibly while protecting confidentiality and avoiding false precision. |
| `people-policy` | `/people-policy` | HR Policy Draft Review | Review an HR policy draft for clarity, internal consistency, accessibility, and escalation needs. |
| `people-offboarding` | `/people-offboarding` | Employee Offboarding Checklist | Coordinate a respectful offboarding with access, knowledge transfer, property, records, and final responsibilities. |

### Customer Success and Support (`customer-success-support`)

Customer onboarding, support triage, service recovery, knowledge, and retention workflows.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `customer-onboarding` | `/customer-onboarding` | Customer Onboarding Plan | Guide a customer to a defined first outcome with owners, milestones, and adoption signals. |
| `customer-support-triage` | `/customer-support-triage` | Support Case Triage | Classify a support issue by impact, urgency, reproducibility, and routing evidence. |
| `customer-reply` | `/customer-reply` | Customer Support Reply | Draft a clear customer reply that addresses the issue, next action, and known limits. |
| `customer-escalation` | `/customer-escalation` | Customer Escalation Brief | Prepare an escalation brief with impact, timeline, evidence, owner, and decision request. |
| `customer-health` | `/customer-health` | Customer Health Review | Assess customer health from transparent adoption, outcome, relationship, and support signals. |
| `customer-renewal` | `/customer-renewal` | Customer Renewal Risk | Build a renewal action plan grounded in value realization, stakeholder needs, and contract facts. |
| `customer-knowledge` | `/customer-knowledge` | Support Knowledge Article | Write a tested support article that resolves a common issue with clear prerequisites and recovery. |
| `customer-voice` | `/customer-voice` | Voice of Customer Synthesis | Combine customer evidence into actionable themes with source coverage and counterexamples. |
| `customer-service-recovery` | `/customer-service-recovery` | Service Recovery Plan | Restore trust after a service failure through verified facts, ownership, and follow-through. |
| `customer-success-qbr` | `/customer-success-qbr` | Customer Business Review | Prepare a customer review that connects usage, outcomes, open risks, and next-period goals. |

### Legal and Compliance Support (`legal-compliance`)

Organize legal and compliance work for review by authorized professionals; not a substitute for counsel.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `legal-contract-intake` | `/legal-contract-intake` | Contract Review Intake | Extract obligations, deadlines, and questions from a supplied contract for counsel review. |
| `legal-obligation-map` | `/legal-obligation-map` | Obligation Tracker | Turn contract or policy text into traceable obligations, owners, dates, and evidence. |
| `legal-policy-gap` | `/legal-policy-gap` | Compliance Gap Assessment | Compare supplied controls or evidence against a named policy or framework requirement. |
| `legal-privacy-intake` | `/legal-privacy-intake` | Privacy Review Intake | Structure a privacy review by mapping purpose, data, access, retention, and user impact. |
| `legal-regulatory-watch` | `/legal-regulatory-watch` | Regulatory Change Brief | Summarize a supplied regulatory update and identify affected business processes for expert review. |
| `legal-incident-hold` | `/legal-incident-hold` | Legal Hold Coordination Checklist | Organize a preservation checklist from authorized instructions without altering source records. |
| `legal-marketing-claims` | `/legal-marketing-claims` | Marketing Claims Review | Trace public claims to substantiation and flag claims needing legal or regulatory review. |
| `legal-entity-records` | `/legal-entity-records` | Corporate Records Checklist | Organize entity governance records and upcoming filing or approval actions from supplied records. |
| `legal-dispute-chronology` | `/legal-dispute-chronology` | Dispute Chronology | Build a source-linked chronology from supplied dispute materials for counsel review. |
| `legal-review-memo` | `/legal-review-memo` | Legal Review Memo Support | Draft a neutral issue-and-evidence memo for a qualified lawyer to review. |

### Procurement and Vendor Management (`procurement-vendor`)

Responsible sourcing, vendor selection, contract administration, and supplier performance.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `procurement-requirements` | `/procurement-requirements` | Procurement Requirements | Translate a business need into measurable, vendor-neutral procurement requirements. |
| `procurement-rfp` | `/procurement-rfp` | RFP Package | Prepare a fair request for proposal with scope, scoring, schedule, and response instructions. |
| `procurement-scorecard` | `/procurement-scorecard` | Vendor Scorecard | Score supplier proposals against published criteria with evidence and consistent normalization. |
| `procurement-total-cost` | `/procurement-total-cost` | Total Cost of Ownership | Compare vendor options across implementation, usage, support, renewal, exit, and risk costs. |
| `procurement-due-diligence` | `/procurement-due-diligence` | Supplier Due Diligence | Coordinate risk-based supplier due diligence across security, privacy, finance, and continuity. |
| `procurement-negotiation` | `/procurement-negotiation` | Supplier Negotiation Plan | Prepare negotiation priorities and fallback options within approved procurement authority. |
| `procurement-onboarding` | `/procurement-onboarding` | Supplier Onboarding | Coordinate supplier onboarding with least-privilege access, ownership, and required control evidence. |
| `procurement-performance` | `/procurement-performance` | Supplier Performance Review | Review vendor service against contracted outcomes, service levels, and corrective actions. |
| `procurement-renewal` | `/procurement-renewal` | Vendor Renewal Review | Make a renewal decision using value, risk, alternatives, usage, and notice deadlines. |
| `procurement-exit` | `/procurement-exit` | Supplier Exit Plan | Plan a controlled supplier transition that protects service, data, access, and records. |

### Entrepreneurship and New Ventures (`entrepreneurship`)

Validate new business ideas, launch plans, early economics, and founder decisions.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `venture-idea` | `/venture-idea` | Venture Idea Screen | Screen a venture idea by customer problem, alternatives, evidence, and founder constraints. |
| `venture-customer-interview` | `/venture-customer-interview` | Customer Interview Guide | Prepare non-leading interviews that test customer behavior and unmet needs. |
| `venture-mvp` | `/venture-mvp` | Minimum Viable Product Scope | Choose the smallest product experiment that can test a critical venture assumption. |
| `venture-business-model` | `/venture-business-model` | Venture Business Model | Map the venture's customer, value, channel, cost, revenue, and operating assumptions. |
| `venture-business-plan` | `/venture-business-plan` | Business Plan Draft | Create a decision-focused business plan with evidence, assumptions, execution, and capital needs. |
| `venture-fundraise` | `/venture-fundraise` | Fundraising Preparation | Organize fundraising narrative, evidence, materials, and diligence readiness. |
| `venture-runway` | `/venture-runway` | Founder Runway Scenarios | Model startup runway and options under base, downside, and financing scenarios. |
| `venture-go-to-market` | `/venture-go-to-market` | Early Go-to-Market Test | Design a low-cost channel test for an early product with a measurable learning objective. |
| `venture-founder-agreement` | `/venture-founder-agreement` | Founder Alignment Checklist | Surface founder-role, decision, equity, vesting, and conflict questions for professional review. |
| `venture-pivot-review` | `/venture-pivot-review` | Pivot or Persevere Review | Decide whether to continue, adjust, or stop a venture hypothesis from observed evidence. |

### Software Engineering (`software-engineering`)

Software architecture, implementation, code review, maintenance, and release quality.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `software-feature` | `/software-feature` | Software Feature Delivery | Deliver a scoped software feature using local conventions and verifiable acceptance criteria. |
| `software-architecture` | `/software-architecture` | Software Architecture Decision | Compare architecture options against constraints, operations, reversibility, and lifecycle cost. |
| `software-code-review` | `/software-code-review` | Software Code Review | Review a code change for correctness, security, maintainability, and missing regression coverage. |
| `software-debugging` | `/software-debugging` | Software Debugging | Diagnose a software failure from reproducible evidence and verify the smallest safe fix. |
| `software-refactor` | `/software-refactor` | Safe Refactoring | Refactor a bounded code area while preserving its documented behavior and public contracts. |
| `software-api-contract` | `/software-api-contract` | Software API Contract | Define and verify an API contract across request, response, errors, versioning, and consumers. |
| `software-dependency` | `/software-dependency` | Dependency Change Review | Assess and implement a dependency change with compatibility, security, and rollback evidence. |
| `software-performance` | `/software-performance` | Software Performance Optimization | Find a measured software bottleneck and optimize it without regressing correctness. |
| `software-migration` | `/software-migration` | Software Migration Plan | Plan a staged migration with compatibility gates, data safety, and rollback criteria. |
| `software-release` | `/software-release` | Software Release Candidate | Prepare a software release with reproducible artifacts, verified changes, and rollback readiness. |

### Data Analytics and Intelligence (`data-analytics`)

Business intelligence, data quality, metrics, dashboards, and decision analysis.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `analytics-question` | `/analytics-question` | Analytics Question Plan | Translate a business question into a measurable analysis plan and data requirements. |
| `analytics-data-audit` | `/analytics-data-audit` | Data Quality Audit | Audit analytical data for missingness, duplication, validity, freshness, and grain. |
| `analytics-sql` | `/analytics-sql` | Business SQL Analysis | Write a traceable SQL analysis with correct grain, joins, time handling, and reconciliation. |
| `analytics-dashboard` | `/analytics-dashboard` | Decision Dashboard | Design a dashboard around a recurring decision with clear metrics, filters, and data freshness. |
| `analytics-metric-tree` | `/analytics-metric-tree` | Metric Tree | Decompose a business outcome into leading drivers and measurable operational inputs. |
| `analytics-cohort` | `/analytics-cohort` | Cohort Analysis | Compare cohort behavior with consistent definitions, exposure windows, and censoring treatment. |
| `analytics-experiment` | `/analytics-experiment` | Business Experiment Analysis | Analyze an experiment with assignment, exposure, predeclared outcomes, and uncertainty checks. |
| `analytics-forecast` | `/analytics-forecast` | Business Forecast Analysis | Build a business forecast from history, drivers, scenarios, and out-of-sample checks. |
| `analytics-insight-brief` | `/analytics-insight-brief` | Executive Analytics Brief | Turn analysis into a concise decision brief with traceable evidence and caveats. |
| `analytics-data-contract` | `/analytics-data-contract` | Analytics Data Contract | Specify ownership, schema, quality, freshness, and change handling for an analytics dataset. |

### AI and Machine Learning (`ai-machine-learning`)

Machine learning, model training, evaluation, LLM, retrieval, and responsible release workflows.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `ml-problem-framing` | `/ml-problem-framing` | ML Problem Framing | Decide whether a machine learning approach fits the task, data, constraints, and failure costs. |
| `ml-dataset-audit` | `/ml-dataset-audit` | ML Dataset Audit | Audit dataset provenance, schema, representativeness, label quality, leakage, and split strategy. |
| `ml-preprocessing-pipeline` | `/ml-preprocessing-pipeline` | ML Preprocessing Pipeline | Build deterministic preprocessing that prevents leakage and preserves training-to-serving parity. |
| `ml-model-train` | `/ml-model-train` | ML Model Training Run | Implement a reproducible model training run with configuration, baseline, checkpoints, and evaluation. |
| `ml-model-evaluation` | `/ml-model-evaluation` | ML Model Evaluation | Evaluate model quality, uncertainty, subgroup behavior, and representative errors against a baseline. |
| `ml-model-improvement` | `/ml-model-improvement` | ML Improvement Loop | Improve a model through controlled experiments with a fixed evaluation protocol and root-cause analysis. |
| `ml-llm-evaluation` | `/ml-llm-evaluation` | LLM Evaluation Suite | Evaluate an LLM feature with representative tasks, rubrics, adversarial cases, latency, and cost. |
| `ml-rag` | `/ml-rag` | RAG Grounding Workflow | Build and evaluate retrieval-augmented answers with source access controls and abstention. |
| `ml-finetuning` | `/ml-finetuning` | Model Fine-Tuning Plan | Assess fine-tuning suitability and prepare a controlled, leakage-safe fine-tuning workflow. |
| `ml-release-monitor` | `/ml-release-monitor` | Model Release and Monitoring | Prepare a model release with provenance, compatibility, rollback, and drift monitoring gates. |

### Cybersecurity (`cybersecurity`)

Defensive security engineering, threat analysis, incident response, and security assurance.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `cyber-threat-model` | `/cyber-threat-model` | Threat Model | Map assets, trust boundaries, threats, controls, and residual risk for a bounded system. |
| `cyber-secure-code` | `/cyber-secure-code` | Secure Code Review | Review a code change for exploitable input, identity, authorization, secret, and data-flow flaws. |
| `cyber-vulnerability-triage` | `/cyber-vulnerability-triage` | Vulnerability Triage | Prioritize a reported vulnerability using affected assets, exploitability, exposure, and impact evidence. |
| `cyber-incident-response` | `/cyber-incident-response` | Cyber Incident Response | Coordinate defensive incident response with containment, evidence preservation, and recovery gates. |
| `cyber-identity-access` | `/cyber-identity-access` | Identity and Access Review | Review identities and permissions for least privilege, lifecycle, ownership, and audit evidence. |
| `cyber-cloud-review` | `/cyber-cloud-review` | Cloud Security Review | Assess cloud configuration against an explicit threat model and approved security baseline. |
| `cyber-security-controls` | `/cyber-security-controls` | Security Control Evidence | Map supplied evidence to security control requirements with traceable, bounded conclusions. |
| `cyber-phishing` | `/cyber-phishing` | Phishing Response Triage | Triage a suspected phishing report and provide safe containment and user guidance. |
| `cyber-secret-response` | `/cyber-secret-response` | Exposed Secret Response | Respond to a potentially exposed credential without echoing or spreading the secret. |
| `cyber-security-test-plan` | `/cyber-security-test-plan` | Authorized Security Test Plan | Define a bounded security test plan with written authorization, targets, limits, and stop conditions. |

### Cloud, DevOps, and SRE (`cloud-devops-sre`)

Infrastructure, delivery automation, service reliability, cost, and production operations.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `cloud-architecture-review` | `/cloud-architecture-review` | Cloud Architecture Review | Compare cloud designs against workload, reliability, security, cost, and operational constraints. |
| `cloud-infrastructure-code` | `/cloud-infrastructure-code` | Infrastructure as Code | Author or review infrastructure changes with plan inspection, least privilege, and rollback. |
| `cloud-ci-cd` | `/cloud-ci-cd` | CI/CD Pipeline | Improve a delivery pipeline with reproducibility, least privilege, useful gates, and rollback. |
| `cloud-container` | `/cloud-container` | Container Build and Hardening | Build a reproducible container with a minimal attack surface and reliable runtime behavior. |
| `cloud-kubernetes` | `/cloud-kubernetes` | Kubernetes Workload Review | Review Kubernetes workloads for availability, resource bounds, identity, health, and rollout safety. |
| `cloud-slo` | `/cloud-slo` | SLO and Error Budget | Define service-level indicators and objectives that reflect user-visible reliability. |
| `cloud-observability` | `/cloud-observability` | Service Observability | Instrument service behavior with actionable metrics, structured logs, and traces. |
| `cloud-incident` | `/cloud-incident` | SRE Incident Management | Manage a reliability incident through impact assessment, safe mitigation, verification, and learning. |
| `cloud-capacity` | `/cloud-capacity` | Capacity and Load Plan | Plan service capacity using measured demand, bottleneck data, growth uncertainty, and failure headroom. |
| `cloud-cost` | `/cloud-cost` | Cloud Cost Optimization | Reduce measurable infrastructure spend while protecting service objectives and recovery options. |

### Quality Engineering and Testing (`quality-engineering`)

Test design, automation, release assurance, defect analysis, and quality improvement.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `qa-test-strategy` | `/qa-test-strategy` | Test Strategy | Choose a risk-based test mix that verifies behavior at the lowest effective level. |
| `qa-test-design` | `/qa-test-design` | Test Case Design | Turn a behavior contract into clear positive, negative, boundary, and state-transition tests. |
| `qa-automation` | `/qa-automation` | Test Automation | Build maintainable test automation with stable setup, deterministic data, and actionable failures. |
| `qa-e2e` | `/qa-e2e` | End-to-End User Journey Test | Verify a critical user journey across the application with realistic but isolated data. |
| `qa-api-contract` | `/qa-api-contract` | API Contract Testing | Check API compatibility, validation, authorization, and error contracts between services. |
| `qa-performance` | `/qa-performance` | Performance Test Plan | Measure a service against representative load, latency, throughput, and resource objectives. |
| `qa-accessibility` | `/qa-accessibility` | Accessibility Test Pass | Test a flow for keyboard operation, semantics, focus, labels, zoom, and assistive technology support. |
| `qa-defect-triage` | `/qa-defect-triage` | Defect Triage | Classify and prioritize a defect using reproducibility, user impact, scope, and workaround evidence. |
| `qa-release-gate` | `/qa-release-gate` | Release Quality Gate | Evaluate release evidence against agreed quality gates and make residual risk visible. |
| `qa-flaky-test` | `/qa-flaky-test` | Flaky Test Investigation | Find the cause of an intermittent test failure and confirm a stable correction. |

### Design, UX, and Accessibility (`design-ux`)

User research, interface design, content hierarchy, design systems, and usability validation.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `design-ux-audit` | `/design-ux-audit` | UX Usability Audit | Audit a user flow for task clarity, feedback, recovery, cognitive load, and accessibility. |
| `design-user-flow` | `/design-user-flow` | User Flow Design | Map a user journey with entry points, decisions, states, errors, and successful completion. |
| `design-wireframe` | `/design-wireframe` | Wireframe Specification | Specify a wireframe around user priorities, information hierarchy, and responsive states. |
| `design-minimal` | `/design-minimal` | Minimalist UI Direction | Create a restrained interface with clear hierarchy, intentional whitespace, and accessible controls. |
| `design-expressive` | `/design-expressive` | Expressive UI Direction | Create a distinctive, layered interface without sacrificing navigation, readability, or accessibility. |
| `design-system-component` | `/design-system-component` | Design System Component | Specify a reusable design-system component with API, states, semantics, and adoption guidance. |
| `design-content` | `/design-content` | UX Content Design | Write interface text that helps users understand choices, status, errors, and recovery. |
| `design-prototype` | `/design-prototype` | Prototype Test Plan | Create a prototype test plan that resolves a specific interaction or comprehension question. |
| `design-accessibility` | `/design-accessibility` | Accessible Interaction Design | Design keyboard, screen-reader, motion, contrast, and touch behavior into an interaction. |
| `design-handoff` | `/design-handoff` | Design to Engineering Handoff | Prepare a design handoff with behavior, states, assets, responsive rules, and unresolved questions. |

### Microsoft Word and DOCX Documents (`word-documents`)

Create, revise, format, redline, and verify Word documents and DOCX deliverables.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `word-draft` | `/word-draft` | Draft a Word Document | Create a structured Word document from a brief, source material, and intended audience. |
| `word-edit` | `/word-edit` | Edit and Restructure DOCX | Edit an existing Word document for clarity and structure while preserving required content. |
| `word-format` | `/word-format` | Word Formatting Repair | Repair Word styles, spacing, headers, pagination, tables, and section layout. |
| `word-redline` | `/word-redline` | Word Tracked Changes Review | Prepare or review DOCX edits with traceable changes and comments for human approval. |
| `word-accessibility` | `/word-accessibility` | Accessible Word Document | Improve DOCX structure and accessibility for navigation, screen readers, and document reuse. |
| `word-template` | `/word-template` | Word Template Design | Create a reusable Word template with stable styles, fields, sections, and usage rules. |
| `word-report` | `/word-report` | Word Report Production | Produce a sourced report in Word with executive summary, evidence, findings, and appendices. |
| `word-merge` | `/word-merge` | Word Document Merge | Combine supplied DOCX materials into one coherent document without losing provenance or structure. |
| `word-forms` | `/word-forms` | Word Form Design | Design a fillable Word form with clear labels, logical completion order, and safe review. |
| `word-review` | `/word-review` | Word Final Proof and QA | Proofread a final DOCX for content consistency, references, fields, and page-level layout. |

### PDF Documents (`pdf-documents`)

Extract, create, combine, review, secure, and validate PDF files.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `pdf-extract` | `/pdf-extract` | PDF Text and Table Extraction | Extract text or tables from a supplied PDF while preserving page references and uncertainty. |
| `pdf-create` | `/pdf-create` | Create a PDF Deliverable | Create a clean PDF from approved source content and verify its page layout and metadata. |
| `pdf-accessibility` | `/pdf-accessibility` | Accessible PDF Review | Review or improve PDF tags, reading order, headings, links, tables, and alternative text. |
| `pdf-merge` | `/pdf-merge` | Merge PDFs | Combine approved PDFs in a defined order while preserving page integrity and source provenance. |
| `pdf-split` | `/pdf-split` | Split PDF by Page or Section | Split a PDF into named outputs using explicit page ranges or verified section boundaries. |
| `pdf-form` | `/pdf-form` | PDF Form Workflow | Inspect or create a fillable PDF form with labeled fields and reliable save behavior. |
| `pdf-ocr` | `/pdf-ocr` | Scanned PDF OCR | Make a scanned PDF searchable with OCR and verify text against original page images. |
| `pdf-redaction` | `/pdf-redaction` | PDF Redaction Review | Apply and verify permanent redaction to specifically authorized PDF content. |
| `pdf-review` | `/pdf-review` | PDF Content and Layout Review | Review PDF content, links, references, page numbering, and rendered layout before delivery. |
| `pdf-signature` | `/pdf-signature` | PDF Signature Workflow Support | Prepare a PDF for an authorized signature workflow and verify fields and final artifact integrity. |

### Presentations and PowerPoint (`presentations-powerpoint`)

Plan, create, edit, and inspect persuasive, accessible presentation decks and PPTX files.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `ppt-storyline` | `/ppt-storyline` | Presentation Storyline | Turn an audience, decision, and evidence set into a coherent presentation narrative. |
| `ppt-create` | `/ppt-create` | Create a PowerPoint Deck | Create a presentation deck from a brief and source material with a clear storyline and consistent design. |
| `ppt-executive` | `/ppt-executive` | Executive Presentation | Prepare an executive deck that leads with decisions, implications, risks, and evidence. |
| `ppt-data-story` | `/ppt-data-story` | Data Story Presentation | Explain data in slides with faithful charts, denominators, uncertainty, and a decision-relevant takeaway. |
| `ppt-visual-design` | `/ppt-visual-design` | Presentation Visual Design | Improve slide hierarchy, typography, color, alignment, and visual consistency without weakening content. |
| `ppt-edit` | `/ppt-edit` | Edit an Existing PPTX | Revise an existing deck while preserving intended content, theme, and editable structure. |
| `ppt-speaker-notes` | `/ppt-speaker-notes` | Speaker Notes and Talk Track | Write speaker notes that support a timed presentation without duplicating slide text. |
| `ppt-accessibility` | `/ppt-accessibility` | Accessible Presentation | Review a presentation for reading order, contrast, meaningful text, captions, and accessible charts. |
| `ppt-template` | `/ppt-template` | PowerPoint Template Design | Create a reusable PowerPoint template with reliable masters, layouts, typography, and color tokens. |
| `ppt-deck-qa` | `/ppt-deck-qa` | PowerPoint Deck QA | Run a final slide-by-slide quality pass on a saved presentation and its exported PDF. |

### Spreadsheets and Excel (`spreadsheets`)

Create, analyze, validate, and present spreadsheet workbooks with reliable formulas and data controls.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `sheet-model` | `/sheet-model` | Spreadsheet Model Design | Structure a spreadsheet model with clear inputs, calculations, outputs, and traceable assumptions. |
| `sheet-formula-audit` | `/sheet-formula-audit` | Spreadsheet Formula Audit | Audit workbook formulas for broken references, inconsistencies, hard-codes, and calculation errors. |
| `sheet-clean` | `/sheet-clean` | Spreadsheet Data Cleaning | Clean tabular spreadsheet data with explicit rules and before/after reconciliation. |
| `sheet-analysis` | `/sheet-analysis` | Spreadsheet Data Analysis | Answer an analytical question from workbook data with transparent formulas and checks. |
| `sheet-dashboard` | `/sheet-dashboard` | Spreadsheet Dashboard | Build a decision-focused spreadsheet dashboard with stable formulas, labels, filters, and accessible visuals. |
| `sheet-pivot` | `/sheet-pivot` | Pivot Table Analysis | Create or review pivot analyses with verified source range, grouping, aggregation, and filter behavior. |
| `sheet-forecast` | `/sheet-forecast` | Spreadsheet Forecast Model | Build or audit a forecast workbook with driver-based assumptions, scenarios, and error checks. |
| `sheet-reconcile` | `/sheet-reconcile` | Spreadsheet Reconciliation | Reconcile two data sources with stable keys, exception categories, and totals control. |
| `sheet-automation` | `/sheet-automation` | Spreadsheet Automation | Automate repetitive workbook transformations with idempotent runs and safe output handling. |
| `sheet-presentation` | `/sheet-presentation` | Spreadsheet Presentation Cleanup | Prepare a workbook for review or print with consistent formats, frozen headers, page setup, and clear labels. |

### Research and Market Intelligence (`research-market-intelligence`)

Source-led research, literature review, market sizing, synthesis, and evidence management.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `research-question` | `/research-question` | Research Question Design | Frame a researchable question with scope, definitions, evidence criteria, and a useful decision. |
| `research-source-audit` | `/research-source-audit` | Source Quality Audit | Evaluate sources for authority, method, date, provenance, conflicts, and fitness for a claim. |
| `research-literature-review` | `/research-literature-review` | Literature Review | Synthesize a literature set with methods, findings, disagreement, and evidence gaps visible. |
| `research-market-size` | `/research-market-size` | Market Sizing | Estimate a market using transparent bottom-up or top-down assumptions and sensitivity ranges. |
| `research-customer` | `/research-customer` | Customer and Market Research | Combine customer evidence and market signals into actionable, bounded insights. |
| `research-competitor` | `/research-competitor` | Competitive Research Brief | Prepare a dated competitor brief from verifiable product, pricing, and positioning evidence. |
| `research-evidence-map` | `/research-evidence-map` | Evidence Map | Organize claims, sources, strength, disagreement, and missing evidence for a decision area. |
| `research-survey` | `/research-survey` | Survey Design and Review | Design a survey with neutral wording, clear constructs, representative sampling, and privacy safeguards. |
| `research-brief` | `/research-brief` | Research Brief | Turn research into a concise, sourced brief with answer, confidence, implications, and open questions. |
| `research-monitor` | `/research-monitor` | Research Update Monitor | Track a defined topic for material source changes without overwhelming users with routine noise. |

### Education and Learning (`education-learning`)

Curriculum, teaching materials, assessment, tutoring, accessibility, and learner feedback.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `education-learning-objectives` | `/education-learning-objectives` | Learning Objectives | Write measurable learning objectives aligned with learner needs, prerequisites, practice, and assessment. |
| `education-lesson` | `/education-lesson` | Lesson Plan | Plan a lesson with sequenced explanation, active practice, feedback, and accessible timing. |
| `education-curriculum` | `/education-curriculum` | Curriculum Map | Organize a curriculum into coherent progression, prerequisite links, practice, and assessment. |
| `education-assessment` | `/education-assessment` | Assessment Design | Create an assessment aligned to learning outcomes with clear instructions and fair scoring. |
| `education-rubric` | `/education-rubric` | Scoring Rubric | Develop a behavior-anchored rubric that supports consistent feedback and grading. |
| `education-study-guide` | `/education-study-guide` | Study Guide | Create a focused study guide with key concepts, retrieval practice, examples, and self-check answers. |
| `education-tutor` | `/education-tutor` | Tutoring Session | Tutor a learner by diagnosing understanding, guiding practice, and adapting explanations. |
| `education-content-accessibility` | `/education-content-accessibility` | Accessible Learning Material | Adapt learning content for accessible navigation, language, formats, and participation. |
| `education-feedback` | `/education-feedback` | Learner Feedback Synthesis | Synthesize learner feedback into evidence-based course improvements while protecting privacy. |
| `education-course-review` | `/education-course-review` | Course Quality Review | Review a course for alignment among objectives, instruction, practice, assessment, workload, and accessibility. |

### Healthcare Operations (`healthcare-operations`)

Administrative workflows for access, quality, privacy, and operational coordination; no clinical diagnosis or treatment.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `healthcare-intake` | `/healthcare-intake` | Healthcare Intake | Improve administrative intake completeness, routing, accessibility, and privacy. |
| `healthcare-scheduling` | `/healthcare-scheduling` | Healthcare Scheduling | Coordinate appointments using supplied policies and patient preferences. |
| `healthcare-operations-map` | `/healthcare-operations-map` | Healthcare Operations Map | Map administrative handoffs, delays, duplication, and ownership gaps. |
| `healthcare-quality` | `/healthcare-quality` | Healthcare Quality Operations | Organize quality improvement with defined measures, owners, and review cycles. |
| `healthcare-privacy` | `/healthcare-privacy` | Healthcare Privacy Review | Review artifacts for privacy exposure and minimum-necessary handling. |
| `healthcare-policy` | `/healthcare-policy` | Healthcare Policy Operations | Maintain operational policies with ownership, evidence, and review dates. |
| `healthcare-patient-comms` | `/healthcare-patient-comms` | Patient Administrative Communications | Write clear non-clinical communications about administrative next steps. |
| `healthcare-audit` | `/healthcare-audit` | Healthcare Operations Audit | Review administrative controls and remediation with an evidence trail. |
| `healthcare-capacity` | `/healthcare-capacity` | Healthcare Capacity Planning | Model service capacity using operational data and explicit assumptions. |
| `healthcare-improvement` | `/healthcare-improvement` | Healthcare Improvement Cycle | Plan and assess a bounded operational improvement with safeguards. |

### E-commerce and Retail (`ecommerce-retail`)

Catalog, merchandising, conversion, inventory, customer support, and retail operations.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `retail-catalog` | `/retail-catalog` | Product Catalog Quality | Improve product data completeness, consistency, and variant accuracy. |
| `retail-merchandising` | `/retail-merchandising` | Retail Merchandising | Align merchandising with customer intent, stock, margin, and brand. |
| `retail-conversion` | `/retail-conversion` | Conversion Review | Diagnose page and checkout friction with evidence and prioritized experiments. |
| `retail-pricing` | `/retail-pricing` | Retail Pricing Analysis | Analyze prices, discounts, and margin with traceable sources. |
| `retail-inventory` | `/retail-inventory` | Retail Inventory Operations | Review inventory signals and replenishment exceptions. |
| `retail-campaign` | `/retail-campaign` | Retail Campaign Planning | Plan campaigns with stock, audience, creative, and measurement aligned. |
| `retail-reviews` | `/retail-reviews` | Customer Review Synthesis | Summarize reviews without fabricating or overstating customer evidence. |
| `retail-returns` | `/retail-returns` | Returns and Refund Analysis | Find return patterns while preserving policy and customer fairness. |
| `retail-store-ops` | `/retail-store-ops` | Store Operations Playbook | Create store procedures with role ownership, safety checks, and escalation. |
| `retail-qa` | `/retail-qa` | Commerce Experience QA | Test product, cart, checkout, device, and accessibility journeys. |

### Business Communications (`business-communications`)

Executive writing, email, reports, policies, stakeholder updates, and crisis communications.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `comms-executive-brief` | `/comms-executive-brief` | Executive Brief | Create a concise decision brief with evidence, options, owner, and timing. |
| `comms-email` | `/comms-email` | Business Email | Draft audience-appropriate business email with a clear next action. |
| `comms-stakeholder-update` | `/comms-stakeholder-update` | Stakeholder Update | Report status, changes, blockers, decisions, and next steps. |
| `comms-policy` | `/comms-policy` | Internal Policy Draft | Draft policy with scope, rules, owner, exceptions, and review cadence. |
| `comms-report` | `/comms-report` | Business Report | Connect evidence to conclusions and actions in a structured report. |
| `comms-crisis` | `/comms-crisis` | Crisis Communications | Prepare a factual holding statement and update plan for an incident. |
| `comms-edit` | `/comms-edit` | Clarity and Tone Edit | Edit writing for clarity, audience fit, accuracy, and consistent tone. |
| `comms-meeting` | `/comms-meeting` | Meeting Brief and Minutes | Prepare agendas and decision-focused minutes with owners and follow-ups. |
| `comms-localization` | `/comms-localization` | Business Content Localization | Adapt content to a locale while preserving meaning, policy, and usability. |
| `comms-quality` | `/comms-quality` | Communications Quality Check | Quality-check business communications before distribution. |

### Supply Chain and Logistics (`supply-chain-logistics`)

Demand, sourcing, inventory, fulfillment, transport, resilience, and supplier performance.

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `supply-demand` | `/supply-demand` | Demand Planning | Build a demand view with documented inputs, scenarios, and error checks. |
| `supply-sourcing` | `/supply-sourcing` | Sourcing Strategy | Compare sourcing options for cost, quality, lead time, resilience, and compliance. |
| `supply-supplier` | `/supply-supplier` | Supplier Performance Review | Review supplier performance with agreed measures and corrective actions. |
| `supply-inventory` | `/supply-inventory` | Inventory Optimization | Identify inventory imbalances without hiding service risk. |
| `supply-warehouse` | `/supply-warehouse` | Warehouse Operations | Improve warehouse flow, safety, accuracy, and workload visibility. |
| `supply-transport` | `/supply-transport` | Transportation Planning | Plan shipments with constraints, service, cost, and exception handling visible. |
| `supply-resilience` | `/supply-resilience` | Supply Chain Risk Review | Assess disruption exposure, early signals, and mitigation options. |
| `supply-control-tower` | `/supply-control-tower` | Supply Chain Exception Review | Triage exceptions by impact, owner, and next update. |
| `supply-procurement` | `/supply-procurement` | Purchase Order Reconciliation | Reconcile orders, receipts, invoices, and supplier records with traceable exceptions. |
| `supply-sustainability` | `/supply-sustainability` | Supply Chain Sustainability Review | Review sustainability claims with boundaries, evidence, and data-quality limits. |

## Additional specialist skills

These complement the domain packs and are grouped by category.

### ai-engineering

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `llm-app` | `/llm-app` | LLM Application Engineering | Implement reliable LLM features with structured outputs, bounded tools, privacy, and graceful failure handling. |
| `llm-evaluation` | `/llm-evaluation` | Evaluate an LLM Workflow | Measure an LLM feature with representative cases, explicit rubrics, failure analysis, and repeatable comparisons. |
| `prompt-engineering` | `/prompt-engineering` | Prompt Engineering | Improve prompts against explicit tasks and evaluations while preserving tool and safety boundaries. |
| `rag` | `/rag` | Retrieval-Augmented Generation | Build a grounded retrieval workflow with traceable sources, chunking tests, and abstention on missing evidence. |

### analytics

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `product-analytics` | `/product-analytics` | Product Analytics | Define product metrics and event instrumentation that answer a decision without collecting unnecessary data. |

### automation

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `workflow-automation` | `/workflow-automation` | Workflow Automation | Automate a repetitive workflow with bounded inputs, safe retries, idempotency, and clear human checkpoints. |

### cloud

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `cloud-architecture` | `/cloud-architecture` | Cloud Architecture | Design a cloud deployment around explicit reliability, security, operations, and cost constraints. |
| `cost-optimization` | `/cost-optimization` | Cloud Cost Optimization | Find measurable cloud cost reductions while protecting reliability and workload correctness. |

### content

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `content-strategy` | `/content-strategy` | Content Strategy | Plan clear, consistent content around a specific audience, task, evidence, and publishing goal. |
| `documentation-translation` | `/documentation-translation` | Technical Localization | Adapt technical content across languages while preserving product meaning, UI limits, and verified terminology. |

### data

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `data-analysis` | `/data-analysis` | Data Analysis | Answer data questions with reproducible calculations, clear definitions, and honest uncertainty. |
| `data-pipelines` | `/data-pipelines` | Data Pipeline Engineering | Build reliable, observable data pipelines with explicit schemas, retries, and idempotency. |

### data-engineering

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `data-governance` | `/data-governance` | Data Governance | Define practical ownership, quality, access, lineage, and retention controls for a data asset. |
| `data-pipeline` | `/data-pipeline` | Data Pipeline Engineering | Build observable, restartable pipelines with explicit schemas, idempotency, and data-quality checks. |
| `database-design` | `/database-design` | Database Design | Design safe relational data models, queries, and migrations that preserve integrity and performance. |

### data-science

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `ab-testing` | `/ab-testing` | A/B Test Analysis | Analyze controlled experiments with valid assignment checks, predeclared metrics, and practical uncertainty. |
| `analyze` | `/analyze` | Analyze Data | Answer a data question with reproducible analysis, explicit assumptions, and evidence tied to the provided data. |
| `clean-data` | `/clean-data` | Clean a Dataset | Audit and clean a dataset with explicit, reversible rules for missing values, duplicates, types, and outliers. |
| `data-visualization` | `/data-visualization` | Data Visualization | Create clear charts that faithfully represent the underlying data and its uncertainty. |
| `geospatial-analysis` | `/geospatial-analysis` | Geospatial Analysis | Analyze spatial data with explicit coordinate systems, units, geometry validity, and privacy controls. |
| `sql-analysis` | `/sql-analysis` | SQL Analysis | Write correct, reviewable SQL for analytics while guarding against join fanout and misleading aggregates. |
| `statistics` | `/statistics` | Statistical Analysis | Choose and interpret statistical methods with assumptions, uncertainty, and practical effects stated clearly. |

### design

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `design-system` | `/design-system` | Design System Engineering | Extend a design system with accessible tokens and reusable components that fit existing conventions. |
| `ux-research` | `/ux-research` | UX Research | Plan and synthesize ethical user research that ties observations to product decisions. |

### developer-tools

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `cli-design` | `/cli-design` | CLI Engineering | Design command-line tools with predictable arguments, clear errors, safe defaults, and scriptable output. |
| `git-workflow` | `/git-workflow` | Git Workflow Support | Prepare safe, reviewable Git changes with clear scope, tests, and commit history. |

### devops

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `devops` | `/devops` | DevOps Engineering | Improve build and delivery workflows with reproducible steps, safe rollout, and actionable failure signals. |
| `docker` | `/docker` | Container Engineering | Build small, secure, reproducible containers with explicit runtime and health behavior. |
| `kubernetes` | `/kubernetes` | Kubernetes Engineering | Author Kubernetes resources with least privilege, clear health behavior, and safe rollout settings. |
| `observability` | `/observability` | Observability Engineering | Instrument services with useful metrics, logs, and traces while controlling noise and sensitive data. |

### documentation

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `documentation-api` | `/documentation-api` | API Documentation | Document API behavior from the implementation and contract, with examples users can reproduce. |
| `technical-writing` | `/technical-writing` | Technical Writing | Write accurate, task-oriented technical documentation with runnable examples and clear prerequisites. |

### education

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `education-content` | `/education-content` | Learning Content Design | Create learning materials with measurable outcomes, sequenced practice, accessible examples, and answer checks. |

### game-development

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `game-development` | `/game-development` | Game Development | Implement game features with deterministic state transitions, responsive input, and measurable performance. |

### general

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `architecture` | `/architecture` | Architecture Designer | Defines system boundaries, interfaces, and implementation constraints. |
| `documentation` | `/documentation` | Documentation Writer | Produces concise user and developer documentation that matches the implementation. |
| `implementation` | `/implementation` | Implementation Builder | Writes production-grade code with minimal duplication and explicit types. |
| `release` | `/release` | Release Manager | Coordinates versioning, packaging, and verification for shipping. |
| `requirements` | `/requirements` | Requirements Clarifier | Collects scope, constraints, acceptance criteria, and open questions before implementation starts. |
| `review` | `/review` | Code Reviewer | Finds defects, regressions, and missing coverage before release. |
| `security` | `/security` | Security Reviewer | Assesses secrets handling, unsafe file access, and privilege boundaries. |
| `testing` | `/testing` | Testing Specialist | Designs and validates tests for the changed slice. |

### machine-learning

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `computer-vision` | `/computer-vision` | Computer Vision | Build vision workflows with robust image handling, leakage-safe splits, and task-appropriate evaluation. |
| `data-preparation` | `/data-preparation` | ML Data Preparation | Prepare reproducible model datasets while preventing leakage and preserving provenance. |
| `deep-learning` | `/deep-learning` | Deep Learning Engineering | Develop deep learning code with explicit tensor shapes, stable optimization, and reproducible evaluation. |
| `evaluate` | `/evaluate` | Evaluate a Model | Evaluate model quality with leakage-safe splits, task-appropriate metrics, baselines, and error analysis. |
| `experiment-tracking` | `/experiment-tracking` | Reproducible ML Experiments | Make model experiments traceable across code, data, configuration, environment, and artifacts. |
| `feature-engineering` | `/feature-engineering` | Feature Engineering | Build features that are valid at prediction time and reproducible across training and inference. |
| `feature-engineering-practice` | `/feature-engineering-practice` | Feature Engineering Practice | Create leakage-safe, interpretable features that match the model's serving-time information. |
| `fine-tuning` | `/fine-tuning` | Model Fine-Tuning | Plan or implement a parameter-efficient or full fine-tuning workflow with controlled data and cost. |
| `hardware-ml` | `/hardware-ml` | Edge and Hardware-Constrained ML | Adapt inference to constrained hardware using measured latency, memory, and accuracy tradeoffs. |
| `improve` | `/improve` | Improve a Machine Learning Model | Find evidence-based model improvements through error analysis and controlled experiments against a fixed baseline. |
| `machine-learning` | `/machine-learning` | Machine Learning Workflow | Develop a scoped machine learning feature, from data inspection and baseline selection through evaluation. |
| `ml-experiment-tracking` | `/ml-experiment-tracking` | Machine Learning Experiment Tracking | Make model experiments comparable with consistent splits, metrics, configuration, and artifact provenance. |
| `mlops` | `/mlops` | MLOps and Model Release | Package, register, and monitor models with reproducible artifacts and explicit release gates. |
| `model-card` | `/model-card` | Model Documentation | Document a model's intended use, data provenance, evaluation, limitations, and deployment assumptions. |
| `model-evaluation` | `/model-evaluation` | Model Evaluation | Evaluate model quality with valid splits, suitable metrics, uncertainty, and error analysis. |
| `model-serving` | `/model-serving` | Model Serving and Inference APIs | Package model inference behind a reliable API with validation, resource limits, and observable behavior. |
| `model-training` | `/model-training` | Model Training | Set up or improve a reproducible model training run with clear configuration, checkpoints, and evaluation. |
| `nlp` | `/nlp` | Natural Language Processing | Build NLP pipelines that respect language, label quality, privacy, and task-specific evaluation. |
| `preprocess` | `/preprocess` | Preprocess Machine Learning Data | Design a repeatable preprocessing pipeline that preserves schema, prevents leakage, and records transformations. |
| `pytorch-training` | `/pytorch-training` | PyTorch Training | Implement PyTorch training loops with correct device, optimizer, checkpoint, and evaluation handling. |
| `tensorflow-training` | `/tensorflow-training` | TensorFlow and Keras Training | Build TensorFlow/Keras training workflows with explicit data, callbacks, and evaluation behavior. |
| `time-series` | `/time-series` | Time-Series Modeling | Analyze and forecast time-indexed data with temporal splits, leakage controls, and useful uncertainty. |
| `train` | `/train` | Train a Machine Learning Model | Build and run a reproducible model training workflow with a baseline, tracked configuration, and held-out evaluation. |

### mobile-development

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `mobile-app` | `/mobile-app` | Mobile App Engineering | Implement mobile features with reliable navigation, offline behavior, accessibility, and platform conventions. |

### operations

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `incident-response` | `/incident-response` | Incident Response | Triage incidents from evidence, reduce impact safely, and preserve a clear timeline and follow-up. |

### product

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `product-discovery` | `/product-discovery` | Product Discovery | Turn a product idea into a testable problem statement, user evidence plan, and scoped first release. |

### professional-services

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `finance-analysis` | `/finance-analysis` | Financial Analysis Support | Structure financial calculations and scenarios with transparent inputs, formulas, and sensitivity ranges. |
| `legal-document-review` | `/legal-document-review` | Legal Document Review Support | Summarize a legal document's structure and flag questions for qualified counsel without giving definitive legal advice. |

### python

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `python-debugging` | `/python-debugging` | Python Debugging | Find the root cause of Python failures using reproducible evidence and the narrowest fix. |
| `python-library` | `/python-library` | Python Library Engineering | Design maintainable Python packages with stable APIs, typing, packaging, and clear examples. |
| `python-migration` | `/python-migration` | Python Upgrade and Migration | Migrate Python code or dependencies in a controlled way with compatibility evidence and a rollback path. |
| `python-packaging` | `/python-packaging` | Python Packaging | Package a Python library with clear APIs, reproducible builds, supported versions, and clean installation behavior. |
| `python-performance` | `/python-performance` | Python Performance | Profile Python hotspots and improve measured runtime or memory without changing semantics. |

### quality-assurance

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `accessibility-audit` | `/accessibility-audit` | Accessibility Audit | Inspect a user flow for keyboard, screen reader, visual, and cognitive accessibility barriers. |
| `e2e-testing` | `/e2e-testing` | End-to-End Testing | Create stable end-to-end coverage for critical user journeys with reliable setup and useful diagnostics. |
| `performance-audit` | `/performance-audit` | Performance Audit | Find and verify the largest performance bottlenecks before changing code or infrastructure. |
| `requirements-to-tests` | `/requirements-to-tests` | Requirements to Acceptance Tests | Turn requirements into observable acceptance cases that cover success, failure, boundaries, and permissions. |
| `test-strategy` | `/test-strategy` | Test Strategy | Choose a balanced test plan that catches important failures at the lowest practical level. |

### release-engineering

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `release-readiness` | `/release-readiness` | Release Readiness Review | Check a release candidate against explicit acceptance, compatibility, security, rollback, and communication gates. |

### research

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `research-synthesis` | `/research-synthesis` | Research Synthesis | Synthesize supplied or sourced evidence with provenance, disagreement, and uncertainty kept visible. |

### security

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `privacy-review` | `/privacy-review` | Privacy Review | Reduce privacy risk by tracing personal data, purpose, access, retention, and user control. |
| `security-review` | `/security-review` | Security Review | Review a scoped change for exploitable weaknesses and give prioritized, verifiable fixes. |
| `web-application-security` | `/web-application-security` | Web Application Security | Review web changes for concrete access-control, injection, session, and data-exposure risks. |
| `web-security` | `/web-security` | Web Security Engineering | Review web features for input, session, authorization, and output-handling vulnerabilities. |

### testing

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `end-to-end-testing` | `/end-to-end-testing` | End-to-End Testing | Validate critical user journeys across the running application with stable, accessible assertions. |
| `integration-testing` | `/integration-testing` | Integration Testing | Verify interactions between real components while isolating external services and state. |
| `performance-testing` | `/performance-testing` | Performance and Load Testing | Design controlled load tests that measure latency, throughput, and saturation safely. |
| `test-automation` | `/test-automation` | Test Automation Engineering | Create maintainable CI test workflows with clear triggers, artifacts, and failure signals. |
| `unit-testing` | `/unit-testing` | Unit Testing | Write fast, deterministic unit tests around public behavior and edge cases. |
| `web-testing` | `/web-testing` | Web Application Testing | Select and implement browser-level tests for important user journeys and regressions. |

### web-design

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `ui-maximalism` | `/ui-maximalism` | Maximalist Interface Design | Create expressive, layered interfaces while preserving hierarchy, readability, and usable controls. |
| `ui-minimalism` | `/ui-minimalism` | Minimalist Interface Design | Create restrained interfaces with clear hierarchy, generous space, and only essential controls. |

### web-development

| Skill ID | Slash name | Skill | Use it for |
| --- | --- | --- | --- |
| `api-design` | `/api-design` | API Design | Design stable APIs with clear contracts, validation, compatibility, and error semantics. |
| `backend-api` | `/backend-api` | Backend API Engineering | Design and implement reliable backend endpoints, validation, and service boundaries. |
| `django-engineering` | `/django-engineering` | Django Engineering | Implement Django features with correct ORM, migrations, permissions, and request handling. |
| `fastapi-engineering` | `/fastapi-engineering` | FastAPI Engineering | Build typed FastAPI endpoints with explicit validation, dependency boundaries, and OpenAPI behavior. |
| `frontend-engineering` | `/frontend-engineering` | Frontend Engineering | Implement focused frontend features with strong state, component, and browser behavior. |
| `responsive-accessibility` | `/responsive-accessibility` | Responsive and Accessible Web UI | Build responsive interfaces that work with keyboard, screen readers, zoom, and touch. |
| `seo-audit` | `/seo-audit` | SEO Audit | Improve technical and content discoverability using crawlable structure and verifiable search metadata. |
| `web-development` | `/web-development` | Web Development | Plan and implement a focused web feature using the repository's existing framework, patterns, and tests. |
| `web-performance` | `/web-performance` | Web Performance Tuning | Find and fix measured frontend performance bottlenecks without degrading behavior. |

## Use and export

```bash
gncore search "clean data"
gncore show train
gncore export --skills train evaluate --output ml-skills.zip
gncore export --all --output all-gncore-skills.zip
```

Every skill guides an AI assistant through scoped, evidence-based work and asks it to report checks honestly. Skills are instructions, not executable agents; the host assistant supplies reasoning and tools.
