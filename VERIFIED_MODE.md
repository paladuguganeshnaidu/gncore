# Verification scope

GNCore reports concrete checks, not an unlimited guarantee of agent output quality.

The phase-two checks cover all active category definitions, unique workflow IDs/procedures, full phase-one migration accounting, exact preserved/rewritten procedure hashes, alias precedence, required resource paths/digests and entrypoint links. Python helper parsing is static; arbitrary imported executables are not run during installation or audit.

The neural-network probe checks all parameter gradients against finite differences, finite loss, parameter continuation and tiny synthetic XOR learning on CPU. It does not test a real dataset, GPU, PyTorch/TensorFlow, distributed training or deployment.

The 90 scenarios span all 30 categories. Corpus validation checks completeness and references. The response runner checks declared selection/decisions and actual file presence. Human/semantic artifact review and external browser/device/database/provider work remain separate; defining a scenario does not mean its entire agent task was executed.

Installer checks include collision preflight, modified-file preservation, stale resources, path boundaries, permissions, actual process interruption, rollback and safe retirement. Clean artifact checks compare package/source/installed/archive bytes and validate actual import/CLI behavior outside the checkout.

The static website is checked for metadata/catalog agreement, local links, redirects, search/filter/empty states and narrow/wide layouts. A local preview is not a verified Cloudflare deployment. GitHub/PyPI publication is held for the owner's requested approval.
