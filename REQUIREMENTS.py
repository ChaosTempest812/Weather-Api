# Must have pip downloaded
commands = ["pip install requests"]

# If pip is downloaded, check the current version
commands = ["pip --version"]

# If your pip is below the requirement (see prerequisites.py), update pip
commands = ["pip install --upgrade pip"]
