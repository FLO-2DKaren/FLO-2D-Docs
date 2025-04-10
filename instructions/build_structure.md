# FLO-2D Documentation: Build 25 Structure Setup Overview

## ✅ Goal
Establish the directory and file structure for the **Build 25** version of the FLO-2D Pro Documentation using Sphinx and `sphinx-multiversion`.

---

## 🗂️ Branch
- Active Git branch: `Build25`
- Branch automatically detected via script using:
  ```bash
  git rev-parse --abbrev-ref HEAD
  ```

---

## 🧱 Directory & File Structure
Created under the `source/` directory with nested subdirectories for organization.

```
source/
├── index.rst (main TOC)
├── setup/
│   ├── index.rst
│   ├── flo-2d_pro_setup.rst
│   ├── qgis_setup.rst
│   ├── gds_mapper.rst
│   └── test_setup.rst
├── flo-2d_pro/
│   ├── index.rst
│   ├── data_input_manual.rst
│   ├── channel_modeling_guidelines.rst
│   └── storm_drain_modeling_guidelines.rst
├── flo-2d_plugin/
│   ├── index.rst
│   ├── user_manual.rst
│   └── technical_reference_manual.rst
└── tutorials/
    ├── index.rst
    ├── self_help_kit.rst
    ├── dam_breach_modeling.rst
    └── coastal_urban_modeling.rst
```

Each `.rst` file includes:
- A section header.
- Placeholder content.
- Included in its section's `index.rst`.

---

## 🛠️ Script Details
A Python script was written to:
- Automatically detect the Git branch.
- Generate the directory and file layout.
- Create properly formatted `.rst` headers and toctrees.
- Update the main `source/index.rst` with the appropriate branch name and links to all top-level sections.

---

## 🧪 Next Steps
- Populate `.rst` files with real content.
- Add media (e.g., diagrams, screenshots).
- Run `sphinx-multiversion` to verify the output:
  ```bash
  sphinx-multiversion source build/html
  ```
- Begin parallel updates on `Build21` and `Build23` branches.

---

**Status:** ✅ Build 25 structure created successfully and ready for content development.
