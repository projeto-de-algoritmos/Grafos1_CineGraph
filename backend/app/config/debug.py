import debugpy, os

def debug_configurations():
    if os.getenv("DEBUGGER"):
        print("You can attach VS Code now")
        debugpy.listen(('0.0.0.0', 5678))
        debugpy.wait_for_client()
        print("Debugger runing on port 5678")