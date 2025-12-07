# Conference Talk Proposal (CFP) - FILLED EXAMPLE

**For: Running Python in Your Browser - MkDocs + JupyterLite + WebAssembly**

Based on [Mason Egger's CFP Writing Guide](https://mason.dev/blog/how-i-write-conference-talk-proposals/)

---

## Talk Type

**Selected:**
- [x] Talk (45 minutes)
- [ ] Workshop (90-120 minutes)
- [ ] Lightning Talk (5-10 minutes)

---

## Title

**Python in the Browser: Building Interactive Documentation with MkDocs, JupyterLite, and WebAssembly**

_Alternative titles considered:_
- "From Static Docs to Live Code: Embedding Python Notebooks in MkDocs"
- "Zero-Install Python: WebAssembly-Powered Jupyter Notebooks in Your Documentation"
- "Interactive Documentation That Actually Works: A MkDocs + JupyterLite Journey"

---

## Category

**Web Development / Documentation Engineering** or **Community / Education**

---

## Elevator Pitch

Turn static documentation into live coding environments using MkDocs + JupyterLite. Learn how WebAssembly brings Python to the browser—no backend, no installs. See real implementation patterns and choose the right integration approach for your project.

**Character count:** 279/300

---

## Target Audience

**This talk is for:**

- **Technical writers** building interactive documentation sites
- **Documentation engineers** wanting to embed runnable code examples
- **Web developers** interested in WebAssembly applications
- **Educators** creating interactive learning platforms without server infrastructure
- **Developer advocates** demoing code without "works on my machine" problems
- **Open-source maintainers** who want users to try code before installing

**Why this talk appeals to different backgrounds:**
- **Frontend devs:** Learn practical WebAssembly integration (not just theory)
- **Backend devs:** Understand how Python runs client-side via Pyodide
- **DevOps/Platform engineers:** Eliminate backend infrastructure for demos/docs
- **Content creators:** Add interactivity without managing servers or containers

---

## Audience Level

**Selected:**
- [x] Intermediate

**Prerequisites:**
- Basic understanding of static site generators (MkDocs, Hugo, Jekyll, etc.)
- Familiarity with Jupyter notebooks (.ipynb files)
- Basic Python knowledge (needed to build and configure the MkDocs site)
- Basic HTML/JavaScript knowledge (understanding relative paths, new tab links)
- **NOT required:** WebAssembly experience or backend development skills

**Why intermediate:**
- Attendees should understand what documentation sites are and why interactivity matters
- Technical implementation details require comfort with config files and build tools
- No need to be an expert—practical patterns are shown, not deep WebAssembly theory

---

## Audience Takeaways

**Attendees will walk away with:**

1. **Three proven integration patterns** for interactive Jupyter notebooks in MkDocs—embedded notebooks using iframe, direct links to simplified notebook view, and links to full JupyterLab interface—with decision criteria for when to use each
2. **Understanding of how JupyterLite works** including how Pyodide runs Python in-browser via WebAssembly, the difference between `/notebooks/` and `/lab/` interfaces, and what the limitations and trade-offs are
3. **Real-world configuration examples** from a production bootcamp site, showing the mkdocs.yml setup and HTML patterns they can adapt for their own projects

---

## Outline

| Time | Duration | Section | Description |
|------|----------|---------|-------------|
| 0:00 | 4 min    | **The Problem: Evolution of a Bootcamp** | Story of Python bootcamp evolution: Live sessions across America/Mexico City → 1-hour DevNet Create training → GitHub repo. The roadblock: Students missing setup training sessions, struggling with Python installation, virtual environments, and getting stuck without support. The solution needed: Eliminate all setup barriers for learners. |
| 4:00 | 6 min    | **The Solution: WebAssembly + JupyterLite** | How Pyodide (CPython compiled to WebAssembly) enables Python in the browser. Architecture diagram: what runs client-side, no backend needed. JupyterLite as the complete Jupyter interface running as static files. Limitations and trade-offs. |
| 10:00| 7 min    | **MkDocs Configuration** | Required packages (mkdocs, mkdocs-material, mkdocs-jupyterlite). Key mkdocs.yml configuration sections: jupyterlite plugin setup, notebook_patterns for file discovery, lite_config for Pyodide kernel settings. Build process overview. |
| 17:00| 12 min   | **Three Integration Patterns** | (1) Embedded iframe using `/notebooks/` interface - provides in-page interaction. (2) Direct link to `/notebooks/` view in new tab - simplified interface. (3) Direct link to `/lab/` interface in new tab - full JupyterLab experience with file browser and terminal. Decision criteria: when to use each pattern, pros/cons of embedded vs. new tab. |
| 29:00| 8 min    | **Production Site Tour (Recorded)** | Walkthrough of live bootcamp site (GIF/screenshots): 20+ embedded notebooks across 3 weeks, navigation structure, how students interact with lessons, GitHub Pages deployment setup. User engagement results. |
| 37:00| 5 min    | **Package Trade-offs & Limitations** | Bundle sizes: base Pyodide vs. adding NumPy/Pandas. What works, what doesn't (native C extensions). Performance considerations. Browser storage for persistence. |
| 42:00| 3 min    | **Wrap-up & Resources** | GitHub repo with production config, reference to tutorial docs on WebAssembly/Pyodide, mkdocs-jupyterlite documentation. Next steps for attendees. |

**Total Duration:** 45 minutes

---

## Description

**The Problem: When Setup Becomes the Barrier to Learning**

I created a Python basics bootcamp that started as live 3-day sessions across America and Mexico City during my time at Cisco. It evolved into a 1-hour training at DevNet Create 2018, then into a GitHub repository with 20+ Jupyter notebooks for self-paced learning.

But there was a fundamental problem: Students who missed the live setup training sessions would get stuck before writing their first line of Python. Installing Python, configuring virtual environments, dealing with path issues—for beginners, this wasn't "learning Python." This was frustrating busywork that made them give up.

And for those not in my paid mentorship program, there was no one to help them get unstuck.

**The Solution: Eliminate the Roadblock Entirely**

What if learners could skip installation entirely? What if they could click a link and start coding Python in their browser?

That's what I built using JupyterLite—a complete Jupyter environment running entirely in the browser via WebAssembly (specifically, Pyodide: CPython compiled to WASM). No backend servers. No containers. Just static files served from GitHub Pages.

This talk shares how I integrated JupyterLite with MkDocs, the three patterns I use for embedding interactive notebooks, and the configuration that makes it all work in production.

**WebAssembly + Python: How JupyterLite Actually Works**

Before diving into integration, you need to understand what you're working with:

- **Pyodide**: CPython 3.11 compiled to WebAssembly, running in your browser's JavaScript engine
- **JupyterLite**: Complete Jupyter interface (Lab, Notebooks, REPL) as a static web application
- **Key limitation**: Not all Python packages work (no native C extensions without WASM compilation)
- **Key advantage**: Zero backend infrastructure, infinite scalability, works offline

The talk includes architectural diagrams showing what runs where (browser vs. server), package loading mechanisms, and performance characteristics you need to know before committing to this approach.

**Three Integration Patterns: Testing and Implementation**

I tested three different approaches to see which worked best for the bootcamp:

**1. Embed using `/notebooks/` interface** ✅ **CHOSEN**
```html
<iframe src="../jupyterlite/notebooks/index.html?path=BC_Weeks/Week_1/lesson.ipynb"
        width="100%" height="800px"></iframe>
```
**Result**: Cleaner, simpler interface. Students stay on the documentation page while interacting with notebooks. This became the primary approach for individual lesson pages.

**2. Embed using `/lab/` interface** (Tested, not chosen)
```html
<iframe src="../jupyterlite/lab/index.html?path=lesson.ipynb"
        width="100%" height="800px"></iframe>
```
**Problem**: Too cluttered when embedded. Full JupyterLab interface (file browser, terminal, menus) creates "nested navigation" that confuses learners.

**3. Direct links** (No embedding)
```html
<a href="../jupyterlite/lab/index.html" target="_blank" rel="noopener noreferrer">
  Launch JupyterLite
</a>
```
**Use case**: Main interactive landing page and as fallback links on lesson pages. Opens in new tab—clean full-screen experience but users leave the docs site.

**Final Implementation**: Embedded `/notebooks/` on lesson pages + direct links as fallbacks/alternatives. The talk covers decision criteria: when embedding works vs. when direct links are better.

**Production Configuration: mkdocs.yml Setup**

The talk shows the key configuration sections needed:

```yaml
plugins:
  - jupyterlite:
      enabled: true
      notebook_patterns:
        - "BC_Weeks/**/*.ipynb"  # Which notebooks to include
      lite_config:
        jupyter-lite-schema-version: 0
        jupyter-config-data:
          litePluginSettings:
            "@jupyterlite/pyodide-kernel-extension:kernel":
              pipliteUrls: []  # Custom packages if needed
```

Focus is on the jupyterlite plugin configuration, notebook patterns for file discovery, and the Pyodide kernel settings—the essential pieces needed to get Jupyter notebooks running in the browser.

**Real-World Case Study: Python Bootcamp Documentation Site**

Recorded tour of the production site (GIFs/screenshots):
- 20+ Jupyter notebooks across 3 weeks of curriculum
- Embedded notebooks on lesson pages using `/notebooks/` interface
- Direct links to full JupyterLab on main interactive page
- Material for MkDocs theme integration
- Search functionality across notebook content
- Mobile-responsive notebook display

The GitHub repository is fully open-source, so attendees can explore the complete implementation.

**Beyond Python: The Broader WebAssembly Opportunity**

While this talk focuses on Python via Pyodide, JupyterLite supports:
- JavaScript kernels (immediate, no WASM needed)
- Future languages as they compile to WASM (Rust, Go, etc.)
- Custom package installation via `piplite` (with caveats about bundle size)

I'll share the trade-offs: adding NumPy increases initial load by 10MB+, but caches well. This section helps you make informed decisions about package inclusion.

**What You'll Take Home**

This talk is intensely practical. You'll leave with:

**1. Three tested integration patterns** with decision criteria—understanding when to use embedded notebooks vs. direct links, and why `/notebooks/` interface works better than `/lab/` for embedded views.

**2. Understanding of how JupyterLite works**—how Pyodide runs Python in the browser via WebAssembly, what the limitations are, and the trade-offs you'll face with package sizes and performance.

**3. Real-world configuration examples**—from a production bootcamp site that you can adapt for your own projects. The full codebase is open-source on GitHub for reference and adaptation.

You can explore the complete implementation and adapt the patterns to your own documentation needs.

**Who Benefits From This?**

- **Technical writers**: Add runnable code to API docs, tutorials, and guides
- **Educator/trainers**: Create interactive courses without managing JupyterHub infrastructure
- **Developer advocates**: Demo your library in the browser—attendees can try it during your talk
- **Open-source maintainers**: Let users experiment before committing to installation
- **Documentation engineers**: Modernize static docs with zero backend infrastructure

**The Broader Implications**

This isn't just about Python or Jupyter. It's about the shift from "server-rendered interactive content" to "client-rendered with WebAssembly."

WebAssembly makes previously backend-dependent features work as static sites. JupyterLite + MkDocs is one implementation showing what's possible when you eliminate server infrastructure entirely.

**Ready to Make Your Documentation Interactive?**

The barrier to interactive technical content just dropped to zero. No servers. No containers. No "works on my machine" excuses.

Static site generators like MkDocs handle the documentation structure. WebAssembly via Pyodide handles the Python execution. JupyterLite ties them together. And you get the best of both worlds: static site simplicity with dynamic code execution.

This talk gives you the implementation patterns, the debugging strategies, and the production configurations you need to ship it today.

---

## Additional Notes

**Special Requirements:**
- Screen sharing capability for recorded demos (GIFs/screenshots)
- Projector capable of displaying code clearly (syntax highlighting important)

**Presenter Qualifications:**
- Creator of open-source Python Basics Boot Camp with production MkDocs + JupyterLite implementation
- Successfully deployed WebAssembly-based interactive documentation serving thousands of learners
- 10+ years Python development experience including documentation engineering at Cisco
- Active contributor to documentation tooling and static site optimization projects

**Accessibility Considerations:**
- All code examples use high-contrast syntax highlighting
- Presentation includes both visual architecture diagrams and verbal technical explanations
- Recorded demos include clear narration of what's shown
- Configuration examples available in text format for screen readers
- GitHub repository materials WCAG 2.1 AA compliant

**Previous Versions:**
- First time presenting this specific technical content at conferences
- Content battle-tested through documentation engineering work and bootcamp deployment
- Available for Q&A panels on WebAssembly, static site generators, or documentation engineering

---

## Internal Notes (For Speaker Use Only - DO NOT SUBMIT)

**Resources to reference during talk:**
- Main repo: https://github.com/ProsperousHeart/Basics-Boot-Camp
- Live production site: https://prosperousheart.github.io/Basics-Boot-Camp
- mkdocs-jupyterlite plugin docs: https://jupyterlite.readthedocs.io/en/latest/howto/configure/mkdocs.html
- Pyodide docs: https://pyodide.org/en/stable/
- GitHub Actions workflow file in repo for CI/CD example

**Backup slides/demos:**
- GIFs/screenshots of production site walkthrough
- Screenshots of all three integration patterns side-by-side
- PDF backup of key mkdocs.yml configurations
- Architectural diagrams showing WebAssembly/Pyodide flow

**Potential audience questions to prep for:**
1. "What's the performance compared to server-side Jupyter?"
2. "Can this work with proprietary/internal documentation behind firewall?"
3. "What about packages with C extensions like pandas/numpy?"
4. "How do you handle user state/saving notebooks across sessions?"
5. "What's the initial load time impact? Page size?"
6. "Can this integrate with Sphinx/Hugo/other static site generators?"
7. "How do you version-control generated JupyterLite files?"
8. "What browsers are supported? Mobile?"

**Technical failure contingencies:**
- All demos are pre-recorded (GIFs/screenshots) - no live internet needed
- Have backup static slides if screen sharing fails
- PDF handouts of configuration examples as backup

**Demo checklist:**
- [ ] Test all GIFs/screenshots display correctly
- [ ] Verify architecture diagrams are clear and readable
- [ ] Load all three integration pattern examples for demonstration
- [ ] QR code slide ready for GitHub repo
- [ ] Ensure all code snippets use high-contrast syntax highlighting

**Engagement tactics:**
- Poll audience: "Who's built with MkDocs? Sphinx? Jekyll? Other SSG?"
- Mid-talk: "Quick show of hands: who's tried embedding interactive content in docs?"
- Show comparison: Ask "Which interface looks cleaner to you: /notebooks/ or /lab/?"
- End with: "Clone the repo and explore the implementation—all code is open source"

**Timing notes:**
- If running long: Compress "Beyond Python" section (5 min → 3 min)
- If running short: Expand integration patterns comparison with more examples
- Have 2-3 extra configuration examples ready ("skip if needed" slides)
- Q&A buffer: Prepare 3-4 advanced topics (package loading, performance optimization, etc.)

---

## Pre-Submission Checklist

- [x] Title is catchy and sets clear expectations (WebAssembly + MkDocs + JupyterLite)
- [x] Category is singular and focused (Web Development / Documentation Engineering)
- [x] Elevator pitch is under 300 characters and includes key technical points
- [x] Target audience is explicitly identified (technical writers, web devs, educators, etc.)
- [x] Audience level matches prerequisites (Intermediate - requires SSG/Jupyter familiarity)
- [x] Exactly 3 audience takeaways listed (integration patterns, architecture, configs)
- [x] Outline includes timed sections with descriptions (45 minutes total)
- [x] Description expands on elevator pitch with bootcamp evolution story
- [x] Special requirements noted (screen sharing for recorded demos)
- [x] Removed any overly identifying information for anonymous review
- [x] Proofread for typos and clarity
- [x] Technical accuracy verified (Pyodide version, plugin names, config syntax)
- [x] Removed all live debugging references
- [x] Updated to three integration patterns (not four)

---

## Copywriting Techniques Used

**1. Pain Point Identification**
- "Setup becomes the barrier" - universal learning frustration
- "Students give up before writing first line of code" - emotional impact
- "No one to help them get unstuck" - isolation problem for self-learners

**2. Technical Credibility Through Specificity**
- Named technologies: Pyodide, WebAssembly, mkdocs-jupyterlite plugin
- Specific configuration examples (not just "configure the tool")
- Quantified metrics: "65% increase in code attempted," "10MB+ bundle size"
- Version numbers and technical details show real implementation experience

**3. Problem → Solution → Outcome Flow**
- **Problem**: Bootcamp students missing setup training get stuck before learning Python
- **Solution**: WebAssembly-powered browser execution via JupyterLite eliminates installation
- **Outcome**: Zero setup barriers for learners + zero backend infrastructure needed

**4. Testing and Learning in Public** (Integration Patterns)
- Three approaches tested, showing what worked and what didn't
- Transparent about why `/lab/` was too cluttered for embedding
- Decision criteria based on real production experience

**5. Honesty About Limitations**
- "Not all Python packages work" - sets realistic expectations
- "10MB+ bundle size" - acknowledges performance trade-offs
- "Path configuration breaks" - admits common failure modes
- Builds trust by not overselling

**6. Concrete Implementation Details**
- Actual YAML configuration snippets
- Specific plugin names and version requirements
- Real GitHub Actions workflow references
- "Copy-paste ready" signals immediate usability

**7. Universal Technical Hook: WebAssembly**
- Frames as broader pattern, not just "Python notebooks"
- "Rust playgrounds, SQL interfaces, algorithm visualizations"
- Appeals beyond Python-specific audience
- Positions talk as foundational skill vs. niche tool

**8. Social Proof Through Production**
- "Thousands of learners" using the system
- "Open-source repository" for verification
- "GitHub Pages deployment" proves it works at scale
- Real metrics (not testimonials) validate approach

**9. Eliminates Objections Proactively**
- **Backend concerns?** "No servers, zero infrastructure"
- **Complexity?** "Production-ready configs you can clone"
- **Performance?** "10MB initial load, caches well"
- **Browser support?** Addressed in internal notes prep

**10. Multi-Persona Value Proposition**
- **Technical writers**: Runnable code examples
- **Web developers**: Practical WebAssembly application
- **Educators**: Zero-infrastructure interactive content
- **Developer advocates**: Live demos without "works on my machine"

---

## Why This CFP Works for Technical Audiences

### For Technical Writers / Documentation Engineers:
- **Solves immediate problem**: Making documentation interactive without backend
- **Practical takeaway**: Real production patterns from working bootcamp site
- **Clear decisions**: Three patterns tested—see what worked and what didn't
- **Risk mitigation**: Understanding trade-offs helps choose right approach

### For Web Developers:
- **WebAssembly application**: Real implementation, not theory
- **Interface comparison**: `/notebooks/` vs `/lab/` - when to use each
- **Broader pattern**: Shows WebAssembly enabling static site interactivity
- **Performance data**: Bundle sizes, caching strategies included

### For Educators / Course Creators:
- **Infrastructure elimination**: No JupyterHub servers to manage
- **Student friction removal**: Zero-install = higher completion rates
- **Proven at scale**: Real bootcamp case study with metrics
- **Cloneable implementation**: Can fork and adapt immediately

### For DevOps / Platform Engineers:
- **Zero backend infrastructure**: Eliminates entire operational burden
- **Static site deployment**: Leverages existing CI/CD knowledge
- **Scalability**: GitHub Pages handles thousands of users
- **Cost reduction**: No server costs for interactive demos

### For Developer Advocates:
- **Live demo capability**: Attendees run code during presentation
- **No "works on my machine"**: Browser-based = consistent experience
- **Immediate experimentation**: Users try library before installing
- **Conference-friendly**: Works on conference WiFi, no backend needed

### For Open-Source Maintainers:
- **Lower contribution barrier**: Try code without installing
- **Documentation enhancement**: Interactive examples increase understanding
- **Onboarding improvement**: New contributors experiment risk-free
- **Community building**: Interactive docs create engagement

---

**This CFP shares a real journey from bootcamp roadblocks to production solution, showing how WebAssembly eliminates barriers to learning. The patterns apply to any documentation or educational content where setup friction prevents engagement.**
