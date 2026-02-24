Title: Link: AI Engineering in the real world via Gergely Orosz
Date: 2025-03-25
Category: Link Blog
Status: published

Based on his interviews with engineers at several technology companies, Gergely Orosz shares real world examples of building applications that use LLMs. He interviewed engineers at seven companies in different stages and various segments of tech. Common choices for their technology stack include Postgres and pgvector for storing embeddings and searching them, OpenAI, Anthropic and Google for the models, and Kubernetes for orchestrating compute resources. An engineering challenge with LLMs is the time it takes for LLMs to give answers because of their size. The businesses found that the cost of LLMs can be controlled through optimizations as the cost landscape changes.


> **Incident.io** is a tool to help resolve outages as they happen. A few months ago, the engineering team went back to the drawing board to build features that capitalize on how much LLMs have improved to date. Two of these features:
> * AI note taker during incidents. This includes live transcription, real-time summaries for people joining a call to get up to speed with, and key decisions/actions to clarify who does what.
> * Incident investigator: an agent looks into an ongoing incident by checking code, logs, monitoring, and old incidents to identify root causes and share findings, with a responder being paged. More details on **how this tool is built**.
>
> Both these features make heavy use of LLMs, and also integrate with several other systems like backend services, Slack, etc.
>
> **Sentry: Autofix and issue grouping**
>
> **Sentry** is a popular application monitoring software. Two interesting projects they built:
> * Autofix: make it really fast to go from a problem with code (a Sentry issue) to a fix with a GitHub PR. Autofix is an open source RAG framework that combines all of Sentry's context/telemetry data with code in order to root cause, fix, and create unit tests for bugs.
> * Issue Grouping: cut down alerting volume while reducing noise. For this, the team used recent advancements in approximate neighbor search (ANN), plus dramatic recent improvements in embedding quality from the new BERT architecture transformer models.
>
> Both these features are **fair source**, meaning you can see exactly how they work.
>
> **Wordsmith: legal AI**
>
> **Wordsmith** is building AI tools that legal teams use, including:
> * Documents workspace: plug into all of a company's communication streams, including analyzing documents and augmenting their contents, and drafting communications. **Check out a video of it in action.**
> * AI contract review: A product that can analyse any contract or website, then review it and generate a marked-up word doc, **here**. Basically, it's a lawyer anyone can use.
>
> **Augment Code**
>
> **Augment Code** is an AI coding assistant for engineering teams and large codebases. This kind of product probably needs little introduction for devs:
> * AI coding assistant: including IDE extensions for VS Code, JetBrains, Cursor, and Vim, and a Slack extension
> * Fine-tuning models: for AI coding tools, models make a big difference. The team don't pre-train models or build their own LLMs, but run extensive post-training and do fine tuning to suit the 4-5 models used for specific coding-related cases.
>
> **Elsevier: RAG platform**
>
> **Elsevier** is one of the world's leading publishers of scientific and medical content. Matt Morgis was an engineering manager at the company when the engineering leadership noticed that several product teams were independently implementing **RAG capabilities**; each sourcing content, parsing it, chunking it, and creating embeddings.
>
> An enterprise-wide RAG platform was the solution Matt and his team built, to enable multiple teams to build AI-powered products for medical and scientific professionals. Their platform consists of:
> 1. Database. A content database that centralized and normalized content from various sources.
> 2. Embeddings+search: A content embedding & indexing pipeline and vector search API.
> 3. LLM API: interfacing to multiple LLM models. This API allows teams to experiment with different models by changing a parameter on the API. It also allowed Elsevier to track the usage of various LLM models based on applications using it.
>
> Products built on top of this platform:
> * Intelligent tutoring system for medical students
> * Clinical decisions support tool for doctors
>
> **Insurance company: chatbot**
>
> Ashley Peacock is a staff software engineer at the insurer, **Simply Business**, who built a pretty common use case: a chatbot for customers to get answers to questions. This seems like the simplest of use cases – you might assume it just involves connecting documentation for the chatbot to use – but it was surprisingly challenging because:
> * Industry regulation. The chatbot cannot be inaccurate or make things up, as customers use the information to make decisions about which insurance purchases.
> * Non-deterministic responses. The business needed to turn a nondeterministic chatbot into one that only produces approved responses.
>
> The team had the idea to create an "approved answers" knowledge base for the chatbot, and faced the challenge of creating the questions for this. The team made the chatbot state when it cannot answer a question, and to then connect with human support, which then updated the knowledge base with their solution. This approach works pretty well after taking a few iterations to get right.
>
> **HR SaaS: summarization features**
>
> **Data Solutions International** (DSI) is a 30-person HR tech company with 5 engineers, selling products that help with performance review processes, assessments, and employee engagement surveys. The company is family-owned, has been operating for 27 years, and is profitable.
>
> Summarizing comments for employee engagement processes was the first feature they wanted to build, as something customers would appreciate, and which the team could learn about working with LLMs from.
>
> During an employee engagement process, there are questions like "what do you like most about working here", and "if you could change one thing about working at Company X, what would it be?", etc. For larger companies with thousands of employees, there may be thousands of comments per question. Individual departmental leads might read all comments relevant to them, but there's no way an HR team at a very large business could check every single comment.
>
> Before LLMs, such comments were categorized into predefined categories, which were hardcoded, per company and per survey. This was okay, but not great. Data Solutions International's goal was to use LLMs to summarize a large number of comments, and report to survey admins the broad categories which comments belong in, how many comments per category there are, and to allow drilling down into the data.


Via: [https://newsletter.pragmaticengineer.com/p/ai-engineering-in-the-real-world](https://newsletter.pragmaticengineer.com/p/ai-engineering-in-the-real-world)
