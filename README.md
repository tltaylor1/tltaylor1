<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/profile-header-dark.jpg">
  <img src="assets/profile-header-light.jpg" alt="Terry Taylor, security engineer and architect: cloud security, identity, governance" width="100%">
</picture>

<img src="assets/portrait.png" align="right" width="170" alt="Stylized portrait of Terry">

## Hi, I'm Terry 👋

I'm a security engineer and architect in Seattle who likes building the thing, not just writing the requirement for it.

My background spans infrastructure, cloud platforms, identity, application security, automation, observability, and federal compliance. I've worked from Linux and network engineering through Azure and AWS architecture, spent time handling Severity-A cloud escalations at Microsoft, and have taken two organizations from Cybersecurity Maturity Model Certification (CMMC) gap assessment through successful certification.

A lot of my work sits where **security architecture meets engineering**: turning ambiguous requirements into systems, controls, automation, diagrams, and operating models that people can actually use.

This is also a relatively new GitHub for me. I recently retired an older account I'd had since 2016 that had accumulated a pretty random mix of projects over the years. This one is intentionally more focused on **enterprise security, application security, cloud, identity, and security engineering**.

The projects here explore things like governed coding agents, non-human identity, infrastructure as code, secure application design, policy enforcement, evidence, and the engineering practices behind security controls. I intentionally keep the design decisions, validation mechanisms, and occasional failures visible, not just the finished product.

Most of the larger projects connect through **[control-plane](https://tltaylor1.github.io/control-plane/)**, while the smaller repositories are experiments, demonstrations, diagrams, and study material.

I build primarily with Python, Terraform, Bicep, PowerShell, cloud-native services, and whatever else is useful for making security repeatable.


If you like the program (control-plane) or the main application
(manifest-identity), please give them a ⭐ and let me know!

---

### Start here

Read these in this order. Two are applications, one is the rulebook every repository here is built under, and one is the platform the applications will run on.

| Project | What it does |
|---|---|
| [manifest-identity](https://manifest-identity.github.io/manifest-identity/) | An application for reviewing who has access to what across an organization's cloud accounts and directories. It keeps a record, written by a named person, of what access each identity is allowed to have; it imports what seven providers report and shows every difference between the two records; it runs review campaigns that put each difference in front of the person responsible, one decision at a time. It never changes anything in the systems it reads. |
| [build-doctrine](https://tltaylor1.github.io/build-doctrine/) | The rulebook the program's code is built under: standards for letting an AI coding agent write code a person is responsible for, where each rule names the problem behind it and the check that catches it. It provides a scorer that grades any repository from 0 to 5 on each rule, a vetting tool that reads a dependency before it is adopted, a project template with the checks switched on, and coverage of seven published security frameworks with the gaps listed. |
| [secure-expense-mvp](https://github.com/tltaylor1/secure-expense-mvp) | A small expense submission and approval application built to exercise application security controls end to end. It includes object-level authorization, bounded file handling, transactional audit records, dependency integrity, and security gates in continuous integration. Critical controls are mutation-tested by deliberately weakening them and confirming that the tests fail. |
| [control-plane](https://tltaylor1.github.io/control-plane/) | The platform the applications run on: an AWS estate defined as code, with every security choice explained beside the code that makes it. It will hold the organization and its accounts, a persistent foundation and an ephemeral workload rebuilt daily, identity without stored keys, the image promoted by digest, the cloud's own monitoring, and recovery drilled on a schedule. The plan is written; the code is next. |

### How the projects fit together

| Project | Role |
|---|---|
| manifest-identity | The identity and access review application. |
| secure-expense-mvp | The application security reference implementation. |
| build-doctrine | The shared rules and the checks that hold them. |
| control-plane | The platform the applications will run on, as code, still to build. |

### Looking for something specific?

**Identity and access governance.** Start with manifest-identity, then read its architecture, security model, decisions, and build gates.

**Application security.** Start with secure-expense-mvp, then read its architecture, design decisions, testing, and security in the development lifecycle sections.

**AI-assisted software development.** Start with build-doctrine, then read its standards, enforcement, coverage, and decisions.

**Cloud security reference material.** Start with aws-azure-security-mapping.

**Platform engineering.** Start with control-plane.

### Design and architecture

| Project | What it is |
|---|---|
| [sample-diagrams](https://github.com/tltaylor1/sample-diagrams) | Architecture and process diagrams covering systems, trust boundaries, data flows, security controls, operational workflows, and cross-team handoffs. |

### References and study tools

| Project | What it is |
|---|---|
| [aws-azure-security-mapping](https://github.com/tltaylor1/aws-azure-security-mapping) | Ninety-nine AWS security concepts mapped to their closest Azure counterparts, including the cases where the two platforms have no clean equivalent. |
| [anki-decks](https://github.com/tltaylor1/anki-decks) | Seven maintained study decks, 1,262 cards across PowerShell, Python, Kusto Query Language (KQL), Bicep, cybersecurity, the AWS Security Specialty, and compliance frameworks. Each deck has a plain CSV source so changes can be reviewed in Git, and an automated parity check keeps the source and the Anki package in step. |

---

<p align="center"><b>Certifications</b></p>
<table align="center"><tr>
  <td align="center"><a href="https://www.isc2.org/certifications/cissp" title="ISC2 Certified Information Systems Security Professional"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/badges/cissp-dark.png"><img src="assets/badges/cissp.png" width="96" height="96" alt="CISSP badge"></picture><br><sub>CISSP</sub></a></td>
  <td align="center"><a href="https://learn.microsoft.com/en-us/credentials/certifications/cybersecurity-architect-expert/" title="Microsoft Certified: Cybersecurity Architect Expert"><img src="assets/badges/microsoft-certified-expert.svg" width="96" height="96" alt="Microsoft Certified Expert badge"><br><sub>Cybersecurity Architect Expert</sub></a></td>
  <td align="center"><a href="https://learn.microsoft.com/en-us/credentials/certifications/azure-solutions-architect/" title="Microsoft Certified: Azure Solutions Architect Expert"><img src="assets/badges/microsoft-certified-expert.svg" width="96" height="96" alt="Microsoft Certified Expert badge"><br><sub>Azure Solutions Architect Expert</sub></a></td>
  <td align="center"><a href="https://learn.microsoft.com/en-us/credentials/certifications/m365-administrator-expert/" title="Microsoft 365 Certified: Administrator Expert"><img src="assets/badges/microsoft-certified-expert.svg" width="96" height="96" alt="Microsoft Certified Expert badge"><br><sub>Microsoft 365 Administrator Expert</sub></a></td>
  <td align="center"><a href="https://developer.hashicorp.com/certifications/infrastructure-automation" title="HashiCorp Certified: Terraform Associate"><img src="assets/badges/terraform-associate.png" width="96" height="96" alt="Terraform Associate badge"><br><sub>Terraform Associate</sub></a></td>
  <td align="center"><a href="https://www.cisco.com/site/us/en/learn/training-certifications/certifications/enterprise/ccna/index.html" title="Cisco Certified Network Associate"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/badges/ccna-dark.png"><img src="assets/badges/ccna.png" width="96" height="96" alt="CCNA badge"></picture><br><sub>CCNA</sub></a></td>
</tr></table>

<p align="center"><b>Skills and tools</b></p>
<p align="center">
  <a href="https://tltaylor1.github.io" title="Azure"><img src="https://skillicons.dev/icons?i=azure" width="48" height="48" alt="Azure"></a>
  <a href="https://tltaylor1.github.io" title="Microsoft Entra ID"><img src="assets/icons/entra-id.svg" width="48" height="48" alt="Microsoft Entra ID"></a>
  <a href="https://tltaylor1.github.io" title="AWS"><img src="https://skillicons.dev/icons?i=aws" width="48" height="48" alt="AWS"></a>
  <a href="https://tltaylor1.github.io" title="Terraform"><img src="https://skillicons.dev/icons?i=terraform" width="48" height="48" alt="Terraform"></a>
  <a href="https://tltaylor1.github.io" title="Bicep"><img src="assets/icons/bicep.svg" width="48" height="48" alt="Bicep"></a>
  <a href="https://tltaylor1.github.io" title="Salt"><img src="https://cdn.simpleicons.org/saltproject/57BCAD" width="48" height="48" alt="Salt"></a>
  <a href="https://tltaylor1.github.io" title="Kubernetes"><img src="https://skillicons.dev/icons?i=kubernetes" width="48" height="48" alt="Kubernetes"></a>
  <a href="https://tltaylor1.github.io" title="Docker"><img src="https://skillicons.dev/icons?i=docker" width="48" height="48" alt="Docker"></a>
</p>
<p align="center">
  <a href="https://tltaylor1.github.io" title="Python"><img src="https://skillicons.dev/icons?i=py" width="48" height="48" alt="Python"></a>
  <a href="https://tltaylor1.github.io" title="PowerShell"><img src="https://skillicons.dev/icons?i=powershell" width="48" height="48" alt="PowerShell"></a>
  <a href="https://tltaylor1.github.io" title="Bash"><img src="https://skillicons.dev/icons?i=bash" width="48" height="48" alt="Bash"></a>
  <a href="https://tltaylor1.github.io" title="FastAPI"><img src="https://skillicons.dev/icons?i=fastapi" width="48" height="48" alt="FastAPI"></a>
  <a href="https://tltaylor1.github.io" title="PostgreSQL"><img src="https://skillicons.dev/icons?i=postgres" width="48" height="48" alt="PostgreSQL"></a>
  <a href="https://tltaylor1.github.io" title="Linux"><img src="https://skillicons.dev/icons?i=linux" width="48" height="48" alt="Linux"></a>
  <a href="https://tltaylor1.github.io" title="GitHub Actions"><img src="https://skillicons.dev/icons?i=githubactions" width="48" height="48" alt="GitHub Actions"></a>
</p>

---

### Areas of focus

Cloud and identity security, application security, infrastructure as code, continuous integration and continuous delivery security, detection engineering, security automation, and regulated environments.

---

Across these projects are implementation plans, architecture decisions,
rejected alternatives, automated tests, security controls, failure
records, and the checks added afterward.
