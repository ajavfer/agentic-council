# Agentic Council: Dialectical Multi-Agent Deliberation

A structured, multi-agent evaluation framework that stress-tests strategic proposals, investment theses, and technical architectures through polarized dialectical debate.

Built as an open-source technical reference for [HUMXUS](https://www.humxus.com), Agentic Council demonstrates how to replace unstructured chat with a bounded 3-agent deliberation loop:

1. **The Strategic Innovator (*Thesis*):** Explores theoretical potential, first-principles upside, market hypotheses, and scaling opportunities.
2. **The Pragmatic Skeptic (*Antithesis*):** Scrutinizes unit economics, operational risks, validation gaps, and over-engineering.
3. **The Executive Chairman (*Synthesis*):** Impartially identifies areas of agreement, highlights critical blind spots, and prescribes a definitive decision with a prioritized 3-to-5 step roadmap.

---

## Architecture

`council.py` is a high-throughput, rate-limit-conscious pipeline built on `google-genai` and `asyncio.gather`. It features typed Pydantic output schemas and an automatic multi-model failover cascade to protect against transient 503 and 429 errors.

---

## Repository Structure

```text
agentic-council/
├── README.md
├── requirements.txt
├── .env.example           # Template for environment variables
├── .gitignore
├── council.py              # Async pipeline with Pydantic schemas & failover
├── tests/                  # Pytest suite (no API calls required)
└── reports/                # Generated council reports (gitignored)
```

---

## Installation

```bash
git clone https://github.com/ajavfer/agentic-council.git
cd agentic-council
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file in the project root (or copy `.env.example`):

```env
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL_BASIC=gemini-3.8-flash
```

---

## Usage

The script supports analyzing text prompts directly or extracting context from attached documents (`.pdf`, `.docx`, `.txt`, `.md`). Reports are automatically saved to `reports/`.

```bash
# Basic evaluation prompt
python council.py "Should we open-source our core proprietary algorithms?"

# Evaluating an attached document
python council.py "Evaluate this product roadmap" --file proposal.pdf --output roadmap_review.md

# Specifying an alternative model
python council.py "Critique our enterprise pricing strategy" --model gemini-3.6-flash
```

### Supported Models

- `gemini-3.8-flash` (Default: optimized for agents and complex reasoning)
- `gemini-4-hydrogen` (Flagship frontier reasoning)
- `gemini-3.6-flash` (Balanced multi-modal and general agentic tasks)
- `gemini-3.5-flash-lite` (High-throughput execution)
- `gemini-3.1-flash-lite` (Cost-efficient lightweight execution)

---

## Supported Context Formats

- Markdown & Plain Text: `.md`, `.txt`
- PDF Documents: `.pdf` (via `pypdf`)
- Word Documents: `.docx` (via `python-docx`)

---

## Report Structure

Generated reports follow an executive-ready structure:

- **Original Objective & Context:** Plain-language problem statement.
- **Divergent Perspectives:** Summary of the Innovator's upside case versus the Skeptic's risk analysis.
- **Chairman's Evaluation & Consensus:** Clear breakdown of common ground and critical unresolved clashes.
- **Definitive Recommendation:** Decisive strategic direction (rejecting vague compromise).
- **Actionable Next Steps:** Prioritized 3-to-5 step implementation roadmap.

---

## Testing

The test suite in `tests/` covers file extraction, the model fallback cascade, and output schema validation. No Gemini API key or network access required.

```bash
python -m pytest tests/ -v
```

---

## About HUMXUS

This project is maintained by [HUMXUS](https://www.humxus.com/), an independent AI advisory practice by Javier Ferrer focused on enterprise AI governance, due diligence, and vendor-neutral decision architectures.
