# Task Progress & Working Notes

## Current Sprint: Helper Function Testing & Implementation

### ✅ Completed Tasks

**2025-05-30 - Ship Command Creation**
   - Created `/ship` command for autonomous task completion workflow
   - Added `.claude/commands/ship.md` with instructions for documentation updates and git workflow
   - (Note: I thought that I created the ship command earlier, but it's entirely lost)
   - Status: Complete ✅
1. **Updated imports in `pipeline.py`**
   - Added: `json`, `yaml`, `datetime`, `pathlib.Path`, `typing`, `re`, `anthropic`
   - Status: Complete ✅

2. **Fixed naming conventions in `pipeline.py`**
   - `get_userInputs()` → `get_user_inputs()` (snake_case)
   - `call_openai()` → `_call_openai()` (mark as internal)
   - `_call_anthropic()` → kept as internal
   - Removed incomplete `run_gpt4o()` function
   - Status: Complete ✅

3. **Fixed critical bugs in pipeline**
   - Fixed `image_path` undefined variable → `graph`
   - Fixed parameter passing in function calls
   - Fixed incomplete `_call_anthropic` call
   - Added proper return statements and error handling
   - Status: Complete ✅

4. **Documentation system reorganization**
   - Restructured CLAUDE.md from 161 to 75 lines (53% reduction)
   - Established clear file roles: instructions.md (vision), task_progress.md (sprint), CLAUDE.md (current state)
   - Designed `/ship` workflow command for automated task completion workflow
   - Status: Complete ✅

### 🚧 In Progress

#### Task 1: Test Helper Functions Individually - **CURRENT FOCUS**
- [ ] Test `_call_openai()` function with sample image
- [ ] Test `_call_anthropic()` function with sample image  
- [ ] Verify both return consistent response format
- [ ] Check error handling for missing API keys
- [ ] Validate base64 image encoding works correctly

**Working Notes:**
- Focus on testing individual functions before integrating into main()
- Use sample images from `data/input/images/batch_1/`
- Ensure both functions return: `{success, model, content, usage, raw_response}`
- Test with and without API keys to verify error handling

#### Task 2: Environment Setup (Backlogged)
- [x] Create `.gitignore` file with standard Python exclusions
- [x] Add `.env` to .gitignore to prevent committing API keys
- [x] Create `.env` file with API key placeholders
- [ ] Test dotenv loading functionality
- [ ] Document environment setup in README/docs

### 📋 Backlogged Tasks (Low Priority)

#### Task 3: Complete main() function implementation
- [ ] Call run_model() from main()
- [ ] Add result display and error handling
- [ ] Test end-to-end pipeline functionality

#### Task 4: Configuration loading
- [ ] Load models.yaml
- [ ] Load prompts.yaml
- [ ] Create configuration objects
- [ ] Add model mapping

#### Task 5: Data extraction methods
- [ ] Implement reasoning extraction
- [ ] Implement CSV extraction
- [ ] Parse model responses
- [ ] Validate extracted data

#### Task 6: Output saving
- [ ] Create output directory structure
- [ ] Save raw responses
- [ ] Save extracted data
- [ ] Add timestamps

#### Task 7: CLI improvements
- [ ] Add more command options
- [ ] Implement batch processing
- [ ] Add verbose/quiet modes
- [ ] Better error messages

## Code Snippets & References

### Model Mapping
```python
MODEL_MAPPING = {
    'gpt-4o': 'gpt-4o',
    'gpt-4o-mini': 'gpt-4o-mini', 
    'sonnet37': 'claude-3-5-sonnet-20241022',
    # Add more as needed
}
```

### Issues Found
1. Line 46: `image_path` is undefined - should be `graph`
2. Line 59: `_call_anthropic` missing parentheses and arguments
3. Line 56: `call_openai(model, graph, prompt)` - should pass `base64_image` not `graph`

#### Task 8: Final Codebase Review
- [ ] Run through entire codebase for .gitignore completeness
- [ ] Check for any temporary files, logs, or cache directories
- [ ] Verify no API keys or secrets in tracked files
- [ ] Review data/ directory structure for output patterns
- [ ] Test pipeline end-to-end with each model type
- [ ] Validate error handling across all functions
- [ ] Final file organization review to ensure all files are in optimal locations

## File Organization & Structure

### Directory Reorganization (COMPLETED ✅)
- ✅ `test_functions.py` → `tests/` (validation scripts) + fixed import paths  
- ✅ `model_data_dict.py` → deleted (tracked in GitHub issue #1, recoverable from git)
- ✅ `visualization_variables.py` → `src/visualization/`
- ✅ `pipeline.py` → kept at root level (main CLI entry point)
- ✅ Import paths updated for moved files

### Planned Refactoring for `model_data_dict.py` (Backlogged)
**Recovery:** File deleted but recoverable from commit `cc930b4`:
```bash
git show cc930b4:model_data_dict.py
```
**Tracking:** GitHub issue #1 - https://github.com/carolynqian/LLM-digitize-visualization/issues/1

**Current State:** Monolithic dictionary with ground truth + model results + metadata
**Target Structure:**
1. **Extract Ground Truth Data** → `data/input/ground_truth/`
   - `Cai7_ground_truth.csv`, `Polian3_ground_truth.csv`, `Ross3_ground_truth.csv`
   - `metadata.json` (axis ranges, labels)

2. **Restructure Model Results** → `data/output/test_runs/`
   - Format: `{img}_{prompt}_{model}_{timestamp}/`
   - Contains: `raw_response.json`, `processed_data.csv`, `error_metrics.json`, `metadata.json`

3. **Create Aggregation Files**
   - `data/output/batch_results/` - Results by image/prompt
   - `data/output/experiments/` - Cross-model comparisons

4. **Update Streamlit** - Read from structured directories instead of monolithic dict

**Rationale:** Separates static ground truth from experimental results, enables timestamped experiment tracking, follows target architecture from instructions.md

## Next Steps
1. Fix the `call_anthropic()` function first
2. Then fix bugs in `run_model()`
3. Test with each model type
4. Add configuration loading