import importlib.resources

def pkg_test():
    with importlib.resources.path("issue_test.test_data","data.txt") as pkg_file:
        print("Successful")

if __name__ == "__main__":
    raise RuntimeError("This file is importable, but not executable")
