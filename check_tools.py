#!/usr/bin/env python3
"""
Test script to check specific Playwright tools.
"""
import asyncio
from pprint import pprint

async def main():
    print("Testing specific Playwright tools...")
    
    try:
        # Import the PlaywrightTools class
        from Tools import PlaywrightTools
        print("✅ Successfully imported PlaywrightTools")
        
        # Create an instance
        tools = PlaywrightTools()
        print("✅ Successfully created PlaywrightTools instance")
        
        # Initialize
        initialized = await tools.initialize()
        print(f"✅ Initialized: {initialized}")
        
        # Check if specific methods exist
        has_navigate = hasattr(tools, 'playwright_navigate')
        has_screenshot = hasattr(tools, 'playwright_screenshot')
        
        print(f"Has playwright_navigate: {has_navigate}")
        print(f"Has playwright_screenshot: {has_screenshot}")
        
        # Print method signatures
        if has_navigate:
            import inspect
            nav_sig = inspect.signature(tools.playwright_navigate)
            print(f"\nplaywright_navigate signature: {nav_sig}")
            print(f"playwright_navigate docstring: {tools.playwright_navigate.__doc__}")
        
        if has_screenshot:
            import inspect
            ss_sig = inspect.signature(tools.playwright_screenshot)
            print(f"\nplaywright_screenshot signature: {ss_sig}")
            print(f"playwright_screenshot docstring: {tools.playwright_screenshot.__doc__}")
        
        # List all available playwright methods
        playwright_methods = [m for m in dir(tools) if callable(getattr(tools, m)) and m.startswith('playwright_')]
        print(f"\nAll Playwright methods ({len(playwright_methods)}):")
        for idx, method in enumerate(sorted(playwright_methods)):
            print(f"{idx+1}. {method}")
        
        # Cleanup
        await tools.cleanup()
        print("\n✅ Successfully cleaned up")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
