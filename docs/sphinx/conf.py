# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

# make repo base directory visible to Sphinx
sys.path.insert(0, os.path.abspath('../../../'))
# make contents of hidden folder .github visible to Sphinx
sys.path.insert(0, os.path.abspath('../../../.github'))
sys.path.insert(0, os.path.abspath('.'))

import site_data

# -- Project information -----------------------------------------------------

project = 'Open-Orange-Button'
copyright = '2022, SunSpec Alliance'


# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.napoleon',
    'sphinx.ext.githubpages',
    'sphinxcontrib.datatemplates',
    'sphinxcontrib.autoprogram',
    'sphinxcontrib.mermaid',
    'sphinx_substitution_extensions'
]

# The suffix of source filenames.
source_suffix = '.rst'


# Add any paths that contain templates here, relative to this directory.
templates_path = []


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = []

html_js_files = []

html_theme_options = {
    'left_sidebar_end': []
}

html_sidebars = {
    'baseclasses': [],
}

# extlinks alias
extlinks = {
    'issue': ('https://github.com/Open-Orange-Button/Orange-Button-Taxonomy/issues/%s', '#%s'),
    'pull': ('https://github.com/Orange-Button-Taxonomy/Open-Orange-Button/pull/%s', '#%s'),
    'ghuser': ('https://github.com/%s', '%s')
}


