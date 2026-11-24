KEELKIT — Productivity & Automation Toolkit

A toolkit for getting repetitive work done, reliably.

KEELKIT is an open-source, cross-platform productivity and automation toolkit designed to simplify repetitive tasks through practical Python utilities.

Features

* Batch filename preview
* File organisation planning
* SHA-256 file manifest generation
* Command-line interface
* Desktop graphical interface
* Automated testing

Supported Platforms

* Windows
* macOS

Requirements

Python 3.11 or newer.

Installation

git clone https://github.com/YOUR_USERNAME/keelkit-automation-toolkit.git
cd keelkit-automation-toolkit
python -m venv .venv

Activate the environment.

Windows:

.venv\Scripts\Activate.ps1

macOS:

source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run the Desktop Application

python -m keelkit.gui

Run the Command-Line Interface

python -m keelkit.cli rename ./documents --prefix archive
python -m keelkit.cli organise ./documents
python -m keelkit.cli manifest ./documents

Testing

pip install pytest
pytest

Development Philosophy

KEELKIT prioritises predictable behaviour, transparent operations, cross-platform compatibility and user control.

The initial release provides previews rather than automatically modifying or deleting user files.

Roadmap

* [x]	Initial automation engine
* [x]	CLI
* [x]	Desktop interface
* [x]	Initial automated tests
* [ ]	Safe file-operation execution
* [ ]	Duplicate detection
* [ ]	Workflow configuration
* [ ]	Exportable reports
* [ ]	Additional automation modules

Licence

MIT License.

Contributions

Bug reports, documentation improvements, testing and feature proposals are welcome.

KEELKIT is an evolving open-source project. Contributions and feedback are encouraged.
