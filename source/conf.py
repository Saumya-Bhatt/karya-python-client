# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import pathlib
import sys

# Get the absolute path of the project root
project_root = pathlib.Path(__file__).parent.parent.absolute()
sys.path.insert(0, str(project_root))


project = "Karya"
copyright = "2024, Saumya Bhatt"
author = "Saumya Bhatt"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ["_templates"]
exclude_patterns = []
extensions = [
    "sphinx.ext.autodoc",  # Automatically document from docstrings
    "sphinx.ext.napoleon",  # For Google-style docstrings
    "sphinx.ext.viewcode",  # Add links to the source code
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
