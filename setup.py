# Read the current version from the file
with open('version.txt', 'r') as file:
    current_version = file.read().strip()

# Split the version into major, minor, and patch parts
major, minor, patch = map(int, current_version.split('.'))

# Increment the patch version
patch += 1

# Check for reset conditions
if patch == 10:
    patch = 0
    minor += 1

if minor == 10:
    minor = 0
    major += 1

# Create the new version string
new_version = f"{major}.{minor}.{patch}"

# Write the updated version back to the file
with open('version.txt', 'w') as file:
    file.write(new_version)

setup(
    name='ellinet13s-lib',
    version=new_version,
    author='ElliNet13',
    author_email='ellinet13@googlegroups.com',
    description='A library made by ElliNet13',
    long_description='This library was made by ElliNet13 and will stay like that.',
    long_description_content_type='text/markdown',
    url='https://github.com/ElliNet13/ellinet13s-lib',
    packages=['ellinet13s-lib'],
    classifiers=[
        
    ],
    install_requires=[
        'wheel'
    ],
)
