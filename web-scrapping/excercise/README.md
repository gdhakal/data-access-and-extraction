# Implement Web Scrapping using Python

We can collect data from any website on the Internet for analysis such as: 

- Show the best deals and rank them.
- Web scrape reviews from online store.
- Web scrape game stats and players record.
- Get info about somebody from Wikipedia.

The website needs to have a standardized design for us to navigate through html tree.

# Tools

- [Anaconda](https://docs.anaconda.com/anaconda/install/mac-os/)
	- Use command line installer to work from terminal. Make sure to verify the data integrity of Anaconda installer files with SHA-256 before installation.
		1) change directory to the file downloaded directory
		2) run `shasum -a 256 filename Anaconda3-2020.02-MacOSX-x86_64.sh`
		3) verify the sha256 output with the value shown [here](https://docs.anaconda.com/anaconda/install/hashes/mac-3-cli/) for the given installer.
		4) Install using the command: `bash Anaconda3-2020.02-MacOSX-x86_64.sh`
		5) Stand by when the installation happens. When the installer prompts "Do you wish the installer to initialize Anaconda3 by running conda init?" Choose yes. If you missed this step, update the installation with `bash Anaconda3-2020.02-MacOSX-x86_64.sh -u`
		6) Verify anaconda installation: Restart terminal and type command `conda list` or `python`. To exit the Python shell, enter the command `quit()`.
- Sublime Text Editor
	- Command + N, Command + Shift + P, `Set Sytanx: Python`.
- [JavaScript Beautifier](https://beautifier.io/)

# Components

- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/) package: Parse or traverse html text within Python.
	- Install: `pip install bs4`
	- Verify:
		- Type `python`
		- Type `import bs4` => It should not throw an error.
- Web client to grab content from the Internet.
  URL Lib package > Request module > URL open function.


# Source

Everything implemented in this exercise is from the [source](https://www.youtube.com/watch?v=XQgXKtPSzUI&ab_channel=DataScienceDojo).


