Title: TIL: Fundamentals of Rust
Date: 2026-02-18
Category: TIL
Status: published

# Simple Curl in Rust

I attended a [meetup](https://luma.com/adtkn9n8) on an introduction to Rust organized by the [PHL Code Club](https://phlcode.club/) where [Ben Corey](https://benjamincorey.net/) taught the fundamentals of Rust by [building a simple version of cURL](https://github.com/bcorey/phlcodeclub-curl-rs/).

We can invoke our app by running `curlrs` and it works anywhere, not just in the project directory.

## Setting up a Rust Development Environment

There's a Rust installer and version  management tool called Rustup and a Rust build tool and package manager called Cargo. There's a  walk through on getting started with Rust here: https://rust-lang.org/learn/get-started/

## Rust Programming Language 

I already know Python and when [comparing programming languages](https://chelseatroy.com/2020/07/15/how-to-jump-start-learning-a-new-programming-language/) I found notable differences in their paradigms (imperative/functional), collaboration (inheritance/interfaces), and handling null. 

There's a collection of  examples that illustrate Rust concepts here: https://doc.rust-lang.org/rust-by-example/index.html

### Paradigm

Driven by expressions and immutability, Rust's idioms push harder toward functional patterns.

```
let request = match (input.request_type, input.body) {
    (RequestType::Get, _) => client.get(input.url),
    (RequestType::Post, Some(body)) => client.post(input.url).body(body),
    (RequestType::Post, None) => client.post(input.url),
};
```

### Collaboration 

Shared behavior comes from traits, which declare a set of methods that any type can implement.

```
impl From<String> for RequestType { ... }
impl From<std::env::Args> for Input { ... }
```

### Handling Null

If absence is possible, the type must be Option<T> and you have to handle both cases before extracting values.

```
let request_type = args.next().unwrap().into();
let url = args.next().unwrap();
```
