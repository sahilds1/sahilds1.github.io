Title: Link: Running local models is good now via Vicki Boykis
Date: 2026-07-04
Category: Link Blog
Status: published

On her blog, Vicki Boykis shares her experiences using the most recent releases of Google's Gemma 4 models to do agentic coding locally and finds she has loops work at about 75% of the accuracy and speed of frontier models.

>I’ve so far been using gemma-4-26b-a4b LM Studio implementation as my default local model. I’ve used the local setup so far to: Refactor a Python script that was a notebook into a repo of 5-6 modules, lint that module to use correct type hints for generics (most frontier models now do this automatically, but not always).
I’ve also used it to proofread some blog posts, write unit tests, and to bootstrap a repo that stands up a two-tower model for recommendations just to see what the agent would do with a blank slate.

>Gemma-4-12b-qat just came out but I’ve already also really been impressed with its performance relative to its size. The model architecture itself is really interesting and proposes a bunch of interesting questions like, “if we are constrained by performance and price, what architectural tradeoffs do we need to make?” a question that so far has not really been asked in the mad token gold rush.

>But don’t take my word for any of this, try it out for yourself! You’ll need a local model inference engine, an agentic harness, and the local model artifact if you want to try to run local agentic flows. You’ll need to set up the harness to point at your local inference endpoint, the downloaded model artifact served via the inference engine.

>For my local setup, I’m currently using Pi as the agent harness and LM Studio as the inference server, although it would likely be faster if I just used llama.cpp directly - a potential direction for a future experiment. I run every Pi session in a Docker container and give it permissions only to bash so that it can’t run Python code or do web browsing, although I do plan to allow curl in a different image for some research work I’m doing

Via: [https://vickiboykis.com/2026/06/15/running-local-models-is-good-now/](https://vickiboykis.com/2026/06/15/running-local-models-is-good-now/)