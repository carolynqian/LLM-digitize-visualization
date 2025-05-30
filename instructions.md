# Claude Code Request: LLM Scientific Plot Data Extraction Pipeline

## Project Overview

I need to create an automated experimental pipeline to evaluate how well different frontier LLMs can extract numerical data from scientific plots. This is a 1-2 week exploratory research project that will test various models to understand their capabilities in digitizing data from scatter and line plots.

## Objectives

1. **Systematic Testing**: Run batches of experiments with different models, prompts, and scientific plots
2. **Data Analysis**: Calculate robust error metrics and generate insights
3. **Visualization**: Create interactive Streamlit dashboard to compare results
4. **Automated Insights**: Use meta-analysis LLM to identify patterns and recommendations

## Technical Requirements

### Directory Structure
```
llm_plot_extraction/
├── config/                   # Central configuration hub
│   ├── models.yaml          # API routing (direct APIs first, OpenRouter fallback)
│   ├── prompts.yaml         # Different extraction strategies (baseline, detailed_cot, etc.)
│   └── experiments.yaml     # Experiment configurations
├── data/                     # Organized input/output separation
│   ├── input/
│   │   ├── images/          # Scientific plots organized by experiment batches
│   │   │   ├── batch_1/
│   │   │   ├── batch_2/
│   │   │   └── ...
│   │   └── ground_truth/    # True data points for each graph (CSV files)
│   └── output/              # Results hierarchy
│       ├── test_runs/      # Individual LLM digitization attempts
│       │   └── {img}_{prompt}_{model}_{timestamp}/
│       │       ├── raw_response.json
│       │       ├── processed_data.csv
│       │       ├── error_metrics.json
│       │       ├── analysis_report.md
│       │       └── metadata.json
│       ├── batch_results/   # Aggregated batch analyses
│       └── experiments/     # Cross-batch comparative studies
├── src/                      # Modular processing pipeline
│   ├── core/                # LLM interface, data processing, error calculation
│   │   ├── llm_interface.py
│   │   ├── data_processor.py
│   │   ├── error_calculator.py
│   │   └── analyzer.py
│   ├── analysis/            # Individual run → batch → comparative analysis progression
│   │   ├── individual_run.py
│   │   ├── batch_analyzer.py
│   │   └── comparative_analyzer.py
│   └── visualization/       # Streamlit dashboard for interactive comparison
│       └── streamlit_app.py
├── experiments/             # Entry points for research execution
│   ├── run_single_test.py   # Execute one LLM digitization attempt
│   ├── run_batch.py         # Run multiple models/prompts systematically
│   └── run_experiment_suite.py  # Cross-batch comparative studies
├── tests/                   # Software testing and validation
└── requirements.txt
```

### Dependencies
```
openai
anthropic
streamlit
plotly
matplotlib
scipy
opencv-python
pandas
numpy
pydantic
PyYAML
requests
python-dotenv
```

## Core Components to Build

### 1. LLM Interface Module (`src/core/llm_interface.py`)
- Support for multiple models via direct APIs (cheaper) and OpenRouter fallback
- Standardized request/response handling with automatic routing to cheapest source
- Retry logic and rate limiting
- Cost tracking
- Chain-of-thought reasoning capture

**API Priority:**
- Use direct APIs first (Anthropic, OpenAI) for cost efficiency
- Fall back to OpenRouter for models not available directly or when free tier available

### 2. Data Processing (`src/core/data_processor.py`)
- Parse LLM responses into structured format
- Handle multiple dataset detection (different symbols: circles, squares, triangles, stars)
- Data validation and cleaning
- CSV output generation

### 3. Error Calculator (`src/core/error_calculator.py`)
**Robust MSE Implementation:**
- Use Hungarian algorithm (scipy.optimize.linear_sum_assignment) to solve assignment problem when LLM confuses which points belong to which dataset
- Calculate point-level, dataset-level, and graph-level accuracy
- Handle cases where LLM detects different numbers of datasets than ground truth

**Visual Similarity Metrics:**
- Structural Similarity Index (SSIM) between original and reconstructed plots
- Histogram comparison
- Feature-based matching

### 4. Streamlit Visualization (`src/visualization/streamlit_app.py`)
**Interface Design:**
- Sidebar with dropdowns for: Test Batch, Graph, Model
- Main area: Side-by-side comparison of original image and reconstructed plot
- No connecting lines between points, just scatter plots with appropriate symbols
- Load data from CSV files in organized directory structure
- Display error metrics and analysis results

**Plot Requirements:**
- Map datasets to specific shapes (circles, squares, triangles, stars) based on LLM output
- Handle variable numbers of datasets per graph
- Color coding optional, focus on symbol differentiation

### 5. Meta-Analysis Integration
- Send experiment results to analysis LLM for automated insights
- Generate summary reports identifying patterns, failure modes, and recommendations
- Compare model performance across different graph types

## Experiment Workflow

### Single Test Run:
1. **Input**: Model selection, prompt template, image file
2. **API Call**: Send image and prompt to selected LLM via most cost-effective route
3. **Response Processing**: Parse output, extract data points and reasoning
4. **Storage**: Save all data to organized directory structure with timestamp
5. **Error Calculation**: Compare against ground truth, calculate metrics
6. **Visualization Update**: Add results to Streamlit dashboard

### Batch Processing:
- Run multiple models on same graph with same prompt
- Run same model with different prompts on same graph
- Process entire batches of graphs systematically
- Generate comparative analyses

## Data Formats

### LLM Response JSON Schema:
```json
{
    "model": "claude-3-5-sonnet-20241022",
    "prompt_version": "baseline",
    "image_file": "img1.png",
    "response": {
        "extracted_data": "CSV format with headers",
        "reasoning": "Chain of thought explanation",
        "datasets_detected": 4,
        "confidence": "high/medium/low"
    },
    "metadata": {
        "timestamp": "2025-05-27T14:30:22Z",
        "cost_usd": 0.045,
        "duration_seconds": 12.5,
        "api_source": "direct_anthropic"
    }
}
```

### Error Metrics JSON:
```json
{
    "mse_total": 125.6,
    "mse_per_dataset": [45.2, 67.1, 13.3],
    "assignment_accuracy": 0.85,
    "visual_similarity": 0.78,
    "point_detection_rate": 0.92,
    "dataset_detection_accuracy": 1.0
}
```

## Configuration Files

### models.yaml:
```yaml
# Direct API sources (cheaper)
direct_apis:
  anthropic:
    api_key: "${ANTHROPIC_API_KEY}"
    base_url: "https://api.anthropic.com"
    models:
      claude35_sonnet:
        name: "claude-3-5-sonnet-20241022"
        max_tokens: 4000
        temperature: 0.1
      claude35_haiku:
        name: "claude-3-5-haiku-20241022"
        max_tokens: 4000
        temperature: 0.1
  
  openai:
    api_key: "${OPENAI_API_KEY}"
    base_url: "https://api.openai.com/v1"
    models:
      gpt4o:
        name: "gpt-4o"
        max_tokens: 4000
        temperature: 0.1
      gpt4o_mini:
        name: "gpt-4o-mini"
        max_tokens: 4000
        temperature: 0.1

# OpenRouter fallback (for models not available directly)
openrouter:
  api_key: "${OPENROUTER_API_KEY}"
  base_url: "https://openrouter.ai/api/v1"
  models:
    opus:
      name: "anthropic/claude-3-opus"
      max_tokens: 4000
      temperature: 0.1
    gemini_pro:
      name: "google/gemini-pro-vision"
      max_tokens: 4000
      temperature: 0.1
```

### prompts.yaml:
```yaml
baseline: |
  Please extract all numerical data points from this scientific plot. 
  Return the data in CSV format with appropriate headers.
  Include your reasoning process.

detailed_cot: |
  Analyze this scientific plot step by step:
  1. Identify the axes and their units
  2. Identify different datasets (symbols, colors)
  3. Extract coordinates for each data point
  4. Organize into CSV format with clear headers
  Return both your analysis and the final CSV data.
```

## Sample Images and Ground Truth

I have scientific plots with multiple datasets represented by different symbols (circles, squares, triangles, stars). These should be stored in `data/input/images/batch_X/` with corresponding ground truth CSV files in `data/input/ground_truth/`.

Example ground truth format:
```csv
D / km·s⁻¹,T / K (Solid Squares),D / km·s⁻¹,T / K (Solid Triangles),D / km·s⁻¹,T / K (Stars),D / km·s⁻¹,T / K (Open Circles)
4.1,700,8.4,5900,8.2,7000,8.3,5500
8.9,5300,10.1,9700,9.3,8100,10.3,10400
13.5,11700,,10.2,10200,10.7,10800
```

## Execution Commands

Create these main entry points:
- `python experiments/run_single_test.py --image img1.png --prompt baseline --model claude35_sonnet`
- `python experiments/run_batch.py --batch batch_1 --models claude35_sonnet,gpt4o --prompts baseline,detailed_cot`
- `streamlit run src/visualization/streamlit_app.py`

## Success Criteria

1. **Functional Pipeline**: Can run experiments and store results systematically
2. **Cost-Effective API Usage**: Automatically routes to cheapest available API source
3. **Robust Analysis**: Handles variable dataset numbers and calculates meaningful error metrics
4. **Interactive Visualization**: Easy comparison of results across models and graphs
5. **Automated Insights**: Meta-analysis provides actionable recommendations
6. **Extensible Design**: Easy to add new models, prompts, or analysis methods

Please create this experimental pipeline with clean, well-documented code that follows the directory structure and implements all the specified functionality. Focus on making it easy to run experiments, analyze results, and gain insights into LLM performance on scientific plot digitization tasks.
