# LLM Security, Alignment & Governance Resources [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of research papers, experiments, and resources related to **LLM security and alignment** — including prompt injection, jailbreaks, hallucinations, defenses, governance, and ethical frameworks.  
Organized for reference and study.

**Last Updated:** 2025-09-17

---

## Legend

- ⭐️ **Foundational** — Classic / seminal papers
- 🛡️ **Practical** — Standards, guides, applied resources
- 🧪 **Experimental** — New methods, ongoing research
- 📊 **Dataset/Benchmark** — Data resources, benchmarks
- 🧾 **Survey** — Reviews, surveys, taxonomies

---

## Citation Style Guide

- **arXiv preprints** → `[arXiv:XXXX.XXXXX]`
- **Conference papers** → `[VENUE YEAR]`
- **Journal articles** → `[Journal Name, Year]`
- **Regulations & policy docs** → `[Official Document ID]`
- **GitHub repos** → `[GitHub]`
- **Blogs / Reports** → `[Blog]` / `[Report]`

---

## Table of Contents

- [Prompt Injection & Jailbreaks](#prompt-injection--jailbreaks)
- [Hallucinations & Reliability](#hallucinations--reliability)
- [Defense Strategies](#defense-strategies)
- [Alignment & Safety](#alignment--safety)
- [Governance & Policy](#governance--policy)
- [Surveys & Overviews](#surveys--overviews)
- [Tools & Datasets](#tools--datasets)
- [Privacy & Data Security](#privacy--data-security)
- [Multimodal Security](#multimodal-security)
- [Model Cards (Major AI Labs)](#model-cards-major-ai-labs)
- [Other References](#other-references)

---

## Prompt Injection & Jailbreaks

1. Prompt Injection
- 🧪 [Prompt Injection attack against LLM-integrated Applications](https://arxiv.org/abs/2306.05499) [arXiv:2306.05499] — Defines indirect injection attacks via external data sources; foundational work on LLM application vulnerabilities.
- 🛡️ [Dropbox/llm-security](https://github.com/dropbox/llm-security) [GitHub] — Educational repo with demo code for injection attacks.
- 🛡️ [OWASP Top 10 for LLMs](https://genai.owasp.org/llm-top-10/) [OWASP 2025] — Defines LLM01: Prompt Injection as the top security risk.
- 🧪 [Backdoored Retrievers for Prompt Injection in RAG](https://arxiv.org/abs/2410.14479) [arXiv:2410.14479] — Poisoned retrievers in RAG pipelines enable indirect injection.
- 🧪 [Manipulating LLM Web Agents via Indirect Injection](https://arxiv.org/abs/2507.14799) [arXiv:2507.14799] — Universal HTML triggers to hijack web agents.
- 📊 [WASP: Web Agent Security Benchmark](https://arxiv.org/abs/2504.18575) [arXiv:2504.18575] — Benchmarks agent robustness to indirect injections.

2. Jailbreaking / Adversarial Prompts
- 🧪 [Universal and Transferable Adversarial Attacks on Aligned Language Models (v2)](https://arxiv.org/abs/2307.15043v2) [arXiv:2307.15043v2] — Updated version showing adversarial prompts transferable across multiple aligned LLMs, enabling generalized jailbreak attacks.
- 🧪 [Jailbroken: How Does LLM Safety Training Fail?](https://arxiv.org/abs/2307.02483) [arXiv:2307.02483] — Anthropic analysis of safety training limitations.
- 🧪 [Red Teaming Language Models to Reduce Harms](https://arxiv.org/abs/2209.07858) [arXiv:2209.07858] — Early research on red teaming methods for LLMs.
- 🧪 [Many-shot Jailbreaking](https://www-cdn.anthropic.com/af5633c94ed2beb282f6a53c595eb437e8e7b630/Many_Shot_Jailbreaking__2024_04_02_0936.pdf) [Anthropic 2024] — Shows long multi-shot contexts can bypass safety rules.
- 🧪 [MASTERKEY: Automated Jailbreaking](https://www.ndss-symposium.org/ndss-paper/masterkey-automated-jailbreaking-of-large-language-model-chatbots/) [NDSS 2024] — Automated jailbreak generation.
- 🧪 [White-box Multimodal Jailbreaks](https://arxiv.org/abs/2405.17894) [arXiv:2405.17894] — Vision-language jailbreaks using adversarial inputs.
- 🧪 [Coordinated Prompt-RAG Attacks](https://arxiv.org/abs/2504.07717) [arXiv:2504.07717] — Coordinated poisoning of knowledge bases for RAG.
- 📊 [HarmBench](https://arxiv.org/abs/2402.04249) [arXiv:2402.04249] — Benchmark dataset for harmful content generation.
- 🧪 [Sugar-Coated Poison: Benign Generation Unlocks LLM Jailbreaking](https://arxiv.org/abs/2504.05652) [arXiv:2504.05652] — Stealth jailbreak method hiding malicious intent behind benign reasoning.
- 🧪 [Bypassing Prompt Injection and Jailbreak Detection in LLM Guardrails](https://arxiv.org/abs/2504.11168) [arXiv:2504.11168] — Evasion techniques against commercial guardrail systems.
- 🧪 [Subversion via Focal Points: Investigating Collusion in LLM Monitoring](https://arxiv.org/abs/2507.03010) [arXiv:2507.03010] — Models colluding to bypass monitoring protocols.
- 🧪 [Exploiting Programmatic Behavior of LLMs: Dual-Use Through Standard Security Attacks (v1)](https://arxiv.org/abs/2302.05733v1) [arXiv:2302.05733v1] — Demonstrates how LLMs’ programmatic features can be misused via standard security attack techniques, highlighting dual-use risks and unexpected vulnerabilities.
- 🧪 [Red Teaming the Mind of the Machine](https://arxiv.org/abs/2505.04806) [arXiv:2505.04806] — Systematic evaluation of 1,400+ adversarial prompts across major LLMs.

---

## Hallucinations & Reliability

- 🧾 [A Survey on Hallucination in LLMs](https://arxiv.org/abs/2311.05232) [arXiv:2311.05232] — Taxonomy, principles, and open questions on hallucinations.
- 🧪 [SelfCheckGPT](https://arxiv.org/abs/2303.08896) [arXiv:2303.08896] — Self-verification technique for fact-checking model outputs.
- 🧪 [RARR: Researching and Revising What LMs Say](https://arxiv.org/abs/2210.08726) [arXiv:2210.08726] — Detects and revises hallucinations in generated text.
- 📊 [TruthfulQA](https://arxiv.org/abs/2109.07958) [arXiv:2109.07958] — Benchmark measuring model truthfulness.
- 🧪 [Does More Inference-Time Compute Really Help Robustness?](https://arxiv.org/abs/2507.15974) [arXiv:2507.15974] — Critical examination of inference-time scaling for robustness.

---

## Defense Strategies

- 🧪 [Defending Against Prompt Injection With a Few DefensiveTokens](https://arxiv.org/abs/2507.07974) [arXiv:2507.07974] — Inserts defensive tokens at inference to block attacks.
- 🛡️ [tldrsec/prompt-injection-defenses](https://github.com/tldrsec/prompt-injection-defenses) [GitHub] — Curated list of practical defense strategies.
- 🛡️ [Llama Guard](https://arxiv.org/abs/2312.06674) [arXiv:2312.06674] — Meta's safety classifier for filtering harmful outputs.
- 🧪 [LLMs Can Defend Themselves Against Jailbreaking](https://arxiv.org/abs/2406.05498) [arXiv:2406.05498] — Shadow stack approach for self-defense against jailbreaks.

---

## Alignment & Safety

- ⭐️ [InstructGPT](https://arxiv.org/abs/2203.02155) [arXiv:2203.02155] — Introduced RLHF for instruction-following; foundation for GPT-3.5/4.
- ⭐️ [Constitutional AI](https://arxiv.org/abs/2212.08073) [arXiv:2212.08073] — Anthropic's RLAIF: AI feedback guided by principles.
- ⭐️ [Deep RL from Human Preferences](https://arxiv.org/abs/1706.03741) [arXiv:1706.03741] — Classic work on preference-based reward learning.
- 🧾 [Survey of RLHF](https://arxiv.org/abs/2312.14925) [arXiv:2312.14925] — Comprehensive review of RLHF techniques.
- 🧪 [How Effective is Constitutional AI in Small LLMs?](https://arxiv.org/abs/2503.17365) [arXiv:2503.17365] — Tests CAI on smaller models.
- ⭐️ [ARC Evals → METR (Model Evaluation & Threat Research)](https://evals.alignment.org/) [Report] — Independent evaluations of frontier models (e.g. GPT-4) for potential dangerous capabilities. Formerly the evaluation team of ARC; now spun out as standalone nonprofit.
- 🧪 [Sleeper Agents: Training Deceptive LLMs](https://arxiv.org/abs/2401.05566) [arXiv:2401.05566] — Demonstrates deceptive LLMs persisting through training.
- 🧪 [Language Models Don’t Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting](https://arxiv.org/abs/2305.04388) [arXiv:2305.04388] — Study showing that models’ CoT explanations often don’t reflect the true influences on outputs; can be misled by biasing features not mentioned in the explanation.
- 🧪 [Explicit Vulnerability Generation with LLMs](https://arxiv.org/abs/2507.10054) [arXiv:2507.10054] — Investigation of LLMs generating insecure code when prompted.

---

## Governance & Policy

- 🛡️ [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) [EU 2024] — Core EU regulation; includes requirements for General-Purpose AI (GPAI), risk classifications, transparency, and safety conditions for “high risk” systems.  
- 🛡️ [NIST AI RMF (2023)](https://www.nist.gov/itl/ai-risk-management-framework) — US voluntary framework for identifying, assessing, and managing AI risks over the lifecycle; includes a Generative AI Profile published in mid-2024.  
- 🛡️ [OWASP Top 10 for LLMs](https://genai.owasp.org/llm-top-10/) — Industry standard list of major security threats specific to large language models.  

*Note: Regulatory / policy docs evolve fast — always check latest versions or drafts from official sources.*


---

## Surveys & Overviews

- 🛡️ [Awesome LLM Security](https://github.com/corca-ai/awesome-llm-security) [GitHub] — Community-curated security resources.
- 🛡️ [Awesome Jailbreak on LLMs](https://github.com/yueliu1999/Awesome-Jailbreak-on-LLMs) [GitHub] — Collection of state-of-the-art jailbreak methods.
- 🧾 [Prompt Hacking in LLMs 2024-2025 Literature Review](https://www.rohan-paul.com/p/prompt-hacking-in-llms-2024-2025) [Blog] — Comprehensive review of recent prompt hacking techniques.

---

## Tools & Datasets

- 📊 [sinanw/llm-security-prompt-injection](https://github.com/sinanw/llm-security-prompt-injection) [GitHub] — Dataset & experiments on prompt safety.
- 📊 [Open LLM Security Benchmark (NetSPI)](https://github.com/NetSPI/Open-LLM-Security-Benchmark?utm_source=chatgpt.com) — Benchmark framework evaluating both security (e.g. jailbreak resistance) and usability trade-offs in LLMs.
- 🛡️ [Microsoft Presidio](https://github.com/microsoft/presidio) [GitHub] — Toolkit for PII detection and anonymization.
- 🛡️ [OpenAI Moderation API](https://platform.openai.com/docs/guides/moderation) [Docs] — Content moderation endpoint and examples.
- 🧪 [DefensiveToken Implementation](https://github.com/Sizhe-Chen/DefensiveToken) [GitHub] — Code for defensive token injection method.

---

## Privacy & Data Security

- 🧪 [Extracting Training Data from LLMs](https://arxiv.org/abs/2012.07805) [arXiv:2012.07805] — Shows vulnerability to training data leakage.
- 🧪 [Quantifying Memorization Across Neural LMs](https://arxiv.org/abs/2202.07646) [arXiv:2202.07646] — Quantifies memorization across model scales.

---

## Multimodal Security

- 🧪 [Visual Adversarial Examples Jailbreak Aligned Large Language Models](https://arxiv.org/abs/2306.13213) [arXiv:2306.13213] — Demonstrates that a single visual adversarial example can universally jailbreak aligned VLMs (e.g. MiniGPT-4, InstructBLIP, LLaVA), causing them to comply with harmful instructions they would normally refuse.

---

## 📑 Model Cards (Major AI Labs)

### Anthropic
- 🧪 [Claude 3 Family](https://www.anthropic.com/claude-3-model-card) [Report] — Safety evaluations and model details.
- 🧪 Claude 4 (Opus/Sonnet) — Available via Claude.ai interface.

### OpenAI
- 🛡️ [GPT-4o System Card](https://openai.com/index/gpt-4o-system-card/) [Report] — Multimodal safety considerations.
- 🛡️ [o1 System Card](https://openai.com/index/openai-o1-system-card/) [Report] — Reasoning model safety evaluations.

### Google DeepMind
- 🛡️ [Gemini Family Model Cards](https://ai.google.dev/gemma/docs) [Report] — Safety and capability assessments.

### Meta
- 🛡️ [Llama 3 Model Card](https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md) [Report] — Open-source model safety details.

### Mistral AI
- 🛡️ [Mistral Models Documentation](https://docs.mistral.ai/) [Report] — Model capabilities and safety measures.

---

## Other References

- 🛡️ [Prompt Injection: What Is It and Why It Matters – Simon Willison](https://simonwillison.net/2022/Sep/12/prompt-injection/) [Blog] — Early explanation of prompt injection risks.
- 🧪 [Lakera: Gandalf – The Prompt Injection Game](https://gandalf.lakera.ai/) [Game] — Interactive challenge for prompt injection.
- 🛡️ [PortSwigger: Web LLM Attacks](https://portswigger.net/web-security/llm-attacks) [Blog] — Guide to prompt injection and related attacks.
- 🛡️ [HiddenLayer: Prompt Injection Attacks on LLMs](https://hiddenlayer.com/innovation-hub/prompt-injection-attacks-on-llms/) [Blog] — Comprehensive guide to LLM attacks and defenses.

---

**Maintainer:** 0xSweet  
**License:** CC BY 4.0


