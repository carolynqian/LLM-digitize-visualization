# Task Progress & Working Notes

## Current Sprint: Helper Function Testing & Implementation

### ✅ Completed Tasks
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

#### Task 7: Final Codebase Review
- [ ] Run through entire codebase for .gitignore completeness
- [ ] Check for any temporary files, logs, or cache directories
- [ ] Verify no API keys or secrets in tracked files
- [ ] Review data/ directory structure for output patterns
- [ ] Test pipeline end-to-end with each model type
- [ ] Validate error handling across all functions

## Next Steps
1. Fix the `call_anthropic()` function first
2. Then fix bugs in `run_model()`
3. Test with each model type
4. Add configuration loading