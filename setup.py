from setuptools import setup, find_namespace_packages

setup(
        name="issue_test",
        package_dir={"":"src"},
        packages=find_namespace_packages(where="src"),
        package_data={"issue_test":["test_data/*.txt"]}
    )
