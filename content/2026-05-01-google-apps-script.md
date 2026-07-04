Title: Writing a script to backup Google Docs with Claude Code
Date: 2025-09-01 
Category: Projects
Status: published

To backup and recover my Google Docs, I wrote a script on [Google Apps Script](https://developers.google.com/apps-script) with Claude Code that exports my Google Docs to open formats (.docx, .xlsx, .pptx). The Google Apps Script platform runs JavaScript code and has built-in libraries for Google applications. 

<script src="https://gist.github.com/sahilds1/4f0900f7f896ec2356184c290e7fe6c9.js"></script>

When deciding to use Google Apps Script, the key criterion was cost becuase I didn't want to use a paid service such as Insync or Backupify/CloudAlly. Among the free options is [rclone](rclone.org), which is a command line-utility to manage files on cloud storage services and [that can export Google Docs from Google Drive](https://rclone.org/drive/#import-export-of-google-documents).  

To implement a backup script of my Google Docs, the key features of a solution are the ability to setup and schedule runs. I can schedule runs on both Google Apps Script and rclone (rclone has finer scheduling control), but Google Apps Script is simpler to setup. With Google Apps Script, I can edit code right in the browser, the script is saved to Drive and runs on Google's servers. 

I'm new to both JavaScript and the Google Apps Script libraries so I used Claude Code (Claude Opus 4.8). During my agentic coding sessions, I guided the agent through two key design decisions for the backup and recovery script. First, I guided the agent to replace the recursive subfolder-mirroring design that it had started with to using a flat dated folder and searching the entire Drive at once. Second, I guided the agent to replace the self-rescheduling continuation design it had started with for the 6 minute runtime limit with skpping files already in today's folder and setting the existing trigger to run hourly. 

```
**Yes** — removing the subfolder mirroring simplifies the script significantly. Here's the tradeoff first:

---

**Tradeoff**

| | Current script | Simplified script |
|---|---|---|
| Folder structure in snapshot | Mirrors your Drive structure | Flat — all files in one dated folder |
| Find a specific file | Navigate subfolders | Scroll through one folder |
| Duplicate filenames | No issue — separated by subfolder | Risk — two files named `Notes.docx` in different folders would conflict |
| Code complexity | Recursive | Simple loop |

---

**Duplicate filename risk**

If you have two files with the same name in different folders:
```
Work/Notes.docx
Personal/Notes.docx
```

The flat snapshot would try to create two files both named `Notes.docx` in the same folder — the second would overwrite the first silently.

If your Drive has no duplicate filenames across folders this is not an issue. Worth checking before switching.

**What changed**

| Change | Detail |
|---|---|
| Removed `processFolder` entirely | No longer needed |
| Removed subfolder recursion | No longer needed |
| `DriveApp.getFilesByType` | Searches entire Drive at once instead of folder by folder |
| All files save directly to `todayFolder` | Flat structure, no subfolders |

The script went from two nested functions down to one simple loop — significantly easier to read and maintain.
```


```
## The options

**1. Do nothing structural — just fix the dry-run fetch**
- *What:* Skip the network fetch in dry-run mode only.
- *Effect:* Makes dry runs fast, but a **real** run still won't finish — you saw ~220 Docs eat the whole 6 min, and Sheets/Slides never ran. Doesn't solve the actual backup failure.
- *Simplicity:* Trivial. *Verdict:* Necessary but insufficient.

**2. Self-rescheduling continuation (what I had drafted)**
- *What:* Stop near a time budget, create a one-off trigger to resume in ~1 min, skip files already in today's folder, repeat until done.
- *Tradeoffs:* Fully automatic, completes within ~15-20 min unattended. But it's the most code: trigger creation/deletion, tracking the continuation trigger by id so it doesn't clobber the weekly trigger, a resume-by-skip check. More moving parts = more to reason about.
- *Simplicity:* Lowest. *Verdict:* Robust but heavy for a personal weekly backup.

**3. Idempotent resume + more frequent plain schedule (no self-triggering)**
- *What:* Add only the "skip files already in today's folder" check. Don't self-reschedule. Instead set the *existing* trigger to run, say, hourly. Each run grabs another batch; once everything's exported, subsequent runs are cheap no-ops.
- *Tradeoffs:* Much less code than #2 — no dynamic trigger juggling, no id tracking. Downside: a backup may take a few hours to fully land, and you run the script more often (still trivially within quotas). "Same day" semantics matter — resume keys off today's dated folder.
- *Simplicity:* Medium, and notably simpler than #2 because it drops all trigger manipulation. *Verdict:* Good balance.

**4. Process one file type per run / partition the work**
- *What:* Export Docs on one trigger, Sheets on another, Slides on another (or shard alphabetically). 
- *Tradeoffs:* Dead simple conceptually, no state. But your Docs alone already blew the budget, so type-partitioning isn't enough — you'd need finer shards, which gets fiddly and fragile as your library grows.
- *Simplicity:* High per-piece, but doesn't reliably solve it at your volume. *Verdict:* Brittle.

**5. Switch the engine to rclone (already noted in your header comments)**
- *What:* Drop Apps Script; run `rclone` (e.g. on a laptop/cron or a small always-on box) to sync/export Drive.
- *Tradeoffs:* No 6-minute limit, no fetch quotas, far more capable. But it needs a host that runs on schedule, initial setup/auth, and ongoing maintenance — exactly the "extra complexity hard to justify" your own comment flags. Moves the work off Google's free infra.
- *Simplicity:* Low setup simplicity, high operational ceiling. *Verdict:* Right answer only if you outgrow Apps Script.

**6. Incremental backups (only export files changed since last run)**
- *What:* Track `getLastUpdated()` and only export files modified since the previous snapshot.
- *Tradeoffs:* Each run becomes tiny after the first, so timeouts mostly disappear. But it changes the model from "full weekly snapshot" to "incremental," complicates the folder/versioning story, and the *first* run still needs one of the above to get over the initial hump.
- *Simplicity:* Medium code, bigger conceptual change. *Verdict:* Powerful but a different product.

## My read

The cleanest fix that actually solves it with the least machinery is **#3** (idempotent skip + run the existing trigger more often), plus the **#1** dry-run fetch fix. It avoids the trigger-management complexity of #2 while still completing unattended. Choose **#2** only if you specifically want it to finish fast in a single chained burst rather than over a few hours, and **#5** only if you're ready to maintain a host.

Want me to implement #3 + #1?
```