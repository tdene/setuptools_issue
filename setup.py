from setuptools import setup

setup(
        name="issue_test",
        package_dir={"":"src"},
        packages=["issue_test"],
        package_data={"issue_test":["test_data/*.v"]}
    )
