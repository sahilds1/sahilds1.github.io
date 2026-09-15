Title: TIL: Speeding up Python with Concurrency
Date: 2025-07-23
Category: Today I Learned
Status: published

I started building AI evals (I/O Bound) and sped it up by evaluating the inputs concurrently.

> Concurrency refers to the ability of a program to manage multiple tasks at once, improving performance and responsiveness. It encompasses different models like threading, asynchronous tasks, and multiprocessing, each offering unique benefits and trade-offs. In Python, threads and asynchronous tasks facilitate concurrency on a single processor, while multiprocessing allows for true parallelism by utilizing multiple CPU cores.

> Concurrency can make a big difference for two types of problems. I/O-bound problems cause your program to slow down because it frequently must wait for input or output (I/O) from some external resource. They arise when your program is working with things that are much slower than your CPU. On the flip side, there are classes of programs that do significant computation without talking to the network or accessing a file. These are CPU-bound programs because the resource limiting the speed of your program is the CPU, not the network or the file system.

> For I/O-bound problems, there’s a general rule of thumb in the Python community: “Use asyncio when you can, threading or concurrent.futures when you must.” asyncio can provide the best speed-up for this type of program, but sometimes you’ll require critical libraries that haven’t been ported to take advantage of asyncio. Remember that any task that doesn’t give up control to the event loop will block all of the other tasks.

> There are a couple of issues with asyncio at this point. You need special asynchronous versions of libraries to gain the full advantage of asyncio. Had you just used Requests for downloading the sites, it would’ve been much slower because Requests isn’t designed to notify the event loop that it’s blocked. This issue is becoming less significant as time goes on and more libraries embrace asyncio.

Via: [https://realpython.com/python-concurrency/](https://realpython.com/python-concurrency/) 
