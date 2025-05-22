import subprocess
import os

# List of subprojects (relative paths from project root)
subprojects = [
    'source/flo-2d_pro/Channel Modeling Guidelines',
    # add more subproject paths here
]

# Build main documentation (single conf.py in /source)
print("📘 Building main documentation...")
subprocess.run(['sphinx-build', '-E', '-b', 'html', '_build/main'], check=True)

# Build each subproject with its own conf.py
for path in subprojects:
    print(f"📗 Building subproject in: {path}")
    build_dir = os.path.join(path, '_build', 'html')
    subprocess.run(['sphinx-build', '-E', '-b', 'html', path, build_dir], check=True)
