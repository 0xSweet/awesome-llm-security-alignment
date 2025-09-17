# Awesome LLM Security & Alignment [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Curated by 0xSweet

A curated list of research papers, experiments, and resources related to **LLM security and alignment** — including prompt injection, jailbreaks, hallucinations, defenses, and ethical frameworks.  
Organized for reference and study.

---

## Legend

- ⭐️ **Foundational** — Classic / seminal papers
    
- 🛡️ **Practical** — Standards, guides, applied resources
    
- 🧪 **Experimental** — New methods, ongoing research
    
- 📊 **Dataset/Benchmark** — Data resources, benchmarks

- 🧾 **Survey** — Reviews, surveys, taxonomies
    
---

## Table of Contents
- [Prompt Injection & Jailbreaks](#prompt-injection--jailbreaks)
- [Hallucinations & Reliability](#hallucinations--reliability)
- [Defense Strategies](#defense-strategies)
- [Alignment & Safety](#alignment--safety)
- [Surveys & Overviews](#surveys--overviews)
- [Tools & Datasets](#tools--datasets)
- [Other References](#other-references)

---

## Prompt Injection & Jailbreaks
- 🧪 [Prompt Injection attack against LLM (arXiv:2306.05499)](https://arxiv.org/abs/2306.05499)   
  Black-box prompt injection using separator tokens and malicious payloads to override system prompts.
- 🛡️ [Dropbox/llm-security (GitHub)](https://github.com/dropbox/llm-security)   
  Educational repo with demo code for injection attacks.  
- 🧪 [Universal and Transferable Adversarial Attacks on Aligned LMs (arXiv:2307.15043)](https://arxiv.org/abs/2307.15043)  
  Generalization of jailbreak prompts across models.

---

## Hallucinations & Reliability

- 🧾 [A Survey on Hallucination in Large Language Models (arXiv:2311.05232)](https://arxiv.org/abs/2311.05232)  
  Principles, taxonomy, challenges, and open questions on hallucination in LLMs.

---

## Defense Strategies
- 🧪 [DefensiveToken (arXiv:2507.07974)](https://arxiv.org/abs/2507.07974)   
  Novel defense approach using special tokens at test-time.  
- 🛡️ [tldrsec/prompt-injection-defenses (GitHub)](https://github.com/tldrsec/prompt-injection-defenses)   
  Practical compilation of prompt injection defenses.

---

## Alignment & Safety
- 🧪 [Anthropic: Challenges in Red Teaming AI Systems](https://www.anthropic.com/news/challenges-in-red-teaming-ai-systems)   
  Insights from real-world red teaming exercises.  
- 🛡️ [OpenAI: GPT-4 System Card (PDF)](https://cdn.openai.com/papers/gpt-4-system-card.pdf)   
  Details model risks and mitigations.  
- 🛡️ [OWASP Top 10 for LLMs](https://genai.owasp.org/llm-top-10/)  
  Standardized list of LLM-specific security concerns.

---

## Surveys & Overviews
- 🛡️ [Awesome LLM Security (GitHub)](https://github.com/corca-ai/awesome-llm-security)  
  Large-scale community-curated list. Useful for cross-checking.

---


## Tools & Datasets
- 📊 [sinanw/llm-security-prompt-injection (GitHub)](https://github.com/sinanw/llm-security-prompt-injection)  
  Dataset and experiments for classifying malicious vs benign prompts.

---

## Other References
- 🛡️ [Prompt Injection: What Is It and Why It Matters – Simon Willison](https://simonwillison.net/2022/Sep/12/prompt-injection/)  
- 🧪 [Lakera: Gandalf – The Prompt Injection Game](https://gandalf.lakera.ai/)  
- 🛡️ [PortSwigger: Web LLM Attacks](https://portswigger.net/web-security/llm-attacks)  

---



This list is evolving as I read more papers, run experiments, and test defenses.  

<p align="center">
Curated by 0xSweet — MIT License
</p>
