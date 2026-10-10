#!/usr/bin/env python3
"""oneclick-check: paste raw email headers (stdin or file); checks RFC 8058 one-click unsubscribe (Gmail/Yahoo bulk-sender rule)."""
import sys, re, email
def main():
    raw=open(sys.argv[1]).read() if len(sys.argv)>1 else sys.stdin.read()
    m=email.message_from_string(raw); lu=m.get_all("List-Unsubscribe") or []; lup=m.get_all("List-Unsubscribe-Post") or []
    probs=[]
    if not lu: probs.append("no List-Unsubscribe header")
    elif not any(re.search(r"<https://",v) for v in lu): probs.append("List-Unsubscribe has no https:// URI (mailto alone is not one-click)")
    if not any(v.strip()=="List-Unsubscribe=One-Click" for v in lup): probs.append("missing 'List-Unsubscribe-Post: List-Unsubscribe=One-Click'")
    dk=" ".join(m.get_all("DKIM-Signature") or [])
    if dk and "list-unsubscribe" not in dk.lower(): probs.append("DKIM h= does not cover List-Unsubscribe / -Post (RFC 8058 sec. 4 requires it)")
    if not dk: probs.append("no DKIM-Signature in pasted headers (paste the headers as received)")
    for p in probs: print("FAIL", p)
    if not probs: print("PASS: RFC 8058 one-click headers present and signed")
    else: print("\nPer-ESP fix (free header check first): https://oneclickout.adjudi.com/?utm_source=github&utm_medium=cli&utm_campaign=oneclickout-intent-w2&utm_content=oneclick-check")
    sys.exit(1 if probs else 0)
if __name__=="__main__": main()
