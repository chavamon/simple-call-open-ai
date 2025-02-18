# Step 1: Check if the required packages are installed
required_packages = [
    "python-dotenv", "openai"
]

missing_packages = []

for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        missing_packages.append(package)
