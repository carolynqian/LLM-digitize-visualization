# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an LLM-based scientific plot digitization and evaluation pipeline that compares the accuracy of various language models in extracting numerical data from scientific graphs.

### Core Components

1. **Data Extraction Pipeline** (`pipeline.py`) - Automated digitization using multiple LLM providers (OpenAI, Anthropic, OpenRouter)
2. **Evaluation Framework** (`model_data_dict.py`) - Comparison dataset with ground truth and model extraction results  
3. **Interactive Visualization** (`plot_comparison.py`) - Streamlit web app for exploring results

## Quick Start

### Environment Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment variables
export OPENAI_API_KEY=your_key_here
export ANTHROPIC_API_KEY=your_key_here  
export OPENROUTER_API_KEY=your_key_here
```

### Common Commands

```bash
# Run the digitization pipeline
python pipeline.py --model gpt-4o --graph path/to/image.png --prompt "Extract graph data"

# Launch interactive comparison tool
streamlit run plot_comparison.py
```

## Project Structure

### Directory Organization

- `data/input/images/` - Source scientific plots for digitization
- `data/output/` - Processing results and experiments
- `config/` - Configuration files for models and prompts
- `experiments/` - Research experiments and analysis
- `tests/` - Test cases and validation
- `imgs/` - Legacy image storage (being phased out)

### Configuration Files

- `config/models.yaml` - Model configurations, API endpoints, and cost tracking
- `config/prompts.yaml` - Prompt engineering templates:
  - baseline
  - detailed_cot
  - precise_extraction
  - symbol_focused

### Key Files

- **`pipeline.py`** - Main digitization pipeline with CLI
  - Supports multiple models via direct APIs
  - Base64 image encoding for API transmission
  - **Note**: Implementation incomplete - missing proper model routing

- **`model_data_dict.py`** - Results database with:
  - Metadata (axis ranges, labels)
  - Ground truth coordinates
  - Model extraction results
  - Test cases: Cai7, Polian3, Ross3

- **`plot_comparison.py`** - Streamlit visualization app

## Technical Details

### Data Format
- All coordinate data follows: `{'x': [list], 'y': [list]}`
- Test cases include:
  - Cai7: temperature vs distance
  - Polian3: density vs pressure
  - Ross3: temperature vs pressure

### API Integration
- Direct API support: OpenAI, Anthropic
- OpenRouter as fallback for additional models
- Environment variables required for API keys
- Built-in cost tracking and usage monitoring

## Development Status

### ✅ Completed
1. **Updated imports** in `pipeline.py`:
   - Added: `json`, `yaml`, `datetime`, `pathlib.Path`, `typing`, `re`, `anthropic`

2. **Fixed `call_openai()` function**:
   - Proper message structure with text and image
   - Try/except error handling
   - Structured response format
   - 4000 max_tokens, 0.1 temperature

### 🚧 In Progress
- **`call_anthropic()` function**:
  - Convert from class method
  - Match return structure of `call_openai()`
  - Consistent error handling

### 📋 Pending Tasks
- Fix `run_model()` function for proper API routing
- Add configuration loading from YAML files
- Implement data extraction methods (reasoning and CSV)
- Add output saving functionality
- Create proper command-line interface
- Rewrite Streamlit visualization
- Implement error measurements

## Development Guidelines

### Design Principles
- Keep API functions separate (no classes initially)
- Consistent return format: `{success, model, content, usage, raw_response}`
- Clear error messages for missing API keys
- Include raw response data for debugging

### Claude Code Instructions

#### General Behavior

#### Complex Task Handling
For multi-step tasks (migrations, fixing errors, complex builds):
1. Create a `{task name}_progress.md` checklist
2. Break down into manageable steps
3. Track progress systematically
4. Document decisions and rationale
5. Update file with results and next steps

#### Code Explanation
When presenting implementations:
- Provide brief reasoning and approach
- Explain how changes improve existing code
- Focus on clarity and maintainability

### Workflow Memories
- Update the `task_progress.md` doc whenever you've completed a task. Then ask if you want to `commit` my changes with git.

## Roadmap

### Short-term Goals
- Complete pipeline refactoring
- Enhance model routing and response handling
- Standardize prompt templates

### Long-term Goals
- Advanced error detection and correction
- Interactive visualization features
- Expanded test cases and validation
- Performance optimization
- Cost-effective model selection algorithms