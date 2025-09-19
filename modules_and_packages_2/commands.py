# Create virtual env.
# >>> python -m venv [your-env-name]

# Activate/Deactivate the virtual env.

# Activate:
# >>> [your-env-name]\Scripts\activate
# (myvenv) ....\modules_and_packages_2>

# Deactivate:
# (myvenv) ....\modules_and_packages_2>
# [your-env-name]\Scripts\deactivate

# Check installed modules and packages 
# >>> pip list
# Package Version
# ------- -------
# pip     25.0.1

# >>> pip freeze
# pillow==11.3.0

# Install modules and packages
# >>> pip install [module-package-name]

# Managing Packages: Beyond installation, PIP can also be used to upgrade, downgrade, or uninstall packages.

# >>> pip install --upgrade package_name
# >>> pip uninstall package_name


# Install modules and packages inside the requirements.txt
# >>> pip freeze > requiremets.txt

# Install modules and packages from requirements.txt file
# >>> pip install -r requirements.txt