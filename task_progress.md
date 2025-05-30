# Task Progress & Working Notes

## Current Sprint: Pipeline Refactoring

### ✅ Completed Tasks
1. **Updated imports in `pipeline.py`**
   - Added: `json`, `yaml`, `datetime`, `pathlib.Path`, `typing`, `re`, `anthropic`
   - Status: Complete ✅

2. **Fixed `call_openai()` function**
   - Proper message structure with text and image
   - Try/except error handling  
   - Structured response format
   - 4000 max_tokens, 0.1 temperature
   - Status: Complete ✅

### 🚧 In Progress

#### Task 0: Environment setup (.env and .gitignore) - **PRIORITY**
- [ ] Create `.gitignore` file with standard Python exclusions
- [ ] Add `.env` to .gitignore to prevent committing API keys
- [ ] Create `.env.example` template file
- [ ] Test dotenv loading functionality
- [ ] Document environment setup in README/docs

**Working Notes:**
- Currently no `.env` or `.gitignore` files exist
- `load_dotenv()` is called but does nothing without `.env` file
- Need to prevent accidental API key commits
- Template should show required environment variables:
  - OPENAI_API_KEY
  - ANTHROPIC_API_KEY  
  - OPENROUTER_API_KEY

#### Task 0.5: Fix Critical Pipeline Bugs - **IMMEDIATE**
- [ ] **Bug 1**: Line 46 - Fix `image_path` undefined variable (should be `graph`)
- [ ] **Bug 2**: Line 56 - Fix OpenAI call passing `graph` instead of `base64_image`  
- [ ] **Bug 3**: Line 59 - Fix incomplete `_call_anthropic` call (missing parentheses/args)

**Working Notes:**
- These bugs prevent pipeline from running at all
- All are in `run_model()` function lines 42-60
- Must fix before any testing can begin
- Bug 1 causes immediate crash on any model
- Bug 2 breaks OpenAI models specifically  
- Bug 3 breaks Anthropic models specifically

#### Task 1: Fix `call_anthropic()` function
- [ ] Convert from class method (remove `self` parameter)
- [ ] Match return structure of `call_openai()`
- [ ] Add consistent error handling
- [ ] Test with proper model name

**Working Notes:**
- Current function signature: `def _call_anthropic(self, prompt: str, base64_image: str)`
- Need to change to: `def call_anthropic(model, base64_image, prompt)`
- Model names: Need to map 'sonnet37' to actual Anthropic model ID

### 📋 Pending Tasks

#### Task 2: Fix `run_model()` function
- [ ] Fix variable name bug (`image_path` vs `graph`)
- [ ] Complete the match/case statement
- [ ] Add proper model routing
- [ ] Handle OpenRouter models

#### Task 3: Configuration loading
- [ ] Load models.yaml
- [ ] Load prompts.yaml
- [ ] Create configuration objects
- [ ] Add model mapping

#### Task 4: Data extraction methods
- [ ] Implement reasoning extraction
- [ ] Implement CSV extraction
- [ ] Parse model responses
- [ ] Validate extracted data

#### Task 5: Output saving
- [ ] Create output directory structure
- [ ] Save raw responses
- [ ] Save extracted data
- [ ] Add timestamps

#### Task 6: CLI improvements
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