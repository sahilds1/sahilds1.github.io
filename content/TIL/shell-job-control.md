Title: Shell job control
Date: 2024-10-07    
Tags: shell
Slug: shell-job-control
Summary: Short version for index and feeds
Status: draft


In a terminal, your process can be in one of 3 states

1. Foreground: Normal state when you start a process
2. Background: Process is still running but you can't interact with it
3. Stopped: Process is paused (won't keep using CPU) but you can restarte it

Commands for moving processes between these 3 states

- `some_process &`: Start a background process
- `Ctrl+z`:  Stops the current foreground process
- `jobs` Lists all active processes in your terminal
-  `fg` or `bg`: Move a specific job to foreground/background

https://jvns.ca/blog/2024/07/03/reasons-to-use-job-control/