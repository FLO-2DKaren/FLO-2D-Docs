import os

# Define the base source directory
base_dir = 'source'

# Define the structure
structure = {
    'Setup': [
        'FLO-2D Pro Setup',
        'QGIS Setup',
        'GDS/Mapper',
        'Test Setup'
    ],
    'FLO-2D Pro': [
        'Data Input Manual',
        'Channel Modeling Guidelines',
        'Storm Drain Modeling Guidelines'
    ],
    'FLO-2D Plugin': [
        'User Manual',
        'Technical Reference Manual'
    ],
    'Tutorials': [
        'Self Help Kit',
        'Dam Breach Modeling',
        'Coastal Urban Modeling'
    ]
}


def safe_filename(name):
    return name.lower().replace(' ', '_').replace('/', '_')


# Create folders and files
for section, pages in structure.items():
    section_dir = os.path.join(base_dir, safe_filename(section))
    os.makedirs(section_dir, exist_ok=True)

    # Create index.rst for each section
    with open(os.path.join(section_dir, 'index.rst'), 'w', encoding='utf-8') as f:
        f.write(f"{section}\n{'=' * len(section)}\n\n")
        f.write(".. toctree::\n   :maxdepth: 2\n   :caption: {}\n\n".format(section))
        for page in pages:
            page_file = safe_filename(page)
            f.write(f"   {page_file}\n")

    # Create each page file
    for page in pages:
        page_filename = safe_filename(page) + '.rst'
        with open(os.path.join(section_dir, page_filename), 'w', encoding='utf-8') as f:
            f.write(f"{page}\n{'=' * len(page)}\n\n")
            f.write(f"Content for {page} will go here.\n")

# Update the main index.rst file
main_index = os.path.join(base_dir, 'index.rst')
with open(main_index, 'w', encoding='utf-8') as f:
    f.write("FLO-2D Pro Documentation – Build 25\n")
    f.write("=" * 40 + "\n\n")
    f.write("Welcome to the Build 25 version of the FLO-2D Documentation.\n\n")
    f.write(".. toctree::\n   :maxdepth: 2\n   :caption: Contents:\n\n")
    for section in structure:
        section_path = safe_filename(section) + '/index'
        f.write(f"   {section_path}\n")

print("Documentation structure created successfully.")
