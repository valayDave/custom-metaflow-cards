from setuptools import find_packages, setup

def get_long_description() -> str:
    with open("README.md") as fh:
        return fh.read()

setup(
    name="metaflow_cards_model_scorecard",
    version="1.0.1",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Valay Dave",
    author_email="valaygaurang@gmail.com",
    license="Apache Software License 2.0",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)