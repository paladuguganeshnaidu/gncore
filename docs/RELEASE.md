# Release workflow

See [the phase-two release plan](PHASE2_RELEASE.md) for the concrete candidate, destinations, artifacts and approval boundary.

Build and test the candidate locally, record artifact checksums, verify a clean wheel installation, inspect the generated website and review migration/ownership. Keep artifact generation separate from public publication. The owner explicitly requested an approval question after this preparation; do not push release source, create public release tags, upload to PyPI or deploy Cloudflare before that approval.

After approval, push the prepared source branch and require CI for the exact release commit. Create the version tag/release with the accepted artifacts. Publish the verified wheel/source bytes using the configured PyPI publisher, then verify public metadata/files. Deploy the synchronized website only after the package/GitHub state is verified. Retain the prior website commit and package version for rollback; uploaded PyPI files cannot be overwritten.
