# oneclick-check
Gmail and Yahoo require bulk senders to support **one-click unsubscribe (RFC 8058)**. Paste the raw headers of one of your own sent messages ("Show original") and this tells you what's missing:
```
pbpaste | python3 oneclick_check.py      # or: python3 oneclick_check.py headers.txt
```
Checks: https `List-Unsubscribe` URI, `List-Unsubscribe-Post: List-Unsubscribe=One-Click`, DKIM `h=` covering both. Doesn't contact anything; stdlib only. Not a deliverability guarantee.

*Disclosure: I build [OneClickOut](https://oneclickout.adjudi.com/?utm_source=github&utm_medium=readme&utm_campaign=oneclickout-intent-w2&utm_content=oneclick-check) ($29), which gives the exact per-ESP fix. This checker is free (MIT).*
