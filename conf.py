"""Simple web server implementation Something SWISS.
Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html

-- Project information -----------------------------------------------------
https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
"""

# pylint: disable=invalid-name,redefined-builtin
import sys
from pathlib import Path
import version_query

sys.path.insert(0, str(Path(".", "swiss").resolve()))


def get_release():
    """Query the current release for the project."""
    try:
        repo_path = Path(".")
        ret_value = version_query.git_query.query_git_repo(repo_path).to_str()
    except ValueError:
        ret_value = version_query.Version.from_str("0.0.1").devel_increment().to_str()
    return ret_value


author = "James Nugraha, Xander Harris"
audodoc_default_options = {"members": True}
autoyaml_root = "."
autoyaml_doc_delimiter = "###"
autoyaml_comment = "#"
autoyaml_level = 10
autoyaml_safe_loader = True
copyright = "2024 (c) James Nugraha, Xander Harris. All rights reserved."

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

exclude_patterns = [
    "_build",
    ".DS_Store",
    ".gnupg",
    ".venv",
    "Thumbs.db",
    "charts/storage-classes/*",
    "charts/postgresql/*",
    "charts/redis/*",
    "charts/calico/*",
]
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.githubpages",
    "sphinxcontrib.autoyaml",
    "sphinx_copybutton",
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_favicon = "_static/img/logo/swiss.png"
html_logo = "_static/img/logo/swiss.png"
html_static_path = ["_static"]
html_theme = "sphinx_book_theme"
myst_dmath_double_inline = True
myst_enable_extensions = [
    "amsmath",
    "attrs_block",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
myst_title_to_header = True
release = get_release()
project = "Charts"
source_suffix = {
    ".md": "markdown",
    ".rst": "restructuredText",
}
templates_path = ["_templates"]
