#!/usr/bin/env python3
import os
import subprocess
import shutil

# Configuration
branches = ["Build21", "Build23", "Build25", "main"]  # Add all your branches here
repo_path = os.getcwd()  # Assumes you're running from the repo root
template_dir = os.path.join(repo_path, "source", "_templates")


# Function to create _templates directory if it doesn't exist
def ensure_template_dir():
    if not os.path.exists(template_dir):
        os.makedirs(template_dir)

    # Write versions.html to template dir if it doesn't exist
    versions_file = os.path.join(template_dir, "versions.html")
    if not os.path.exists(versions_file):
        with open(versions_file, 'w') as f:
            f.write("""<div class="rst-versions" data-toggle="rst-versions" role="note" aria-label="versions">
    <span class="rst-current-version" data-toggle="rst-current-version">
        Version:
        {% if current_version.name == "main" %}
        dev
        {% else %}
        {{ current_version.name }}
        {% endif %}
        <span class="fa fa-caret-down"></span>
    </span>
    <div class="rst-other-versions">
        {% if versions %}
        <dl>
            <dt>{{ _('Versions') }}</dt>
            {% for item in versions|reverse %}
            <dd><a href="{{ item.url }}">
                    {% if item.name == "main" %}
                    dev
                    {% else %}
                    {{ item.name }}
                    {% endif %}
                </a></dd>
            {% endfor %}
        </dl>
        {% endif %}
        <br>
        </dl>
    </div>
</div>""")


# Function to update conf.py in the current branch
def update_conf_py():
    conf_path = os.path.join(repo_path, "source", "conf.py")

    if not os.path.exists(conf_path):
        print(f"Warning: conf.py not found in current branch at {conf_path}")
        return

    with open(conf_path, 'r') as f:
        content = f.read()

    # Fix templates_path if needed
    if "templates_path = ['_templates']" in content and "html_sidebars" not in content:
        # Add html_sidebars configuration
        sidebar_config = "html_sidebars = {'**': ['versions.html']}\n"

        # Find where to insert html_sidebars
        # Usually after templates_path or in the HTML Output section
        if "# -- HTML Output" in content:
            content = content.replace("# -- HTML Output",
                                      "# -- HTML Output\n" + sidebar_config)
        else:
            content = content.replace("templates_path = ['_templates']",
                                      "templates_path = ['_templates']\n" + sidebar_config)

    # Ensure sphinx_multiversion is in extensions
    if "'sphinx_multiversion'" not in content and "\"sphinx_multiversion\"" not in content:
        if "extensions = [" in content:
            content = content.replace("extensions = [",
                                      "extensions = [\n    'sphinx_multiversion',")

    # Update smv_branch_whitelist to include all build branches
    whitelist = r"smv_branch_whitelist = r'^(main|Build.*|dev)$'"
    if "smv_branch_whitelist" in content:
        # Use regex to replace existing whitelist
        import re
        content = re.sub(r"smv_branch_whitelist = r'[^']+'", whitelist, content)
    else:
        # Add it if not present
        content += f"\n\n# Added by migration script\n{whitelist}\n"

    # Write updated content back to conf.py
    with open(conf_path, 'w') as f:
        f.write(content)
    print(f"Updated conf.py in current branch")


# Main script logic
def main():
    current_branch = subprocess.check_output(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        text=True
    ).strip()

    print(f"Starting with current branch: {current_branch}")

    # Store any uncommitted changes
    has_changes = subprocess.call(["git", "diff-index", "--quiet", "HEAD", "--"]) != 0
    if has_changes:
        print("Stashing uncommitted changes...")
        subprocess.call(["git", "stash"])

    try:
        # Process each branch
        for branch in branches:
            print(f"\nSwitching to branch: {branch}")
            subprocess.call(["git", "checkout", branch])

            # Create template directory and add versions.html
            ensure_template_dir()

            # Update conf.py
            update_conf_py()

            # Commit changes
            subprocess.call(["git", "add", "-A"])
            subprocess.call(["git", "commit", "-m", "Update sphinx-multiversion configuration"])

            # Push changes
            print(f"Pushing changes to {branch}...")
            subprocess.call(["git", "push", "origin", branch])

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Return to original branch
        print(f"\nReturning to original branch: {current_branch}")
        subprocess.call(["git", "checkout", current_branch])

        # Restore uncommitted changes if there were any
        if has_changes:
            print("Restoring stashed changes...")
            subprocess.call(["git", "stash", "pop"])


if __name__ == "__main__":
    print("This script will update sphinx-multiversion configuration across multiple branches.")
    print("Make sure you have a clean working directory before running.")
    confirmation = input("Continue? (y/n): ")

    if confirmation.lower() == 'y':
        main()
    else:
        print("Operation cancelled.")