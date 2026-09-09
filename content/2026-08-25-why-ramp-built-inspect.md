Title: Link: Why Ramp built its own in-house coding agent, Inspect via The Pragmatic Engineer
Date: 2026-08-25
Category: Link Blog
Status: published

Ramp built its own AI infrastructure for a coding agent instead of using Codex, Claude Code, etc becuase  they found local machines are liminted in how many agents they can run, they wanted to improve their frontend tooling and had a need for remote deve environments. Block, Strip and Shopify also also write most of their code with their own coding agents. 

>At a select few tech companies, they write most of their code with their own, custom-built, internal AI coding agents. This is different from most of the industry which uses AI coding agents and harnesses like Codex, Claude Code, Cursor, OpenCode, GitHub Copilot, etc. At Ramp, their own version is called Inspect, while at Block it’s Goose (open source), at Stripe it’s Minions, and River at Shopify.

>A couple of things make Inspect different from coding agents like Claude Code and Cursor: Remote sandboxes: Inspect spins up a sandboxed remote development environment which unlocks unlimited session concurrency, centralized setup configuration, and cross-functional session collaboration. Internal integrations: Inspect is integrated across the org with the same tools and context that a Ramp engineer has; the only constraint on agents’ ability is model intelligence, not missing tools or access.

>Platform for agents: Engineers at Ramp have built more than 200 agents running on top of the Inspect platform. It’s clever that the Ramp team extended Inspect into a platform, and made it easy to build additional agentic tools, without engineers having to worry about the cloud backend for those tools

>SQLite: the database attached to the Durable Object. Stores all events that take place within an Inspect session, so that when another user joins, they can see the entire backlog of events. This enables ‘multiplayer’: two devs can work in the same session, or a PM can review the work inside a dev-started session.

>On top of local tools running on the sandbox, an Inspect session also gets access to internal and external tools that Ramp engineers use, as previously mentioned [integrated via API and MCP]. Inspect has read-only, sanitized access to the prod database that no third-party tool could have. One benefit of Ramp having its own, internal coding agent is that it gives read-only access to a sanitized version of their production database. 

>There are two main components of the sandbox: the developer environment and the coding harness. The development environment contains repository, services for local development (Postgres, Redis, RabbitMQ, Temporal, Vite, and others), visual verification, VS Code server. Ramp decided to use OpenCode as the harness, which gives Ramp devs the option to choose their model provider. The LLM gateway routes to the selected model.

>An Inspect session is collaborative by default and opt-outs aren’t available; the session is open for others to join and both the work and the prompting history are exposed. This “multiplayer-first” approach is deliberate, and has probably contributed to Inspect spreading as fast as it did. 

Via: [https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect](https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect)
