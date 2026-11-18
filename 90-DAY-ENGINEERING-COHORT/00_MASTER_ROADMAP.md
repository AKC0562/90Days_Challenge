# 00_MASTER_ROADMAP.md

## Model Orchestration System (FREE models only)

**Orchestrator:** Nemotron 3.5 Super (`opencode/nemotron-3.5-super-vl-free`, FREE, vision-language) — coordinates all specialists, synthesizes findings, adjudicates disagreements.

### Available FREE models (verified via model inventory, cost = 0)
| # | Model ID | Name | Notes |
|---|----------|------|-------|
| 1 | `opencode/nemotron-3.5-super-vl-free` | Nemotron 3.5 Super VL Free | Orchestrator (me). Strong general reasoning + VL. |
| 2 | `opencode/deepseek-v4.1-flash-free` | DeepSeek V4.1 Flash Free | Known for code/reasoning strength. Good for implementation. |
| 3 | `opencode/flint-40b-free` | Flint 40B Free | 40B parameter, free. Generalist. |
| 4 | `opencode/hy4-flash-free` | Hy4 flash Free | Free. Generalist. |
| 5 | `opencode/iceman-free` | Iceman Free | Free. Generalist. |
| 6 | `opencode/inkling-2-small-free` | Inkling 2 Small Free | Free, small. Lightweight tasks. |
| 7 | `opencode/longcat-2.5-free` | LongCat 2.5 Free | Free. Generalist. |
| 8 | `opencode/beam-free` | Beam Free | Free. Generalist. |
| 9 | `opencode/mimo-v2.6-flash-free` | MiMo-V2.6-Flash Free | Free. Generalist. |
| 10 | `opencode/big-pickle` | Big Pickle | Free. Generalist. |

### PAID models (NOT used without explicit permission)
gpt-6.2-sol/astra, gemini-4-hydrogen, muse-ember-1.0, claude-fable-5-2, claude-haiku/sonnet/opus-5.5, mistral-large-4, grok-4.7/build-0.1, gemini-3.x, glm-5.x, qwen3.8-flash, kimi-k3/k2.7-code, minimax-m3, deepseek-v4-pro, gpt-5.x family.

### Capability note
Verified data available per model: ID, name, cost, status, variants, release date. **Detailed context size, tool-calling, and reasoning capability are not documented in the inventory.** I will not invent these. Where subagent model assignment is unreliable, I (Nemotron) perform the specialist role myself and record the limitation.

### Specialist Instructor → Model Assignment (FREE only)
| Specialist | Role | Assigned Model | Confidence |
|------------|------|----------------|------------|
| Orchestrator / CTO | Coordination, synthesis, adjudication | nemotron-3.5-super-vl-free (me) | High |
| CS Professor | OS, networking, architecture, algorithms | nemotron-3.5-super-vl-free (me) | High |
| Senior Full Stack Architect | JS, TS, React, Next.js, Node, Express, architecture | deepseek-v4.1-flash-free | Medium* |
| Python Instructor | Python, OOP, FastAPI, data engineering | deepseek-v4.1-flash-free | Medium* |
| Mathematics & Statistics Professor | Linear algebra, calculus, probability, stats | nemotron-3.5-super-vl-free (me) | High |
| ML Scientist | Data science, classical ML, scikit-learn | flint-40b-free | Medium* |
| Deep Learning Engineer | Neural nets, PyTorch, TF, Transformers | flint-40b-free | Medium* |
| LLM & GenAI Engineer | LLM arch, fine-tuning, LoRA, quantization | nemotron-3.5-super-vl-free (me) | High |
| RAG & Agentic AI Architect | RAG, vector DBs, LangGraph, MCP, agents | deepseek-v4.1-flash-free | Medium* |
| DevOps & Cloud Architect | Linux, Docker, AWS, CI/CD, K8s, Terraform | nemotron-3.5-super-vl-free (me) | High |
| Principal Code Reviewer | Bugs, security, architecture, production readiness | deepseek-v4.1-flash-free | Medium* |
| Examiner & Interviewer | Quizzes, DSA, interviews, assessments | nemotron-3.5-super-vl-free (me) | High |

\*Medium = model free but detailed capability unverified; I will verify by using it and fall back to Nemotron if weak.

**Rule:** Never use paid models without explicit student permission. Never accept an answer because multiple models agree. Have Nemotron synthesize and adjudicate.

---

## Complete Curriculum (All 23 Modules preserved + AI/ML/LLM expansions)

See detailed module list in the cohort syllabus. All 23 modules retained:
1. How Software Works
2. Developer Toolkit
3. HTML, CSS and Frontend Foundations
4. JavaScript
5. TypeScript
6. Backend Engineering
7. Database Engineering
8. Modern Frontend Engineering
9. Real-Time Systems
10. DevOps and Cloud Engineering
11. Python Engineering
12. Mathematics for AI
13. Data Science
14. Machine Learning
15. Deep Learning and Neural Networks
16. NLP and Transformers
17. LLM Engineering
18. RAG and Vector Databases
19. Agentic AI and Multi-Agent Systems
20. Multimodal AI
21. AI Production Engineering
22. Spec-Driven Development
23. Forward Deployed Engineering

---

## 90-Day Structure (3 Levels)

### LEVEL 1 — Days 1–30: Full Stack Software Engineering
**Primary Project:** LeadFlow CRM SaaS
Deliverables: Responsive frontend, Auth, RBAC, Production REST APIs, DB architecture, File uploads, Admin dashboard, Testing, Deployment, Documentation.

### LEVEL 2 — Days 31–60: Python, Math, ML, DL and LLM Foundations
**Primary Project:** KnowBase AI
Deliverables: Python backend, Data pipeline, ML model, Neural network, LLM integration, Document ingestion, Embeddings, Vector DB, RAG pipeline, AI chat interface, Evaluation.

### LEVEL 3 — Days 61–90: Advanced AI Engineering and FDE
**Primary Project:** DeployMate AI
Deliverables: Multi-agent workflows, LangGraph, MCP integrations, Advanced RAG, AI evaluation, Model routing, Redis + background jobs, Docker, Cloud deployment, Monitoring, Security, Production documentation, Client demo.

---

## Day-by-Day Execution Plan

Each day: Theory → Guided Implementation → Independent Coding → Code Review → Production Lab → Test & Interview → Memory Update.

### LEVEL 1 — Full Stack (Days 1–30)

**Week 1: How Software Works + Developer Toolkit**
| Day | Topics | Deliverable |
|-----|--------|-------------|
| 1 | Binary/char encoding, compilers vs interpreters, client-server, OSI/TCP-IP | Notes + mini explanation |
| 2 | DNS (records, root/TLD/authoritative/recursive), TCP vs UDP, IP/subnetting, ports/sockets | DNS lookup lab (nslookup/dig) |
| 3 | HTTP request-response, methods, status codes, HTTPS/TLS, processes vs threads | HTTP lab with curl |
| 4 | CPU/RAM/stack/heap, memory mgmt, OS, concurrency vs parallelism | Memory diagram + notes |
| 5 | Terminal/shell, Git & GitHub, branches/merges, PRs | Git init, repo, first branch |
| 6 | IDE/VS Code/OpenCode setup, debugging tools, Linux fundamentals | Dev environment ready |
| 7 | **Weekly Exam:** DSA basics + Git + networking quiz | Assessment score recorded |

**Week 2: HTML/CSS + Frontend Foundations**
| Day | Topics | Deliverable |
|-----|--------|-------------|
| 8 | HTML5, semantic tags, forms, validation, accessibility/WCAG | Semantic HTML page |
| 9 | CSS box model, selectors, specificity, cascade, Flexbox | Flexbox layout |
| 10 | CSS Grid, responsive design, media queries, mobile-first | Responsive page |
| 11 | Animations, transitions, Tailwind CSS, browser DevTools | Tailwind UI component |
| 12 | Browser rendering pipeline, critical rendering path, Core Web Vitals, SEO, PWA | Performance audit |
| 13 | CSS architecture, design tokens, revision + lab | Styled component library |
| 14 | **Weekly Exam:** HTML/CSS + frontend quiz + code review | Assessment score |

**Week 3: JavaScript Fundamentals**
| Day | Topics | Deliverable |
|-----|--------|-------------|
| 15 | JS data types, operators, conditionals, loops | JS basics lab |
| 16 | Functions, scope, closures (review), IIFE, modules | Closure lab |
| 17 | Objects, arrays, array methods, destructuring, spread/rest | Data manipulation lab |
| 18 | ES6+ (classes, OOP, prototypes), promises, async/await | Async JS lab |
| 19 | DOM, events, event delegation, Fetch, CORS | DOM interaction lab |
| 20 | Execution context, call stack, event loop, micro/macrotask queues | Event loop visualization |
| 21 | **Weekly Exam:** JS fundamentals + event loop quiz + debugging challenge | Assessment score |

**Week 4: Advanced JS + TypeScript + Backend Intro**
| Day | Topics | Deliverable |
|-----|--------|-------------|
| 22 | Memory & GC, deep/shallow copy, immutability, functional programming | FP lab |
| 23 | Design patterns (module, factory, observer), error handling, testing | Pattern lab + unit tests |
| 24 | TS basic/advanced types, interfaces, aliases, generics | TS types lab |
| 25 | TS conditional/mapped/utility types, narrowing, inference, tsconfig, ESLint/Prettier | TS config + type-safe lab |
| 26 | Node.js HTTP, Express, middleware, REST, routing | Express server |
| 27 | Zod validation, file handling, Multer, auth basics, logging/monitoring | Validated API |
| 28 | REST API design, status codes, idempotency, versioning | API spec + routes |
| 29 | LeadFlow CRM: project setup, DB schema, auth, RBAC | Project scaffold |
| 30 | **Level 1 Final Exam:** Full-stack practical + system design + code review | Final assessment |

---

### LEVEL 2 — Python / Math / ML / DL / LLM (Days 31–60)

**Week 5: Python Engineering + Mathematics**
| Day | Topics | Deliverable |
|-----|--------|-------------|
| 31 | Python syntax, data types, conditions, loops | Python basics lab |
| 32 | Functions, modules/packages, OOP, inheritance/polymorphism | OOP lab |
| 33 | Decorators, generators, iterators, context managers, exceptions | Decorator + generator lab |
| 34 | Type hints, Pydantic, asyncio, threading/multiprocessing | Async Python lab |
| 35 | Virtual envs, pip, pytest, SQLAlchemy, FastAPI intro | FastAPI app |
| 36 | Arithmetic/algebra, functions/graphs, vectors/matrices | Math lab (NumPy) |
| 37 | Matrix mult, linear transformations, eigen, derivatives, gradients | Calculus/linear algebra lab |
| 38 | Probability, Bayes, distributions, mean/var/std, inference | Stats lab |
| 39 | Hypothesis testing, correlation/covariance, revision | Stats lab |
| 40 | **Weekly Exam:** Python + math quiz + coding test | Assessment |

**Week 6: Data Science + Classical ML**
| Day | Topics | Deliverable |
|-----|--------|-------------|
| 41 | NumPy, Pandas, data cleaning, missing values | Data cleaning pipeline |
| 42 | Matplotlib/Seaborn, EDA, visualization | EDA notebook |
| 43 | Feature engineering, preprocessing, train/val/test split, data leakage | Feature pipeline |
| 44 | ML intro, supervised/unsupervised, linear/logistic regression | Regression lab |
| 45 | Decision trees, random forests, gradient boosting, XGBoost | Ensemble lab |
| 46 | KNN, SVM, Naive Bayes, K-means, PCA | Classification/clustering lab |
| 47 | Cross-validation, hyperparameter tuning, bias-variance, over/underfitting | Tuning lab |
| 48 | Precision/recall/F1/ROC-AUC, scikit-learn pipelines, model deployment | Evaluation + pipeline |
| 49 | Revision + weak areas | Revision lab |
| 50 | **Weekly Exam:** ML practical + math + Python | Assessment |

**Week 7: Deep Learning + NLP + Transformers**
| Day | Topics | Deliverable |
|-----|--------|-------------|
| 51 | Neuron, perceptron, layers, activation, loss, forward prop | NN from scratch (NumPy) |
| 52 | Backprop, gradient descent, SGD, Adam, learning rate, regularization | Training lab |
| 53 | Dropout, batch norm, CNN | CNN lab (PyTorch) |
| 54 | RNN, LSTM, GRU, attention | Sequence lab (PyTorch) |
| 55 | Transformers, self-attention, multi-head, positional encoding | Transformer lab |
| 56 | BERT/GPT concepts, transfer learning, fine-tuning, HF ecosystem | HF model lab |
| 57 | Text preprocessing, tokenization, embeddings, Word2Vec | Tokenization lab |
| 58 | Encoder/decoder, model inference, evaluation | Inference lab |
| 59 | Revision + weak areas | Revision |
| 60 | **Level 2 Final Exam:** DL + NLP practical + math | Assessment |

---

### LEVEL 3 — LLM / RAG / Agents / FDE (Days 61–90)

**Week 8: LLM Engineering + RAG**
| Day | Topics | Deliverable |
|-----|--------|-------------|
| 61 | How LLMs work, tokens/tokenizers, context windows, transformer internals | Tokenizer lab |
| 62 | Pretraining, instruction tuning, SFT, RLHF concepts | SFT concepts |
| 63 | Prompt engineering, system prompts, structured outputs | Prompt lab |
| 64 | Function/tool calling, streaming, model APIs | Tool calling lab |
| 65 | Open-source models, quantization INT8/INT4, GGUF | Quantization lab |
| 66 | LoRA, QLoRA, PEFT, fine-tuning | PEFT lab |
| 67 | Inference optimization, KV cache, batching, model serving | Serving lab |
| 68 | Embeddings, vector similarity, cosine, vector indexing | Embedding lab |
| 69 | Chunking strategies, document ingestion, metadata filtering | Ingestion pipeline |
| 70 | **Weekly Exam:** LLM + RAG concepts + lab | Assessment |

**Week 9: Vector DBs + Advanced RAG + Agents**
| Day | Topics | Deliverable |
|-----|--------|-------------|
| 71 | FAISS, Chroma, Qdrant, pgvector | Vector DB lab |
| 72 | Semantic search, hybrid search, BM25, reranking | Hybrid search lab |
| 73 | RAG evaluation, retrieval eval, hallucination reduction | RAG eval lab |
| 74 | Advanced RAG: contextual retrieval, query rewriting, multi-query | Advanced RAG lab |
| 75 | GraphRAG fundamentals, knowledge graphs | GraphRAG lab |
| 76 | Agent architecture, agent loops, planning/execution | Agent lab |
| 77 | Memory systems, state management, LangChain/LangGraph | LangGraph agent |
| 78 | MCP, multi-agent orchestration, human-in-the-loop | MCP + multi-agent |
| 79 | Agent evaluation, reliability, sandboxing, tool security | Agent security lab |
| 80 | **Weekly Exam:** Agent + MCP + advanced RAG | Assessment |

**Week 10: Multimodal + AI Production + FDE**
| Day | Topics | Deliverable |
|-----|--------|-------------|
| 81 | VLM, image understanding, OCR, STT/TTS | Multimodal lab |
| 82 | Audio/video processing, multimodal embeddings, image/doc RAG | Multimodal RAG |
| 83 | FastAPI AI backend, Node+Python integration, AI SDK | AI API |
| 84 | Streaming AI apps, model gateway, observability (Langfuse/MLflow) | Observability |
| 85 | Auth, guardrails, PII protection, prompt injection, rate limits | Security lab |
| 86 | Cost tracking, token budgeting, caching, fallback, load testing | Cost/perf lab |
| 87 | Docker, cloud deployment, monitoring, disaster recovery | Deploy lab |
| 88 | FDE: client discovery, requirements, rapid prototyping, API integration | FDE simulation |
| 89 | DeployMate AI: multi-agent workflow, Redis jobs, Docker, cloud deploy | Capstone build |
| 90 | **Final Capstone Review:** Full-stack + ML + LLM/RAG + agent + FDE client simulation + portfolio review | Final assessment |

---

## Mastery Score Scale
- 0–39: Not understood
- 40–59: Beginner
- 60–74: Developing
- 75–89: Competent
- 90–100: Strong mastery

**Rule:** A score is not proof of mastery without practical evidence (working code).

---

## Dependencies & Difficult Topics
- **Prerequisite chain:** HTML/CSS → JS → TS → Node/Express → React/Next.js → DB → Auth/Deploy. Never skip.
- **Difficult topics (extra revision blocks):** Event loop, closures, async/await, TS generics, backprop, transformers, LoRA/QLoRA, RAG eval, LangGraph agents, MCP, Kubernetes/Terraform.
- **Project milestones:** LeadFlow CRM (Day 30), KnowBase AI (Day 60), DeployMate AI (Day 90).

---

## Technology Decisions (to be recorded in 10_TECHNOLOGY_DECISIONS.md)
Pending. Technologies selected per module with justification (engineering value, not trends).

---

## Status
- Roadmap drafted. **Awaiting student approval.**
- After approval: create remaining memory files (03–11, 13), then begin DAY 1.
