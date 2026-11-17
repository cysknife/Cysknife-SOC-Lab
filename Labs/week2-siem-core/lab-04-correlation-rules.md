\# Lab 4: Building SIEM Correlation Rules



\## Objective

Learn how to write correlation rules in Splunk to detect multi-stage attacks by linking isolated events.



\## Scenario

An attacker often performs reconnaissance (port scanning) before launching an exploit. Individually, a single port scan might look normal, but when correlated with web application errors and SQL injection attempts, it indicates a major threat.



\## Steps



\### Step 1: Write a Correlation Search for Brute Force Patterns

Create a search that correlates multiple failed logins with a successful login from the same IP address, indicating a successful password brute-force attack.



In Splunk, use the `stats` and `transaction` commands:

```spl

index=main (event\_id=4625 OR status="FAILED") 

| stats count as fail\_count, values(user) as users by ip\_address 

| join ip\_address 

| search event\_id=4624 status="SUCCESS" 

| where fail\_count > 5

| table ip\_address, fail\_count, users, user

Step 2: Create a Correlation Rule for Web Attacks
Correlate web server logs showing SQL injection payloads with system-level process creations on the backend database server.


index=main event_type="sql_injection" 
| stats count as sqli_count by ip_address 
| where sqli_count > 3 
| join ip_address 
| search event_id=4688 process="cmd.exe" OR process="powershell.exe"
| table ip_address, sqli_count, process
Step 3: Configure Splunk Alert Actions
Save the correlation searches as Saved Searches and configure them to trigger alerts:

Go to Settings > Searches, reports, and alerts.
Click New.
Paste your correlation SPL query.
Under Schedule and alert, set the schedule to run every 5 minutes.
Configure the alert trigger threshold (e.g., trigger alert when result count is greater than 0).

