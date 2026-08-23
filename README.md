## Terry Taylor

I am a security engineer and architect in Seattle, working in cloud and identity
security for regulated and federal environments. I have taken two organizations
from gap assessment through Cybersecurity Maturity Model Certification. Most of
the repositories below form [control-plane](https://tltaylor1.github.io),
a security engineering program built in public with a governed coding
agent: every change agent-proposed, human-reviewed, signed, and
gated, with the decisions and the failure record kept on purpose.
The diagrams repository stands on its own.

### The program

| Repository | What it is, and what it proves | The evidence |
|---|---|---|
| [role-call](https://github.com/tltaylor1/role-call) | Inventory and governance for non-human identities, the roles, service accounts, and access keys nobody offboards. State derives from observed history rather than being stored, and the tool amplifies a human decision rather than acting on its own. Complete through its version one scope. | [Releases with build provenance](https://github.com/tltaylor1/role-call/releases), verifiable against the public transparency log; runs from a fresh clone on Compose or a hardened local Kubernetes cluster |
| [control-plane](https://tltaylor1.github.io) | The program the repositories form: phases fixed before building, monitoring and recovery documented with drills that expire, and the agent governed by gates it cannot route around. | [The site](https://tltaylor1.github.io), with the phase plan published before the work |
| [build-guidelines](https://github.com/tltaylor1/build-guidelines) | The standards every project here starts from, organized by layer. Each rule names what enforces it and the incident that produced it; what no tool can check is named as a human attestation with an expiry. | [The enforcement mapping](https://github.com/tltaylor1/build-guidelines/blob/main/ENFORCEMENT.md), where every rule states its mechanism or is labeled a hope |
| [secure-expense-mvp](https://github.com/tltaylor1/secure-expense-mvp) | A small expense application, finished and hardened: object-level authorization, tokenized values, audit logging, a security-gated pipeline. Complete on purpose. | Mutation-tested: controls are proven by removing them and watching the suite fail |

### Standing apart

| Repository | What it is |
|---|---|
| [sample-diagrams](https://github.com/tltaylor1/sample-diagrams) | Hand-drawn architecture and process diagrams, drawn in Visio, kept as illustration-only examples of design work |

CISSP · Terraform Associate · CCNA · Microsoft Expert x3

[![Toolset](https://skillicons.dev/icons?i=azure,aws,terraform,kubernetes,docker,py,fastapi,postgres,linux,bash,powershell,githubactions&perline=12)](https://tltaylor1.github.io)
