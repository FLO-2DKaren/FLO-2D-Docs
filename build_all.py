import subprocess
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
main_source = os.path.join(root_dir, 'source')
channel_source = os.path.join(main_source, 'flo-2d_pro', 'Channel Modeling Guidelines')
build_dir = os.path.join(root_dir, '_build')

print("📘 Building main documentation...")
subprocess.run(['sphinx-build', '-E', '-b', 'html', main_source, os.path.join(build_dir, 'main')], check=True)

print("🌊 Building Channel Modeling Guidelines...")
subprocess.run(['sphinx-build', '-E', '-b', 'html', channel_source, os.path.join(build_dir, 'channel_modeling')], check=True)

print("✅ Build complete! Check _build directory.")
