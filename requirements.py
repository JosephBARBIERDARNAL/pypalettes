import subprocess

packages = ["matplotlib", "pandas", "pre-commit", "pytest", "bs4"]
REQUIREMENTS_FILE = "requirements.txt"


def get_package_version(package_name: str) -> str:
    result = subprocess.run(
        ["pip", "show", package_name], capture_output=True, text=True
    )
    details = result.stdout.split("\n")
    for line in details:
        if line.startswith("Version: "):
            return line.split(" ")[1]
    return None


with open(REQUIREMENTS_FILE, "w") as file:
    for package in packages:
        version = get_package_version(package)
        if version:
            packageVersion = f"{package}=={version}"
            print(packageVersion)
            file.write(packageVersion + "\n")
        else:
            print(f"Version not found for package {package}")
