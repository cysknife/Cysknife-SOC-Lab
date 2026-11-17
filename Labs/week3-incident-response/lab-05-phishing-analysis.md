

\---



\### 6. `Labs/week3-incident-response/lab-05-phishing-analysis.md`

This lab guides students through analyzing a mock phishing email, extracting headers, validating authentication protocols, and extracting indicators.



```markdown

\# Lab 5: Phishing Email Analysis \& Triage



\## Objective

Learn how to analyze email headers, verify authentication protocols (SPF, DKIM, DMARC), and extract Indicators of Compromise (IOCs) from a phishing email.



\## Scenario

You are a SOC analyst. A user reported a suspicious email claiming to be from "Cysknife Support" asking for urgent credential verification. You need to analyze the email headers and body to determine if it is malicious.



\## Steps



\### Step 1: Extract and Parse Email Headers

Examine the raw MIME headers of the sample email provided in `/data/pcaps/sample\_phishing.eml`. Look for key fields:

\*   \*\*From / Return-Path\*\*: Check for spoofed display names vs actual domains.

\*   \*\*Received\*\*: Trace the path of the email from the source mail server to the recipient's inbox. Look for suspicious IP addresses.

\*   \*\*X-Originating-IP\*\*: Identify the actual source IP of the sender.



\### Step 2: Validate Email Authentication (SPF, DKIM, DMARC)

Use command-line tools or online validators to check the domain's authentication records:

\*   \*\*SPF (Sender Policy Framework)\*\*: Check if the sending IP is authorized to send mail for the domain.

&#x20;   ```bash

&#x20;   dig +short TXT example.com | grep spf

&#x20;   ```

\*   \*\*DKIM (DomainKeys Identified Mail)\*\*: Verify the cryptographic signature to ensure the email content was not altered in transit.

\*   \*\*DMARC (Domain-based Message Authentication)\*\*: Check the policy (`p=none`, `p=quarantine`, or `p=reject`) to see how receivers should treat failed authentication messages.



\### Step 3: Extract Indicators of Compromise (IOCs)

Analyze the email body for malicious elements:

\*   \*\*Suspicious URLs\*\*: Identify hidden links (hover over buttons, check raw HTML source).

\*   \*\*Malicious Attachments\*\*: Check file extensions (e.g., `.exe`, `.js`, `.docm`) and compute SHA-256 hashes.

\*   \*\*Social Engineering Keywords\*\*: Highlight urgent language ("Your account will be suspended in 24 hours").



\### Step 4: Classify and Write a Triage Verdict

Based on the evidence, write a triage report classifying the email:

\*   \*\*Verdict\*\*: Phishing / Malicious / Benign / Spam

\*   \*\*Confidence Level\*\*: High / Medium / Low

\*   \*\*Evidence\*\*: List the exact headers, IPs, and URLs that led to this conclusion.



\## Deliverables

Write a structured triage report containing the extracted IOCs (IPs, domains, hashes) and import them into your Splunk SIEM threat intelligence database to block future occurrences.

