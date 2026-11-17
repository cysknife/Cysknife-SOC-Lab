\# Lab 6: The Incident Response Lifecycle



\## Objective

Apply the 6 phases of the Incident Response (IR) lifecycle to a simulated security breach scenario inside the Cysknife lab environment.



\## Scenario

A company employee downloaded an invoice.exe attachment from a phishing email. The executable ran, encrypted files on the local workstation, and started spreading to other machines on the network. You are the Incident Response team lead.



\## The 6 Phases of Incident Response



\### Phase 1: Preparation

Before the incident occurs, prepare the infrastructure and policies.

\*   \*\*Task\*\*: Ensure the SIEM logs are actively collecting endpoint Sysmon logs, network flows, and DNS queries. Draft the communication plan (who to call when a ransomware incident happens).



\### Phase 2: Detection \& Analysis

Identify that an incident is occurring and analyze the scope.

\*   \*\*Task\*\*: Use your Splunk SIEM dashboard to search for:

&#x20;   \*   Multiple HTTP requests to known C2 domains.

&#x20;   \*   Sudden spikes in file modifications (`.encrypted` extension change).

&#x20;   \*   Process tree showing `invoice.exe` spawning `cmd.exe` and `powershell.exe`.

&#x20;   \*   Classify the severity of the alert as \*\*Critical\*\*.



\### Phase 3: Containment, Eradication, \& Recovery

Stop the threat, remove the malware, and restore systems.

\*   \*\*Short-Term Containment\*\*: Isolate the infected host from the network immediately (disable NIC or firewall block).

\*   \*\*Long-Term Containment\*\*: Block the C2 IP address and the phishing sender domain at the proxy firewall level.

\*   \*\*Eradication\*\*: Identify the persistence mechanism (e.g., registry Run keys or scheduled tasks) and delete the malicious binary `invoice.exe`.

\*   \*\*Recovery\*\*: Restore files from clean backups and verify system integrity before reconnecting the machine to the network.



\### Phase 4: Lessons Learned

Review the incident and write a report to improve future responses.

\*   \*\*Task\*\*: Conduct a post-incident meeting. Document:

&#x20;   \*   Time to detect (TTD) and time to contain (TTC).

&#x20;   \*   What went wrong (e.g., email filters didn't catch the phishing email).

&#x20;   \*   Recommendations (implement application whitelisting, conduct user awareness training).



\## Deliverables

Create a formal \*\*Incident Report (IR Report)\*\* following the standard template containing:

1\. Executive Summary (non-technical overview for management).

2\. Technical Analysis (timeline, root cause, indicators of compromise).

3\. Actionable Recommendations to prevent recurrence.

