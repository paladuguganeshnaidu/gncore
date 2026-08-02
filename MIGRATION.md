# Migration

GNCore 3.0 is a new product line. It no longer exposes the old workflow-engine stages or provider abstraction.

If you are upgrading from an earlier repository snapshot:

1. Remove any old `.gncore/` workflow state directories from your projects.
2. Install the new package with `pip install gncore`.
3. Run `gncore list apps` to inspect detected applications.
4. Run `gncore activate` to install the bundled skills into the selected applications.

The new repo stores its own installer manifest inside each target application's config directory, so old workflow artifacts are not reused.
