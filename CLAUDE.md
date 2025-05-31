# CLAUDE.md - Working with This Codebase

Guidance for Claude Code when working in this LLM scientific plot digitization project.

## Current State Reality

**What we have now:**
- `pipeline.py` - Basic digitization script (needs completion)
- `model_data_dict.py` - Test dataset with ground truth coordinates
- `plot_comparison.py` - Streamlit visualization app

**What we're building toward:**
- Full modular architecture with `src/core/`, `experiments/`, analysis pipeline (see `instructions.md`)

**Current focus:**
- Get basic `pipeline.py` helper functions working (see `task_progress.md` for details)

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Set up API keys in .env file
# OPENAI_API_KEY=your_key_here
# ANTHROPIC_API_KEY=your_key_here  

# Run current pipeline (basic)
python pipeline.py --model gpt-4o --graph path/to/image.png --prompt "Extract graph data"

# Launch visualization
streamlit run plot_comparison.py
```

## Key Files (Current)

- **`pipeline.py`** - Basic digitization script with CLI
  - Has `_call_openai()` and `_call_anthropic()` helper functions
  - **Current issue**: Missing proper model routing in `run_model()`
  - Returns format: `{success, model, content, usage, raw_response}`

- **`model_data_dict.py`** - Test dataset with ground truth coordinates
  - Test cases: Cai7, Polian3, Ross3 (temperature/pressure/distance plots)
  - Data format: `{'x': [list], 'y': [list]}`

- **`plot_comparison.py`** - Streamlit visualization app

## Current Development Focus

**Priority 1:** Get basic pipeline.py working
- Fix `_call_anthropic()` function
- Fix `run_model()` for proper API routing
- Test with sample images from `data/input/images/batch_1/`

**See `task_progress.md` for detailed sprint work and technical notes.**

## Coding Guidelines

### Design Principles
- Keep API functions separate (no classes initially)
- Consistent return format: `{success, model, content, usage, raw_response}`
- Clear error messages for missing API keys
- Include raw response data for debugging

### Documentation & Workflow
For multi-step tasks:
1. Create a `{task name}_progress.md` checklist
2. Break down into manageable steps
3. Track progress systematically
4. Update `task_progress.md` when completed, then ask about git commit

### Where to Find More
- **`instructions.md`** - Complete project vision, requirements, and target architecture
- **`task_progress.md`** - Current sprint work, technical details, and active development
- **`BUILD_GUIDE.md`** - Step-by-step implementation guide for junior engineers
- **This file** - How to work with the current codebase state