# AI Use Decision Flowchart

## Overview

This decision tree helps determine whether AI should be used for a specific task, what level of human oversight is required, and what documentation is needed. Work through each section in order.

---

## Quick Reference Summary

```
START
  |
  v
Is this use prohibited? --> YES --> STOP - Do not proceed
  |
  NO
  v
Does task involve sensitive data? --> YES --> Apply privacy safeguards
  |
  NO/SAFEGUARDS APPLIED
  v
What is the risk level? --> Determine oversight requirements
  |
  v
Document decision and proceed
```

---

## Section 1: Should AI Handle This Task?

### Step 1.1: Check Prohibited Uses First

**Is the proposed AI use in the prohibited category?**

Answer these questions - if ANY answer is YES, **STOP - AI use is not permitted**:

| Question | YES | NO |
|----------|-----|-----|
| Does this involve creating fake/misleading content? | STOP | Continue |
| Will this process personal data without consent? | STOP | Continue |
| Could this discriminate based on protected characteristics? | STOP | Continue |
| Does this involve automated legal/medical decisions without human review? | STOP | Continue |
| Will confidential data be entered into a public AI tool? | STOP | Continue |
| Does this create security risks or exploit vulnerabilities? | STOP | Continue |

If all answers are NO, proceed to Step 1.2.

---

### Step 1.2: Evaluate Task Suitability

**Is AI the right tool for this task?**

```
                        START HERE
                             |
                             v
        +------------------------------------------+
        |  Is this task repetitive and rule-based? |
        +------------------------------------------+
                    /              \
                  YES               NO
                   |                 |
                   v                 v
        +-----------------+  +------------------------+
        | Good AI fit     |  | Does task require      |
        | Proceed to      |  | creativity/judgment?   |
        | Step 1.3        |  +------------------------+
        +-----------------+         /          \
                                  YES            NO
                                   |              |
                                   v              v
                    +------------------+  +------------------+
                    | AI can assist,   |  | Is data analysis |
                    | but human        |  | or pattern       |
                    | creativity       |  | recognition      |
                    | required         |  | needed?          |
                    +------------------+  +------------------+
                           |                  /          \
                           |                YES           NO
                           |                 |             |
                           v                 v             v
                    +-----------------+  +----------+  +----------+
                    | Human-AI        |  | Good AI  |  | Consider |
                    | collaboration   |  | fit      |  | manual   |
                    | recommended     |  |          |  | process  |
                    +-----------------+  +----------+  +----------+
```

### AI Task Suitability Matrix

| Task Type | AI Suitability | Recommendation |
|-----------|---------------|----------------|
| Data entry/transcription | High | Automate with verification |
| Pattern recognition | High | AI-first with exception review |
| Content drafting | Medium | AI draft + human editing |
| Customer communication | Medium | AI-assisted, human approved |
| Strategic decisions | Low | Human decision, AI input |
| Creative work | Medium | AI brainstorm, human create |
| Compliance/legal | Low | Human-led, AI assist |
| Emotional support | Low | Human primary, AI routing |

---

### Step 1.3: Benefits vs. Risks Assessment

Complete this quick assessment:

**Potential Benefits** (check all that apply):
- [ ] Saves significant time (>50% reduction)
- [ ] Improves consistency/accuracy
- [ ] Enables 24/7 availability
- [ ] Reduces costs substantially
- [ ] Scales beyond human capacity
- [ ] Enhances customer experience

**Potential Risks** (check all that apply):
- [ ] Privacy concerns
- [ ] Accuracy/hallucination risk
- [ ] Bias potential
- [ ] Customer trust impact
- [ ] Compliance requirements
- [ ] Security vulnerabilities

**Decision**:
- More benefits than risks checked = Proceed with appropriate safeguards
- More risks than benefits = Reconsider or add significant safeguards
- Equal = Conduct deeper analysis before proceeding

---

## Section 2: What Level of Human Oversight?

### Step 2.1: Determine Impact Level

```
                    What could go wrong?
                           |
           +---------------+---------------+
           |               |               |
           v               v               v
      +--------+     +---------+     +----------+
      | Minor  |     | Moderate|     | Severe   |
      | Impact |     | Impact  |     | Impact   |
      +--------+     +---------+     +----------+
           |               |               |
           v               v               v
      Internal      Customer        Legal/
      convenience   inconvenience   financial/
      only          or confusion    reputational
           |               |               |
           v               v               v
      LEVEL 1        LEVEL 2         LEVEL 3
      Oversight      Oversight       Oversight
```

### Impact Assessment Questions

| Factor | Low (1 point) | Medium (2 points) | High (3 points) |
|--------|---------------|-------------------|-----------------|
| Who sees output? | Internal only | Customers | Public/regulatory |
| Reversibility | Easily undone | Moderately fixable | Permanent/difficult |
| Financial impact | <$100 | $100-$10,000 | >$10,000 |
| Legal exposure | None | Minor | Significant |
| Reputation risk | Minimal | Some | Major |

**Total Score**:
- 5-8 points: Level 1 Oversight
- 9-12 points: Level 2 Oversight
- 13+ points: Level 3 Oversight

---

### Step 2.2: Apply Oversight Level

#### Level 1: Minimal Oversight

**When**: Low-risk, internal tasks, easily reversible

**Requirements**:
- [ ] Periodic spot-checks (weekly)
- [ ] Monthly quality review
- [ ] User can override AI decisions
- [ ] Basic logging maintained

**Examples**: Internal summarization, scheduling suggestions, data categorization

---

#### Level 2: Standard Oversight

**When**: Customer-facing, moderate risk, some consequences

**Requirements**:
- [ ] Sample review of outputs (20%+ reviewed)
- [ ] Human approval before external communication
- [ ] Clear escalation path to human
- [ ] Detailed logging and audit trail
- [ ] Regular accuracy monitoring
- [ ] Customer can request human review

**Examples**: Customer email drafts, chatbot responses, content recommendations

---

#### Level 3: Full Oversight

**When**: High-stakes decisions, legal/financial impact, sensitive data

**Requirements**:
- [ ] 100% human review before action
- [ ] AI provides recommendation, human decides
- [ ] Multiple reviewers for critical decisions
- [ ] Complete audit trail
- [ ] Regular bias and accuracy audits
- [ ] Customer notification of AI involvement
- [ ] Appeal/override process documented

**Examples**: Account decisions, pricing, hiring assistance, legal document drafting

---

## Section 3: Privacy Considerations

### Step 3.1: Data Classification Check

**What type of data will AI process?**

```
        What data does this AI task involve?
                       |
    +------------------+------------------+
    |                  |                  |
    v                  v                  v
Public Data      Business Data      Personal Data
    |                  |                  |
    v                  v                  v
No special       Standard          Continue to
precautions      security          Step 3.2
needed           required
```

---

### Step 3.2: Personal Data Assessment

**If personal data is involved, answer these:**

| Question | Action Required |
|----------|-----------------|
| Is data minimized to only what's needed? | If NO - Reduce data scope |
| Do we have consent/legal basis for this use? | If NO - Obtain consent or stop |
| Is data anonymized where possible? | If NO - Anonymize if feasible |
| Does AI vendor have data processing agreement? | If NO - Execute DPA or use different tool |
| Can data subjects exercise their rights? | If NO - Implement rights mechanisms |
| Is data retained only as long as needed? | If NO - Set retention limits |

---

### Step 3.3: Privacy Safeguard Checklist

Before proceeding with personal data:

- [ ] **Lawful basis documented** (consent, contract, legitimate interest, etc.)
- [ ] **Privacy policy updated** to cover this AI use
- [ ] **Data minimization applied** - only necessary data used
- [ ] **Vendor security verified** - SOC 2, ISO 27001, or equivalent
- [ ] **Data processing agreement** in place with AI vendor
- [ ] **Retention period defined** and enforced
- [ ] **Access controls** limit who can see AI outputs with personal data
- [ ] **Audit logging** captures AI access to personal data
- [ ] **Deletion procedures** include AI-processed data

---

## Section 4: Risk Assessment

### Step 4.1: Risk Identification

For the proposed AI use, rate each risk area:

| Risk Category | None (0) | Low (1) | Medium (2) | High (3) |
|---------------|----------|---------|------------|----------|
| **Accuracy**: Could AI make consequential errors? | | | | |
| **Bias**: Could AI discriminate unfairly? | | | | |
| **Privacy**: Is sensitive data at risk? | | | | |
| **Security**: Could this create vulnerabilities? | | | | |
| **Compliance**: Are there regulatory concerns? | | | | |
| **Reputation**: Could this damage trust? | | | | |
| **Financial**: Could errors cause monetary loss? | | | | |
| **Operational**: Could failure disrupt business? | | | | |

**Total Risk Score**: _____

---

### Step 4.2: Risk Level Determination

```
Total Score    Risk Level       Required Actions
-----------    ----------       ----------------
0-5            Low Risk         Standard procedures
6-10           Medium Risk      Additional safeguards required
11-16          High Risk        Leadership approval + enhanced controls
17+            Critical Risk    Consider not using AI / Executive approval
```

---

### Step 4.3: Risk Mitigation

For each Medium or High risk identified, document mitigation:

| Risk | Severity | Mitigation Measure | Owner | Status |
|------|----------|-------------------|-------|--------|
| | | | | |
| | | | | |
| | | | | |

---

## Section 5: Documentation Requirements

### Step 5.1: Required Documentation

Based on your assessment, complete required documentation:

#### For All AI Uses:
- [ ] AI use registered in company inventory
- [ ] Purpose and scope documented
- [ ] Owner assigned

#### For Medium Risk AI Uses (add):
- [ ] Risk assessment completed
- [ ] Mitigation measures documented
- [ ] Oversight procedures defined
- [ ] Review schedule established

#### For High Risk AI Uses (add):
- [ ] Leadership approval documented
- [ ] Privacy impact assessment completed
- [ ] Bias assessment conducted
- [ ] Compliance review completed
- [ ] Incident response plan created
- [ ] Audit schedule defined

---

### Step 5.2: AI Use Registration Form

Complete this for each AI application:

```
AI USE REGISTRATION

Application Name: ________________________________
Vendor/Tool: ________________________________
Department: ________________________________
Owner: ________________________________

Purpose:
________________________________
________________________________

Data Involved:
[ ] Public only  [ ] Business  [ ] Personal  [ ] Sensitive

Risk Level: [ ] Low  [ ] Medium  [ ] High  [ ] Critical

Oversight Level: [ ] Level 1  [ ] Level 2  [ ] Level 3

Approval:
Requester: _________________ Date: _______
Manager: _________________ Date: _______
Security (if required): _________________ Date: _______
Leadership (if required): _________________ Date: _______

Review Schedule: [ ] Monthly  [ ] Quarterly  [ ] Annually

Next Review Date: _______________________
```

---

## Decision Summary Flowchart

```
START
  |
  v
[1] Is this use prohibited? ----YES----> STOP
  |
  NO
  |
  v
[2] Is AI suitable for this task? ----NO----> Consider alternatives
  |
  YES
  |
  v
[3] Do benefits outweigh risks? ----NO----> Reconsider/add safeguards
  |
  YES
  |
  v
[4] Does it involve personal data? ----YES----> Apply privacy safeguards
  |                                              |
  NO                                             |
  |<---------------------------------------------+
  v
[5] Determine risk level
  |
  +-----> Low Risk: Standard procedures
  |
  +-----> Medium Risk: Enhanced controls + documentation
  |
  +-----> High Risk: Leadership approval + full controls
  |
  +-----> Critical: Executive review or don't proceed
  |
  v
[6] Set oversight level (1, 2, or 3)
  |
  v
[7] Complete required documentation
  |
  v
[8] Register AI use in inventory
  |
  v
[9] Set review schedule
  |
  v
PROCEED WITH APPROPRIATE CONTROLS
```

---

## Quick Decision Checklist

Use this for rapid assessment of straightforward cases:

- [ ] Use is not prohibited
- [ ] Task is suitable for AI
- [ ] Benefits justify risks
- [ ] Privacy requirements addressed
- [ ] Oversight level determined
- [ ] Documentation completed
- [ ] AI use registered
- [ ] Review scheduled

**If all boxes checked: Proceed**
**If any box unchecked: Address before proceeding**

---

## Contacts for Guidance

| Question Type | Contact |
|---------------|---------|
| Policy questions | [ROLE/EMAIL] |
| Privacy concerns | [ROLE/EMAIL] |
| Security review | [ROLE/EMAIL] |
| Compliance issues | [ROLE/EMAIL] |
| Technical implementation | [ROLE/EMAIL] |

---

*Document Version: 1.0*
*Last Updated: [DATE]*
*Owner: [NAME/ROLE]*
