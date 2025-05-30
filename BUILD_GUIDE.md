# Complete Build Guide for Junior Engineer

## Current Implementation Status

### ✅ **What's Actually Working:**
- **`config/models.yaml`** - Complete, ready to use
- **`config/prompts.yaml`** - Complete, 4 different extraction strategies  
- **`tests/test_functions.py`** - Comprehensive test suite for API functions
- **`pipeline.py`** - Core API functions work (`_call_openai()`, `_call_anthropic()`)

### ⚠️ **What's Partially Implemented:**
- **`pipeline.py`** - Missing main() integration (lines 175-176 incomplete)
- **`src/visualization/streamlit_app.py`** - Works but imports missing `model_data_dict`
- **Data structure** - Configured but no actual ground truth data files

### ❌ **What's Missing:**
- **`requirements.txt`** - Incomplete (missing API clients, yaml, dotenv)
- **`src/core/`** directory - Empty, needs all modules
- **`.env` file** - Needs creation
- **Ground truth data** - CSV files in `data/input/ground_truth/`

---

## Step-by-Step Build Plan

### **Phase 1: Environment Setup (30 minutes)**

**1. Fix requirements.txt**
```bash
# Current requirements.txt only has 4 basic packages
# Need to add:
openai
anthropic  
python-dotenv
PyYAML
opencv-python
scipy
plotly
pydantic
requests
```

**2. Create .env file**
```bash
# Create in project root
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
OPENROUTER_API_KEY=your_openrouter_key_here
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

### **Phase 2: Fix Core Pipeline (45 minutes)**

**4. Complete pipeline.py main() function**
```python
# pipeline.py:175-176 currently incomplete
# Need to add:
def main():
    load_dotenv()
    model, graph, prompt = get_user_inputs()
    
    result = run_model(model, graph, prompt)
    
    if result['success']:
        print(f"✅ Success! Model: {result['model']}")
        print(f"Content: {result['content'][:200]}...")
        print(f"Usage: {result['usage']}")
    else:
        print(f"❌ Error: {result['error']}")
```

**5. Fix Anthropic model mapping**
```python
# pipeline.py:124 - hardcoded model name, should use config
# Change from: model="claude-3-sonnet-20240229"
# To: model="claude-3-5-sonnet-20241022"  # Match config
```

### **Phase 3: Test Basic Functionality (30 minutes)**

**6. Test with existing test suite**
```bash
python tests/test_functions.py
```

**7. Test end-to-end pipeline**
```bash
python pipeline.py --model gpt-4o --graph data/input/images/batch_1/Cai7_graph_forVis.png --prompt "Extract graph data"
```

### **Phase 4: Create Missing Core Modules (2-3 hours)**

**8. Create `src/core/llm_interface.py`**
```python
# Unified interface that:
# - Loads config from models.yaml
# - Routes to cheapest API (direct vs OpenRouter)
# - Handles rate limiting and retries
# - Tracks costs
```

**9. Create `src/core/data_processor.py`**
```python
# Functions to:
# - Parse "REASONING:" and "CSV_DATA:" sections from LLM responses
# - Validate extracted coordinates
# - Handle multiple datasets (different symbols)
# - Convert to structured format
```

**10. Create `src/core/error_calculator.py`**
```python
# Implement robust MSE with Hungarian algorithm
# - Point-level accuracy
# - Dataset-level accuracy  
# - Visual similarity metrics
```

### **Phase 5: Data Structure (1-2 hours)**

**11. Create ground truth data files**
```bash
# Need to recover model_data_dict.py and extract ground truth:
git show cc930b4:model_data_dict.py > temp_model_data.py

# Then manually create:
# data/input/ground_truth/Cai7_ground_truth.csv
# data/input/ground_truth/Polian3_ground_truth.csv  
# data/input/ground_truth/Ross3_ground_truth.csv
```

**12. Fix Streamlit app**
```python
# src/visualization/streamlit_app.py:7
# Remove: from model_data_dict import all_model_data
# Replace with: loading from structured data files
```

### **Phase 6: Testing & Integration (1 hour)**

**13. Create batch processing**
```bash
# Create experiments/run_single_test.py
# Create experiments/run_batch.py
```

**14. End-to-end testing**
```bash
streamlit run src/visualization/streamlit_app.py
```

---

## Critical Files to Modify/Add

### **Immediate Priority (Fix broken functionality):**

1. **`requirements.txt`** - Add missing dependencies
2. **`pipeline.py:175-176`** - Complete main() function  
3. **`.env`** - Create with API key placeholders
4. **`pipeline.py:124`** - Fix hardcoded Anthropic model name

### **Medium Priority (Core functionality):**

5. **`src/core/llm_interface.py`** - NEW FILE - Unified API handler
6. **`src/core/data_processor.py`** - NEW FILE - Response parsing
7. **Ground truth CSV files** - Extract from git history
8. **`src/visualization/streamlit_app.py`** - Fix import error

### **Lower Priority (Advanced features):**

9. **`src/core/error_calculator.py`** - NEW FILE - Error metrics
10. **`experiments/run_single_test.py`** - NEW FILE - Single test runner
11. **`experiments/run_batch.py`** - NEW FILE - Batch processing

---

## Detailed Implementation Notes

### **Current File Analysis**

**Working Files:**
- `config/models.yaml` - Well-structured with cost tracking, direct API priority
- `config/prompts.yaml` - 4 strategies: baseline, detailed_cot, precise_extraction, symbol_focused
- `tests/test_functions.py` - Comprehensive test suite with proper error handling
- `pipeline.py` API functions - Both `_call_openai()` and `_call_anthropic()` are complete

**Broken/Incomplete:**
- `pipeline.py:175-176` - Main function literally stops mid-execution
- `requirements.txt` - Missing 8+ critical dependencies
- `src/visualization/streamlit_app.py:7` - Imports deleted file `model_data_dict`
- No ground truth data files exist

### **Quick Win Path (1 hour to working pipeline):**

1. **Fix requirements.txt** (5 minutes)
2. **Complete pipeline.py main()** (15 minutes)  
3. **Create .env file** (5 minutes)
4. **Test end-to-end** (35 minutes)

### **Architecture Notes**

**Target Structure (from instructions.md):**
```
src/core/
├── llm_interface.py    # API routing, cost optimization
├── data_processor.py   # Response parsing, validation  
├── error_calculator.py # Hungarian algorithm, MSE metrics
└── analyzer.py         # Meta-analysis integration
```

**Current State:**
- All `src/core/` files missing
- Basic functionality exists in `pipeline.py` but needs modularization
- Configuration system ready for integration

### **Data Recovery Process**

The `model_data_dict.py` file was deleted but is recoverable:
```bash
git show cc930b4:model_data_dict.py
```

Contains ground truth data for:
- Cai7 (temperature/pressure plot)
- Polian3 (distance plot) 
- Ross3 (scientific measurement plot)

Need to extract this into structured CSV files in `data/input/ground_truth/`.

---

## Success Criteria

**Phase 1 Complete:** Basic pipeline runs end-to-end
**Phase 2 Complete:** Modular architecture with config integration
**Phase 3 Complete:** Batch processing and error metrics
**Phase 4 Complete:** Interactive visualization working

**Final Goal:** Research-ready pipeline for systematic LLM evaluation on scientific plot digitization.

---

## Notes for Implementation

- **Test images available:** 3 scientific plots in `data/input/images/batch_1/`
- **Configuration ready:** Models and prompts fully configured
- **Foundation solid:** Core API functions work and are tested
- **Main blocker:** Integration layer incomplete (pipeline.py main function)

The project has excellent bones - just needs the connecting tissue to become functional.