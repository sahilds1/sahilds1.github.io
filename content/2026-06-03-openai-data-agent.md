Title: Link: How OpenAI Built Its Data Agent
Date: 2026-06-03
Category: Link Blog
Status: published

Emma Tang shared the work of the Data Platform Engineering team at OpenAI with ByteByteGo. She shared how their data agent works, how they uses Codex internally, what other teams can learn from  their data agent, and what comes next for OpenAI's Data Platform. 


> How the Data Agent Works: To understand the agent, we will look at three things: what users experience when they ask a question, what architecture supports that experience, and how a request moves through the agent until it returns a verified answer.

> The agent sits across the entire data platform and answers questions in natural language. A user can ask in Slack, in a web portal, in their IDE, or in the Codex CLI through MCP. The agent figures out which tables are relevant, writes SQL, runs it, checks the result, and returns the answer with its reasoning attached.

> The team’s approach is the opposite of what most people expect. The agent itself is simple. The reliability comes from the engineering around it: careful data acquisition that gives the agent the right context before it ever sees a question.

>Many agent systems become complicated at this point as shown in the figure below. A team might add a router that sends easy questions to a small, cheap model and hard ones to a larger model. It might mix multiple LLMs, fine-tune models on internal data, or build complex retrieval pipelines with different embedding models for different content types. Each choice can help, but each also adds cost, latency, and more ways for the system to fail.

>OpenAI’s data team took a different approach. They found that a simple architecture works well at their scale, backed by their robust and unified data platform foundation. The data agent they developed consists of four main components: a single LLM, a context assembly layer, a carefully curated set of tools, and an agent runtime.

>Three steps from question to verified answer. What makes the agent reliable is the quality of the context that flows through the three steps, which depends on the quality of the underlying infrastructure and how easy it is for the model to reason about

>A platform that serves 5,500 internal users gets a steady stream of support questions. A pipeline fails. A dashboard breaks. A permission link does not work. Every one of these ends up with the platform team, and each one requires investigation before it can be fixed. 

> How OpenAI Uses Codex Internally: The data platform uses Codex to read pipeline code each night, enriching the context the agent retrieves. That is one use case of Codex. But Codex supports many other use cases internally, helping run the platform itself.


Via: [https://blog.bytebytego.com/p/how-openai-built-its-data-agent](https://blog.bytebytego.com/p/how-openai-built-its-data-agent)