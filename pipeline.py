import argparse
from dotenv import load_dotenv
import base64
import os
import json
import yaml
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional
import re

# Import API clients
import openai
import anthropic

def get_user_inputs():
    parser = argparse.ArgumentParser(description="Automated Digitization Pipeline")
    parser.add_argument('--model', 
                        '-m',
                        type=str, 
                        default='gpt-4o',
                        help='Model to use')
    parser.add_argument('--graph', 
                        '-g',
                        type=str, 
                        required=True, 
                        help='Path to graph image')
    parser.add_argument('--prompt', 
                        '-p',
                        type=str, 
                        default='Extract the graph data from the image',
                        help='Prompt for the model')

    args = parser.parse_args()
    print(f"Model: {args.model}, Graph: {args.graph}, Prompt: {args.prompt}")
    return args.model, args.graph, args.prompt

# process input()


# step 2: run through model (LLM)
def run_model(model, graph, prompt):
    print(f"Running model {model} on graph {graph} with prompt: {prompt}")

    # read and encode image
    with open(graph, "rb") as image_file:
        # base64 encoding converts binary image data to text format that can be sent over HTTP
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')

    match model:
        case 'gpt-4o':
            print("Using GPT-4o model")
            return _call_openai(model, base64_image, prompt)
        case 'gpt-4o-mini':
            print("Using GPT-4o-mini model")
            return _call_openai(model, base64_image, prompt)
        case 'sonnet37':
            print("Using Sonnet 3.7 model")
            return _call_anthropic(model, base64_image, prompt)
        case _:
            return {'success': False, 'error': f'Unsupported model: {model}'}

def _call_openai(model, base64_image, prompt):
    # Retrieve API key from environment variable
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set.")
        print("Please set it using: export OPENAI_API_KEY='your_key_here'")
        exit(1) # Exit if the key is not set
    
    # Initialize the OpenAI client with the key from the environment
    client = openai.OpenAI(api_key=api_key)
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=4000,
            temperature=0.1
        )
        
        return {
            'success': True,
            'model': model,
            'content': response.choices[0].message.content,
            'usage': {
                'input_tokens': response.usage.prompt_tokens,
                'output_tokens': response.usage.completion_tokens,
                'total_tokens': response.usage.total_tokens
            },
            'raw_response': response.model_dump()
        }
        
    except Exception as e:
        return {'success': False, 'error': f"OpenAI API error: {str(e)}"}





def _call_anthropic(model: str, base64_image: str, prompt: str) -> Dict[str, Any]:
    """Call Anthropic's Claude vision model"""
    # You'll need to install: pip install anthropic
    # And set your API key: export ANTHROPIC_API_KEY=your_key_here
    
    try:
        import anthropic
        client = anthropic.Anthropic()  # Uses ANTHROPIC_API_KEY environment variable
        
        response = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1000,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/jpeg",
                                "data": base64_image
                            }
                        },
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ]
        )
        
        return {
            'success': True,
            'model': model,
            'content': response.content[0].text,
            'usage': {
                'input_tokens': response.usage.input_tokens,
                'output_tokens': response.usage.output_tokens,
                'total_tokens': response.usage.input_tokens + response.usage.output_tokens
            },
            'raw_response': response.model_dump()
        }
        
    except Exception as e:
        return {'success': False, 'error': f"Anthropic API error: {str(e)}"}


# step 3: store results


def main():
    # Load environment variables from .env file
    load_dotenv()
    # step 1: get user inputs
    model, graph, prompt = get_user_inputs()


    # step 2: run through model (LLM)

if __name__ == "__main__":
    main()