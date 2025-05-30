#!/usr/bin/env python3
"""
Test script for individual helper functions in pipeline.py
"""

import sys
import os
import base64
from pathlib import Path
from dotenv import load_dotenv

# Add the root directory to the path so we can import from pipeline.py
sys.path.append(str(Path(__file__).parent.parent))

from pipeline import _call_openai, _call_anthropic

def test_base64_encoding(image_path):
    """Test that base64 encoding works correctly"""
    print(f"\n🔧 Testing base64 encoding for: {image_path}")
    
    try:
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')
        
        print(f"✅ Base64 encoding successful")
        print(f"   - Encoded length: {len(base64_image)} characters")
        print(f"   - First 50 chars: {base64_image[:50]}...")
        return base64_image
    except Exception as e:
        print(f"❌ Base64 encoding failed: {str(e)}")
        return None

def test_openai_function(base64_image):
    """Test the _call_openai function"""
    print(f"\n🤖 Testing _call_openai() function...")
    
    model = "gpt-4o"
    prompt = "What do you see in this image? Describe it briefly."
    
    try:
        result = _call_openai(model, base64_image, prompt)
        
        print(f"✅ OpenAI function completed")
        print(f"   - Success: {result.get('success', 'Unknown')}")
        
        if result.get('success'):
            print(f"   - Model: {result.get('model', 'Unknown')}")
            print(f"   - Content length: {len(result.get('content', ''))}")
            print(f"   - Usage: {result.get('usage', {})}")
            print(f"   - Content preview: {result.get('content', '')[:100]}...")
        else:
            print(f"   - Error: {result.get('error', 'Unknown error')}")
        
        return result
    except Exception as e:
        print(f"❌ OpenAI function failed with exception: {str(e)}")
        return None

def test_anthropic_function(base64_image):
    """Test the _call_anthropic function"""
    print(f"\n🤖 Testing _call_anthropic() function...")
    
    model = "sonnet37"
    prompt = "What do you see in this image? Describe it briefly."
    
    try:
        result = _call_anthropic(model, base64_image, prompt)
        
        print(f"✅ Anthropic function completed")
        print(f"   - Success: {result.get('success', 'Unknown')}")
        
        if result.get('success'):
            print(f"   - Model: {result.get('model', 'Unknown')}")
            print(f"   - Content length: {len(result.get('content', ''))}")
            print(f"   - Usage: {result.get('usage', {})}")
            print(f"   - Content preview: {result.get('content', '')[:100]}...")
        else:
            print(f"   - Error: {result.get('error', 'Unknown error')}")
        
        return result
    except Exception as e:
        print(f"❌ Anthropic function failed with exception: {str(e)}")
        return None

def test_api_key_handling():
    """Test error handling when API keys are missing"""
    print(f"\n🔑 Testing API key error handling...")
    
    # Save current API keys
    openai_key = os.getenv("OPENAI_API_KEY")
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")
    
    # Remove API keys temporarily
    if openai_key:
        os.environ.pop("OPENAI_API_KEY", None)
    if anthropic_key:
        os.environ.pop("ANTHROPIC_API_KEY", None)
    
    print("   Testing OpenAI without API key...")
    try:
        result = _call_openai("gpt-4o", "dummy_image", "test prompt")
        print(f"   - Result: {result}")
    except SystemExit:
        print("   - OpenAI function properly exits when API key missing ✅")
    except Exception as e:
        print(f"   - OpenAI error handling: {str(e)}")
    
    print("   Testing Anthropic without API key...")
    try:
        result = _call_anthropic("sonnet37", "dummy_image", "test prompt")
        print(f"   - Result: {result}")
    except Exception as e:
        print(f"   - Anthropic error handling: {str(e)}")
    
    # Restore API keys
    if openai_key:
        os.environ["OPENAI_API_KEY"] = openai_key
    if anthropic_key:
        os.environ["ANTHROPIC_API_KEY"] = anthropic_key

def main():
    """Main test function"""
    print("🧪 Starting helper function tests...")
    
    # Load environment variables
    load_dotenv()
    
    # Test image path
    image_path = "data/input/images/batch_1/Cai7_graph_forVis.png"
    
    if not os.path.exists(image_path):
        print(f"❌ Test image not found: {image_path}")
        return
    
    # Test 1: Base64 encoding
    base64_image = test_base64_encoding(image_path)
    if not base64_image:
        print("❌ Cannot proceed without successful base64 encoding")
        return
    
    # Test 2: OpenAI function
    openai_result = test_openai_function(base64_image)
    
    # Test 3: Anthropic function  
    anthropic_result = test_anthropic_function(base64_image)
    
    # Test 4: API key error handling
    test_api_key_handling()
    
    # Summary
    print(f"\n📊 Test Summary:")
    print(f"   - Base64 encoding: {'✅' if base64_image else '❌'}")
    print(f"   - OpenAI function: {'✅' if openai_result and openai_result.get('success') else '❌'}")
    print(f"   - Anthropic function: {'✅' if anthropic_result and anthropic_result.get('success') else '❌'}")

if __name__ == "__main__":
    main()