#Getting the system information using platform
import platform
from datetime import datetime

print("="*10, "System Information", "="*10)
uname=platform.uname()
print(f"System:{uname.system}")
print(f"Node:{uname.node}")
print(f"Release:{uname.release}")
print(f"Machine:{uname.machine}")
print(f"Processor:{uname.processor}")
