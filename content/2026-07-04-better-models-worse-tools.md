Title: Link: Better Models Worse Tools via Armin Ronacher
Date: 2026-07-04
Category: Link Blog
Status: published

On his blog, Armin Ronacher shares his thoughts debugging Claude models sometimes calling Pi's edit tool with invented fields. He hypothesizes that modern Anthropic models learn what a tool call looks like and what mistakes are tolerated in the Claude Code harness environment.


> If you have not spent too much time looking at LLM tool calling internals, the important thing to understand is that tool calls are not magic and use some rather crude in-band signalling. The model receives a transcript, a system prompt and a list of available tools. The server munches that into a large prompt with special marker tokens. Because the model was trained and reinforced on examples of that format, at some point during generation it emits something that the API or client interprets as “call this tool with these arguments”.

>To the best of my knowledge, the call above would come out serialized like this from the model:
```
<antml:function_calls>
  <antml:invoke name="edit">
    <antml:parameter name="path">some/file.py</antml:parameter>
    <antml:parameter name="edits">
[
  {
    "oldText": "text to replace",
    "newText": "replacement text"
  }
]
    </antml:parameter>
  </antml:invoke>
</antml:function_calls>
```


>There are two very different ways to make the model produce a structure like this:
- You can ask the model to produce valid JSON matching a schema and then validate it afterwards.
- You can constrain the sampler so that invalid JSON, or even invalid schema shapes, cannot be sampled in the first place.
The second approach is what people usually refer to as grammar-aware or constrained decoding. The sampler masks out tokens that would violate the grammar. If the model is currently inside a JSON object and the schema says only oldText and newText are allowed, the sampler can prevent it from emitting "in_file" or "type". Grammar-aware decoding can be used both to constrain something to be syntactically valid JSON and also to enforce specific enum values or keys.

>Claude Code’s own tools are comparatively flat. The ordinary edit tool is not Pi’s nested edits[] shape; it is closer to file_path, old_string, new_string, and an optional flag (replace_all). Looking at Claude Code’s client is very instructive: it contains retry paths for malformed tool use, parameter aliases, type coercions, Unicode repairs and filtering of unknown keys. In other words, Anthropic’s own client appears to expect and accept a fair amount of slop and repairs it, mostly silently.
If reinforcement learning happens in a harness like that, or a simulation of one, then slightly malformed tool calls can still complete the task and receive reward. The harness fully absorbs the error and there is little gradient against inventing an alias, adding a stray field or using a nearby parameter name.

>Will this problem be with us in other harnesses too? One huge issue with Anthropic is that the models are completely closed, and so is the harness. Codex models are also closed, but at least the harness is not. We also have gpt-oss which is at least a bit interesting. The models are explicitly trained to use OpenAI’s harmony response format and there is a lot of documentation that at least tells us how OpenAI people think about this.

>Tool schemas are somewhere in the distribution and some shapes are close to what the model saw during post-training and some are far away. Some are easy for the provider’s hidden encoding (e.g. top-level attributes in ANTML), whereas some require the model to write large escaped JSON objects inside nested arrays after long multiline strings. The model may be smart enough to understand the schema and still be bad at sampling the exact shape under pressure.
If this type of model behavior continues, I wonder what the implications for harnesses are. Obviously one could turn on strict sampling in Anthropic and the problem should go away. On the other hand, that the model has this behavior shows the impact that reinforcement learning has on them. Fighting that prior is probably futile if you want to get the best model performance.


Via: [https://lucumr.pocoo.org/2026/7/4/better-models-worse-tools/](https://lucumr.pocoo.org/2026/7/4/better-models-worse-tools/)