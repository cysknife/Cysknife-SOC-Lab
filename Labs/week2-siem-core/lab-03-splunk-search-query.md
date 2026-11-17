

\#### Content for `Labs/week2-siem-core/lab-03-splunk-search-query.md`:

```markdown

\# Lab 3: Splunk Search Queries (SPL)



\## Objective

Write basic SPL queries to search, filter, and analyze log data.



\## Steps



\### 1. Search for Failed Login Attempts

Filter logs to find potential brute force attempts (Event ID 4625 or status code 401/403):

```spl

index=main status="FAILED" OR event\_id=4625

