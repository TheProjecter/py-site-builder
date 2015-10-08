# Short Description #

This is simple python-based builder for a site.


# Features #

  * Getting source code of your project from a repository
  * Renaming static data (for example css/js) to resolve _browser cache problem_ (to reload these files each time after building)
  * Custom minimization of _javascript_ and _html_ files


# Dependencies #
Requires **jstools** (http://pypi.python.org/pypi/JSTools/) to be installed.


# How to use #

Edit **config.py** to custom builder settings. Then **run** from command line: **python build.py**.