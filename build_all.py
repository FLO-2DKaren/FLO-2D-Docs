import subprocess
import os

# Root = C:\Users\PC\PycharmProjects\FLO-2D-Docs
root_dir = os.path.abspath(os.path.dirname(__file__))

main_source = os.path.join(root_dir, 'source')
channel_source = os.path.join(root_dir, 'source', 'flo-2d_pro', 'Channel Modeling Guidelines')
storm_drain_source = os.path.join(root_dir, 'source', 'flo-2d_pro', 'Storm Drain Modeling Guidelines')
build_dir = os.path.join(root_dir, '_build')

print("📘 Building main documentation...")
subprocess.run(['sphinx-build', '-E', '-b', 'html', main_source, os.path.join(build_dir, 'main')], check=True)

print("🌊 Building Channel Modeling Guidelines...")
subprocess.run(['sphinx-build', '-E', '-b', 'html', channel_source, os.path.join(build_dir, 'channel_modeling')], check=True)

print("🌊 Building Storm Drain Modeling Guidelines...")
subprocess.run(['sphinx-build', '-E', '-b', 'html', storm_drain_source, os.path.join(build_dir, 'storm_drain_modeling')], check=True)

print("✅ Build complete! Check the _build folder in the root directory.")
