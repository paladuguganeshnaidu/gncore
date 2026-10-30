"""Generate the Cloudflare Pages preview from the same accepted package catalog."""

import argparse
from html import escape as h
import json
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from gncore import __version__, list_domains, get_skill
from gncore.routing import SIGNALS, route_task
from gncore.skills.library import migration_manifest
from gncore.skills.unified import unified_manifest
from benchmark_pages import benchmark_home, benchmark_page, publish_assets

HOST = "https://gncore.pages.dev"


def command(text):
    return f'<div class="command-block"><pre><code>{h(text)}</code></pre><button class="copy-command" data-copy="{h(text, quote=True)}" type="button">Copy command</button></div>'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "website")
    parser.add_argument("--published", action="store_true", help="Use only after approved release artifacts are publicly verified")
    args = parser.parse_args()
    output = args.output.resolve()
    if not output.is_relative_to(ROOT.resolve()):
        raise ValueError("website output must stay within this workspace")
    entries, domains = unified_manifest(), list_domains()
    by_id = {e["id"]: e for e in entries}
    group_for = {name: domain for domain in domains for name in domain.skill_ids}
    total = sum(len(e["workflows"]) for e in entries)
    route_result = route_task("Check neural network gradients")
    route_example = json.dumps({key: route_result[key] for key in ("skill_id", "status", "workflows")}, indent=2)
    pages = {}
    links = [('/skills/', 'Skills'), ('/domains/', 'Developer domains'), ('/docs/', 'Docs'), ('/benchmarks/', 'Benchmarks'), ('/migration/', 'Migration'), ('/creator/', 'Creator')]
    nav = ''.join(f'<a href="{url}">{label}</a>' for url, label in links)
    mark = '<img src="/assets/favicon.svg" width="36" height="36" alt="">'
    banner = '' if args.published else '<div class="preview-banner">PHASE TWO PREVIEW · Release candidate prepared locally · Publication pending approval</div>'
    header = f'{banner}<a href="#main" class="skip-link">Skip to content</a><header class="site-header"><div class="nav-shell"><a class="brand" href="/">{mark}<span>GN<span class="brand-accent">Core</span></span><sup>{h(__version__)}</sup></a><nav class="nav-links" aria-label="Main navigation">{nav}</nav><a class="nav-cta" href="/download/">Get started ↗</a><button class="menu-button" id="menu-toggle" aria-label="Open navigation" aria-expanded="false" aria-controls="mobile-menu"><span></span><span></span><span></span></button></div><div id="mobile-menu" class="mobile-menu" hidden>{nav}<a href="/download/">Get started</a></div></header>'
    footer = f'<footer class="footer"><div class="footer-top"><div><a class="brand" href="/">{mark}GNCore</a><p>Developer skills. Concrete checks.<br>Powered by your assistant.</p><a href="/creator/">Created by Paladugu Ganesh Naidu ↗</a></div><div><span class="footer-label">Explore</span>{nav}<a href="/all-skills/">All workflows</a></div><div><span class="footer-label">Resources</span><a href="/download/">Install and verify</a><a href="/use-cases/">Developer use cases</a><a href="/assistants/">Using exported skills</a><a href="https://github.com/paladuguganeshnaidu/gncore">GitHub project ↗</a><a href="https://pypi.org/project/gncore/">PyPI project ↗</a></div></div><div class="footer-bottom"><span>© 2026 GNCore · {h(__version__)}</span><span>{len(entries)} categories · {total} workflows · source-specific licenses retained</span><a href="#top">Back to top ↑</a></div></footer>'

    def page(path, title, description, body):
        canonical = HOST + path
        robots = 'index,follow' if args.published else 'noindex,follow'
        head = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#101226"><meta name="color-scheme" content="light"><meta name="google-site-verification" content="PGoKYGWP0GCamPo1DomvnLgz8CsFOt7qEPCDO7UR-lc"><title>{h(title)} — GNCore</title><meta name="description" content="{h(description, quote=True)}"><meta name="robots" content="{robots}"><link rel="canonical" href="{canonical}"><meta property="og:title" content="{h(title, quote=True)} — GNCore"><meta property="og:description" content="{h(description, quote=True)}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="{HOST}/assets/social.png"><link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/site.css"><link rel="stylesheet" href="/assets/phase2.css"><link rel="stylesheet" href="/assets/benchmarks.css"><script src="/assets/benchmarks.js" defer></script><script src="/assets/site.js" defer></script><script src="/assets/explorer.js" defer></script></head>'
        pages[path] = head + f'<body id="top">{header}<main id="main">{body}</main>{footer}</body></html>\n'

    def intro(kicker, title, text):
        return f'<section class="container page-intro"><span class="eyebrow">{h(kicker)}</span><h1>{h(title)}</h1><p>{h(text)}</p></section>'

    def card(entry, searchable=False):
        name, domain = entry['id'], group_for[entry['id']]
        keywords = ' '.join([name, entry['description'], *SIGNALS[name], *(w['id']+' '+w['title']+' '+w['description'] for w in entry['workflows'])])
        attrs = f' data-category="{name}" data-group="{domain.domain_id}" data-search="{h(keywords, quote=True)}"' if searchable else ''
        return f'<a class="category-card" href="/skills/{name}/"{attrs}><span class="card-id">${name}</span><h3>{h(entry["title"].removeprefix("GNCore "))}</h3><p>{h(entry["description"])}</p><span class="card-meta">{len(entry["workflows"])} workflows · {h(domain.name)} ↗</span></a>'

    hero = f'<section class="container hero"><div class="hero-grid"><div class="hero-copy"><span class="eyebrow"><span class="eyebrow-dot"></span>THE DEVELOPER SKILL LAYER</span><h1>Build smarter.<br><em>Ship with evidence.</em></h1><p class="hero-sub">One adaptive skill for the task. Focused playbooks for software, neural networks, model operations and systems—selected by your assistant, checked against real work.</p><div class="hero-actions"><a class="btn btn-dark" href="/skills/">Explore {len(entries)} skills ↗</a><a class="btn btn-outline" href="/download/">Install and verify →</a></div><div class="hero-micro">{h(__version__)} · Developer-focused phase two</div></div><div class="hero-art phase2-art"><div class="terminal"><div class="terminal-top">LOCAL ROUTING · JSON EXCERPT <span>↗</span></div><pre>$ gncore route "Check neural network gradients"\n\n{h(route_example)}\n\n$ gncore export --specific neural-networks\n$ gncore verify</pre><div class="terminal-bottom">No model account required to browse or export.<br>Your host agent supplies the model and tools.</div></div></div></div><div class="stats-row"><div><strong>{len(entries)}</strong><span>developer categories</span></div><div><strong>{total}</strong><span>focused workflows</span></div><div><strong>90</strong><span>evaluation scenarios</span></div><div><strong>6</strong><span>capability groups</span></div></div></section>'
    featured = ['neural-networks', 'web-frontend', 'web-backend', 'systems-programming', 'mlops', 'embedded-systems']
    body = hero + benchmark_home() + '<section class="container"><div class="section-heading"><h2>From idea to <em>working code.</em></h2><a class="text-link" href="/skills/">All developer skills ↗</a></div><div class="category-grid">' + ''.join(card(by_id[name]) for name in featured) + '</div></section>'
    body += '<section class="container article-body"><h2>Short brief. Focused execution.</h2><p>Invoke one category, describe your goal and constraints, and the compatible host agent chooses relevant workflows. Existing stacks and brands stay part of the brief; an explicit choice takes priority.</p>' + command('$web-frontend Build a clinic booking page, no animation.\n$neural-networks Check gradient flow before scaling training.\n$web-backend Add an idempotent tenant-scoped endpoint.') + '<h2>Know what was checked.</h2><p>Merge accounting, resource hashes, links and helper syntax can be checked locally. The evaluation corpus separates structural checks from human review and unexecuted browser, device or model-provider checks. A passing file check is not a guarantee of AI output quality.</p><div class="notice">Original GNCore guidance is MIT-licensed. Bundled reference guides and tools retain their original authorship, notices and applicable licenses.</div></section>'
    page('/', 'Developer skills for software and neural networks', '30 developer skills covering software, machine learning, neural networks, systems and reliable delivery.', body)
    options = '<option value="all">All developer domains</option>' + ''.join(f'<option value="{d.domain_id}">{h(d.name)}</option>' for d in domains)
    controls = f'<div class="catalog-controls"><label for="skill-search">Search skills and workflows<input id="skill-search" type="search" placeholder="Try neural networks, Postgres, Rust…" autocomplete="off"></label><label for="group-select">Developer domain<select id="group-select">{options}</select></label><button class="btn btn-outline" id="reset-filters" type="button">Reset filters</button></div><p id="result-count" role="status" aria-live="polite">{len(entries)} categories</p><p id="empty-state" class="notice" hidden>No matching skills. Try a broader term or reset the filters.</p>'
    page('/skills/', 'Explore developer skills', 'Search developer categories and all merged workflow names.', intro('THE CATALOG', 'Choose the work. Keep the context.', 'Search by task, framework or capability. Each category contains focused procedures and checks; install only what your project needs.') + '<section class="container">' + controls + '<div class="category-grid">' + ''.join(card(e, True) for e in entries) + '</div></section>')
    for entry in entries:
        workflow_body = ''.join(f'<section class="workflow-detail" id="{w["id"]}"><h3>{h(w["title"])}</h3><p><code>{h(w["id"])}</code></p><p>{h(w["procedure"])}</p></section>' for w in entry['workflows'])
        body = intro(group_for[entry['id']].name, entry['title'].removeprefix('GNCore '), entry['description']) + '<article class="container article-body">' + command('gncore export --specific '+entry['id']+'\n'+'$'+entry['id']+' Describe your task, existing project and constraints.') + f'<p>{len(entry["workflows"])} focused workflows · Version {h(__version__)} · {h(entry["license"])}</p><p>Use relevant workflows within this category; the list is not a requirement to run every mode. Supporting references are included in complete exports.</p>' + workflow_body + '</article>'
        page('/skills/'+entry['id']+'/', entry['title'], entry['description'], body)
    domain_body = intro('SIX CAPABILITY GROUPS', 'Built around developer work.', 'Business and professional-service packs are retired from phase two. Overlapping technical categories are consolidated, with explicit migration mappings.')
    for domain in domains:
        domain_body += f'<section class="container"><div class="section-heading"><h2 id="{domain.domain_id}">{h(domain.name)}</h2><span>{len(domain.skill_ids)} categories</span></div><div class="category-grid">' + ''.join(card(by_id[name]) for name in domain.skill_ids) + '</div></section>'
    page('/domains/', 'Developer domains', 'Six capability groups spanning the full developer catalog.', domain_body)
    table = ''.join(f'<tr><td><code>{h(w["id"])}</code></td><td><a href="/skills/{e["id"]}/#{w["id"]}">{h(w["title"])}</a></td><td>{h(e["id"])}</td></tr>' for e in entries for w in e['workflows'])
    page('/all-skills/', 'All merged workflows', 'The complete developer workflow index and category destinations.', intro('COMPLETE INDEX', f'{total} focused workflows.', 'Workflow IDs resolve to their category. Exporting several workflows in one category creates one complete skill folder.') + '<section class="container article-body"><div class="table-scroll"><table class="data-table"><thead><tr><th>Workflow ID</th><th>Workflow</th><th>Category</th></tr></thead><tbody>'+table+'</tbody></table></div></section>')
    install = command('python -m pip install gncore=='+__version__+'\ngncore version\ngncore export --specific neural-networks\ngncore verify')
    note = 'The candidate commands below become available after approved publication. The currently public PyPI package is a separate release.' if not args.published else 'Install the verified release. Review the migration notes before replacing an older catalog.'
    page('/download/', 'Install, inspect and verify', 'Install GNCore and export portable developer skills.', intro('GET STARTED', 'Install only what you need.', note) + '<article class="container article-body">' + install + '<h2>Preview a full migration</h2>' + command('gncore export --all --prune-retired --dry-run\ngncore export --all --prune-retired\ngncore verify\ngncore audit') + '<p>Pruning retires only unchanged inventory-managed old categories and retains a full backup. Custom edits and untracked folders are preserved; conflicts stop the update.</p><h2>Portable archive</h2>' + command('gncore export --all --output gncore-developer-skills.zip') + '<p>The host agent must support and enable the standard skill format. Exporting does not install a model, frameworks, browser tools or credentials.</p></article>')
    page('/docs/', 'Commands and verification', 'Search, route, inspect, export and evaluate developer skills.', intro('DOCUMENTATION', 'A small CLI. Concrete evidence.', 'Browse locally, ask for an explainable routing hint, and verify the exact files that get installed.') + '<article class="container article-body">' + command('gncore list skills\ngncore list domains\ngncore list workflows\ngncore search "neural network"\ngncore route "Check neural network gradients"\ngncore show neural-networks\ngncore evaluate --validate\ngncore audit') + '<h2>Evaluation scope</h2><p>The corpus has a normal, underspecified and boundary scenario for each of the 30 categories. The offline runner checks recorded selection, constraints and artifact presence. Human review and external execution remain separate and cannot be certified by a structural pass.</p><h2>Project context</h2><p>The optional route context file permits stack, brand, audience and preferred_skills. It is an explicit small JSON brief; GNCore does not scan secrets or unrelated project files.</p>'+command('gncore route "Build a website" --context ./project-brief.json')+'</article>')
    ledger = migration_manifest()
    rows = ''.join(f'<tr><td><code>{h(item["id"])}</code></td><td>{h(item["target"] or "Retired: outside developer scope")}</td></tr>' for item in ledger['categories'])
    page('/migration/', 'Phase-two migration', 'Understand retired professional packs, technical consolidation and safe installation.', intro('MAJOR CATALOG CHANGE', 'Fewer categories. Deeper developer work.', 'Phase two replaces 60 mixed categories with 30 developer categories. All 553 earlier workflow IDs have a recorded retained, rewritten or retired outcome.') + '<article class="container article-body"><p>319 technical workflows remain, including 116 task-specific rewrites; 55 original workflows are added. The 234 retired workflows belong outside the focused developer scope. Historical content remains in Git history; it is not silently assigned to an unrelated skill.</p><div class="notice">Do not treat a retired workflow as an alias for a different capability. Inspect the mapping and preserve customized old folders before changing your installation.</div><div class="table-scroll"><table class="data-table"><thead><tr><th>Previous category</th><th>Destination</th></tr></thead><tbody>'+rows+'</tbody></table></div></article>')
    page('/assistants/', 'Use exported skills', 'Load portable skill folders in a compatible host agent.', intro('THE HOST DOES THE WORK', 'One category. Your project context.', 'Export a category to .agents/skills, then ask a compatible agent to use it. Automatic discovery and invocation syntax depend on that host’s settings.') + '<article class="container article-body">'+command('gncore export --specific web-frontend\n$web-frontend Build a booking site using the existing stack.')+'<p>Entry instructions select relevant modes. Substantial references are conditional. Imported tools remain inert until deliberately used, and host permissions continue to govern external actions.</p></article>')
    page('/use-cases/', 'Developer use cases', 'Practical entrypoints for web, ML, systems and delivery work.', intro('PRACTICAL STARTING POINTS', 'Choose a concrete outcome.', 'Keep the existing stack, define the critical constraint, and ask for verifiable output.') + '<article class="container article-body">'+command('$neural-networks Diagnose stalled learning on a tiny batch.\n$deep-learning Verify checkpoint resume before scaling.\n$web-backend Add a tenant-scoped idempotent endpoint.\n$embedded-systems Test timer wraparound with host fixtures.\n$release-engineering Prepare artifacts, then wait for publication approval.')+'</article>')
    page('/creator/', 'Creator', 'GNCore is created by Paladugu Ganesh Naidu.', intro('THE CREATOR', 'Made by a builder. For builders.', 'GNCore is created by Paladugu Ganesh Naidu. This phase focuses the library on practical developer work, traceable source obligations and observable verification.') + '<article class="container article-body"><p><a href="https://github.com/paladuguganeshnaidu">GitHub profile ↗</a></p><p>Original GNCore guidance and code are MIT-licensed. Retained third-party materials keep their source-specific terms. Contributors should preserve provenance and improve demonstrated behavior rather than inflate line counts.</p></article>')
    publish_assets(output)
    reference_snapshot=ROOT/'web-results/comparison/source-snapshots.json'
    if reference_snapshot.exists():
        shutil.copyfile(reference_snapshot,output/'assets/benchmarks/source-snapshots.json')
    elif (ROOT/'web/benchmarks/source-snapshots.json').exists():
        shutil.copyfile(ROOT/'web/benchmarks/source-snapshots.json',output/'assets/benchmarks/source-snapshots.json')
    page('/benchmarks/', 'Benchmarks and open measurements', 'Original GNCore benchmark data, historical IDE pilots, generated-code checks and transparent methodology.', benchmark_page())
    for path, content in pages.items():
        target = output / path.strip('/') / 'index.html'
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding='utf-8', newline='\n')
    (output / 'assets').mkdir(parents=True, exist_ok=True)
    for asset in (ROOT / 'web/assets').iterdir():
        shutil.copyfile(asset, output / 'assets' / asset.name)
    data = {'version': __version__, 'status': 'published' if args.published else 'candidate-preview', 'categories': len(entries), 'workflows': total,
            'skills': [{'id':e['id'], 'name':e['title'], 'description':e['description'], 'group':group_for[e['id']].domain_id, 'workflows':[{'id':w['id'],'name':w['title'],'description':w['description']} for w in e['workflows']]} for e in entries],
            'groups':[{'id':d.domain_id,'name':d.name,'skills':list(d.skill_ids)} for d in domains]}
    (output / 'assets/catalog.json').write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    redirects = {f"/skills/{w['id']}/": '/skills/'+w['target']+'/' if w['target'] else '/migration/' for w in ledger['workflows'] if w['id'] not in by_id}
    redirects.update({f"/collections/{item['id']}/": '/skills/'+item['target']+'/' if item['target'] else '/migration/' for item in ledger['categories']})
    redirects.update({f"/skills/{item['id']}/": '/skills/'+item['target']+'/' if item['target'] else '/migration/' for item in ledger['categories'] if item['id'] not in by_id})
    redirects.update({f"/skills/{name}/": '/skills/'+target+'/' for name,target in ledger.get('aliases', {}).items() if name not in by_id})
    redirects['/collections/web-design/'] = '/skills/web-frontend/'
    historical = json.loads((ROOT / 'catalog/legacy_site_paths.json').read_text(encoding='utf-8'))
    for path in historical['paths']:
        if path in pages or path in redirects:
            continue
        prefix, *rest = path.strip('/').split('/')
        if prefix in {'skills', 'collections'} and rest:
            try:
                redirects[path] = '/skills/'+get_skill(rest[0]).metadata.skill_id+'/'
            except KeyError:
                redirects[path] = '/migration/'
        else:
            redirects[path] = '/'+prefix+'/' if '/'+prefix+'/' in pages else '/migration/'
    (output / '_redirects').write_text(''.join(f'{source} {target} 301\n' for source,target in sorted(redirects.items())), encoding='utf-8')
    (output / '_headers').write_text("/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: DENY\n  Permissions-Policy: camera=(), microphone=(), geolocation=()\n  Content-Security-Policy: default-src 'self'; img-src 'self' data:; style-src 'self'; script-src 'self'; object-src 'none'; base-uri 'self'; frame-ancestors 'none'; upgrade-insecure-requests\n/assets/*\n  Cache-Control: public, max-age=3600\n", encoding='utf-8')
    (output / 'robots.txt').write_text('User-agent: *\n'+('Allow: /\n' if args.published else 'Disallow: /\n')+f'Sitemap: {HOST}/sitemap.xml\n', encoding='utf-8')
    (output / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{HOST}{path}</loc></url>' for path in sorted(pages))+'</urlset>\n', encoding='utf-8')
    (output / 'llms.txt').write_text(f'# GNCore {__version__}\n\nDeveloper-focused skill catalog: {len(entries)} categories, {total} workflows.\nStatus: {data["status"]}.\nSkills guide host agents; they do not independently execute projects or certify output quality.\n\n- Catalog: {HOST}/skills/\n- Workflow index: {HOST}/all-skills/\n- Migration: {HOST}/migration/\n- Install: {HOST}/download/\n- Source-specific attribution and licenses remain applicable.\n', encoding='utf-8')
    (output / '404.html').write_text(pages['/migration/'].replace('Phase-two migration — GNCore', 'Page not found — GNCore').replace('Fewer categories. Deeper developer work.', 'This page has moved or is unavailable.').replace(HOST+'/migration/', HOST+'/404.html').replace('name="robots" content="index,follow"', 'name="robots" content="noindex,follow"'), encoding='utf-8')
    print(json.dumps({'output':str(output),'pages':len(pages),'categories':len(entries),'workflows':total,'status':data['status']}))


if __name__ == '__main__':
    main()
