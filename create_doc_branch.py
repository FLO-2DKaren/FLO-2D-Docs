import os
import subprocess
import shutil


def run_command(command, cwd=None):
    result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {command}\n{result.stderr}")
    else:
        print(result.stdout)


def create_branch(build_name, project_dir):
    branch_name = build_name.replace(" ", "")

    # Create new branch
    run_command(f"git checkout -b {branch_name}", cwd=project_dir)

    # Update index.rst with version info
    index_path = os.path.join(project_dir, "source", "index.rst")
    with open(index_path, "r") as f:
        content = f.readlines()

    content.insert(0, f".. This is the documentation for {build_name}\n\n")
    content.insert(0, f".. version: {build_name}\n")

    with open(index_path, "w") as f:
        f.writelines(content)

    # Commit the changes
    run_command("git add .", cwd=project_dir)
    run_command(f'git commit -m "Add documentation for {build_name}"', cwd=project_path)
    # Optional: uncomment to push
    # run_command(f"git push -u origin {branch_name}", cwd=project_dir)


if __name__ == "__main__":
    # Your version builds
    builds = ["Build 21", "Build 23", "Build 25"]

    # Path to the Git repo root
    project_path = os.path.abspath(".")

    for build in builds:
        create_branch(build, project_path)
        run_command("git checkout main", cwd=project_path)  # Return to main before creating the next branch
