\# Capstone Project: SOC Analyst Simulation



\## Objective

Integrate all the skills acquired over the 4-week bootcamp (log parsing, SIEM correlation, phishing analysis, and incident response) to solve a simulated security breach.



\## Capstone Scenario: "The Database Exfiltration Attack"

An external threat actor has successfully breached the internal network of a local hospital database server. You are assigned as the Tier 2 Security Analyst to investigate, contain, and document the full lifecycle of this breach.



\## Lab Requirements

You will work with the log generator running in your Docker environment. You have access to:

\- Splunk SIEM (for log searching and visualization)

\- Vulnerable Web App (the entry point of the attack)

\- Raw generated JSON logs in `/data/logs/cysknife\_logs.jsonl`



\## Step-by-Step Tasks



\### Step 1: Alert Triage \& Prioritization (30 mins)

Look at the incoming SIEM alerts. Identify the initial compromise vector:

\*   Did the attacker exploit a SQL vulnerability on the web portal?

\*   Did they use stolen SSH credentials?

\*   Identify the \*\*Patient Zero\*\* machine IP address and the initial user account compromised.



\### Step 2: Threat Hunting \& Lateral Movement Analysis (45 mins)

Trace the attacker's path inside the local network (`10.10.0.0/16`):

\*   Find out how the attacker moved from the web server (`10.10.0.5`) to the database server (`10.10.0.20`).

\*   Identify the credentials dumped (e.g., using Mimikatz or similar techniques).

\*   List all internal hosts accessed by the attacker after gaining initial access.



\### Step 3: Data Exfiltration Analysis (30 mins)

Determine if and how data was stolen:

\*   Check outbound network traffic connections to external IPs.

\*   Analyze the volume of outbound traffic (look for massive spikes in DNS queries or HTTPS uploads).

\*   Identify the database tables accessed (e.g., `patient\_records`, `credentials`).



\### Step 4: Write the Final Incident Report (45 mins)

Compile your findings into a professional SOC Incident Report. It must include:

1\.  \*\*Metadata\*\*: Case ID, Severity (Critical), Date of Occurrence, Analyst Name.

2\.  \*\*Executive Summary\*\*: A brief 3-sentence summary of the breach, the data exposed, and the business impact.

3\.  \*\*Timeline of Events\*\*: A chronological table mapping timestamps to actions (Initial Access -> Execution -> Credential Access -> Lateral Movement -> Exfiltration).

4\.  \*\*IOCs (Indicators of Compromise)\*\*: A clean table listing malicious IPs, domains, file hashes, and user accounts to be blocked.

5\.  \*\*Remediation Steps\*\*: Concrete steps to patch the vulnerability, rotate credentials, and configure firewall rules to prevent recurrence.



\## Grading Criteria / Deliverables

To pass the capstone, submit:

\*   The \*\*Patient Zero IP\*\* and the exploit vector.

\*   The \*\*Exfiltrated Data Size / Destination IP\*\*.

\*   The complete \*\*Incident Response PDF report\*\*.

