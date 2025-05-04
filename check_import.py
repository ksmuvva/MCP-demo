#!/usr/bin/env python3
"""
Simple test script to check Python path and module imports.
"""
import sys
import os

def main():
    print("Python executable:", sys.executable)
    print("Python version:", sys.version)
    print("Python path:")
    for p in sys.path:
        print(f"  - {p}")
    
    print("\nCurrent directory:", os.getcwd())
    print("\nTrying to import Tools package...")
    
    try:
        import Tools
        print("✅ Successfully imported Tools package")
        print("Tools package path:", Tools.__file__)
        
        # List the contents of the Tools package
        print("\nContents of Tools package:")
        print(dir(Tools))
        
        # Check if PlaywrightTools is defined
        if hasattr(Tools, 'PlaywrightTools'):
            print("\n✅ PlaywrightTools is defined in Tools package")
        else:
            print("\n❌ PlaywrightTools is not defined in Tools package")
            
            # Try to import PlaywrightTools directly
            try:
                from Tools import PlaywrightTools
                print("✅ Successfully imported PlaywrightTools from Tools package")
            except Exception as e:
                print(f"❌ Error importing PlaywrightTools: {e}")
        
        # Check Tools directory structure
        tools_dir = os.path.dirname(Tools.__file__)
        print(f"\nTools directory: {tools_dir}")
        print("Files in Tools directory:")
        for f in os.listdir(tools_dir):
            print(f"  - {f}")
        
    except ImportError as e:
        print(f"❌ Error importing Tools package: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
