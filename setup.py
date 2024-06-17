from setuptools import setup, find_packages;
import argparse;

with open("README.md", "r") as fh:
    readMe = fh.read();

with open("requirements.txt") as f:
    required = f.read().splitlines();

with open("version.txt", "r") as fh:
    versionFile = fh.read().strip();

optional_dependencies = {
    "All": [],
    "Graphics": [
        "tkcalendar==1.6.1"
    ],
    "PdfManager": [
        "reportlab==4.2.0",
        "pypdf==4.2.0"
    ],
    "XmlManager": [
        "lxml==5.2.2"
    ],
    "AdvancedUtils": [
        "codicefiscale==0.9"
    ]
}

parser = argparse.ArgumentParser()
parser.add_argument("--feature", action="append", help="Libraries Needed (comma-separated)")
args, unknown = parser.parse_known_args()
libraries = args.library

installRequiresCustom = required;
if libraries:
    for library in libraries:
        if library in optional_dependencies:
            if library == "All":
                for lib,dep in optional_dependencies:
                    installRequiresCustom.extend(dep);
            else:
                installRequiresCustom.extend(optional_dependencies[library]);

setup(
    name='almax_common',
    version=versionFile,
    description='Library with my most used Classes and Methods',
    long_description=readMe,
    long_description_content_type='text/markdown',
    author='AlMax98',
    author_email='alihaider.maqsood@gmail.com',
    packages=find_packages(),
    package_dir={'': '.'},
    install_requires=installRequiresCustom,
);