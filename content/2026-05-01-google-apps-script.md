Title: Writing a script to back up Google Docs with Claude Code
Date: 2025-09-01 
Category: Projects
Status: published

To backup and recover my Google Docs, I wrote a script on [Google Apps Script](https://developers.google.com/apps-script) with Claude Code that exports my Google Docs to open formats ().docx, .xlsx, and .pptx) The Google Apps Script platform runs JavaScript code and has built-in libraries for Google applications. I'm new to JavaScript and the Google Apps Script libraries so I used Claude Code (Claude Opus 4.8 to write the script:

<script src="https://gist.github.com/sahilds1/4f0900f7f896ec2356184c290e7fe6c9.js"></script>

When deciding to use Google Apps Script, the key criterion was cost becuase I didn't want to use a paid service such as Insync or Backupify/CloudAlly. Among the free options is [rclone](rclone.org), which is a command line-utility to manage files on cloud storage services [that can export Google Docs from Google Drive](https://rclone.org/drive/#import-export-of-google-documents).  

Google Apps Script is simpler to setup than rclone becuase I can edit code right in the browser and the script is saved to Drive and runs on Google's servers. 

rclone has finer scheduling control than Google Apps Script  and I had to run the script every hour and skip exporting files already in the day's backup folder and when the day of the week isn't Sunday because Google Apps Script caps runs at 6 mins.
