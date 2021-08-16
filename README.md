# Ghidra Notebook

Ghidra Notebook is a [Jupyter](https://jupyter.org)
[kernel](https://jupyter.readthedocs.io/en/latest/projects/kernels.html)
that combines the flexibility of Ghidra's API with the Jupyter notebook
system to create reproducable, scriptable notes.

This allows you to create notes that can also be run
to show both your thinking and your work.

# Installation

This project depends on the (excellent) ghidra-bridge
project. You'll need to
[install Ghidra Bridge](https://github.com/justfoxing/ghidra_bridge#install-the-ghidra-bridge-package-and-server-scripts) before you can use ghidra-notebook.

```bash
# Install the package
pip3 install --user .
# Install the iPython kernel
python3 -m ghidra-notebook.install
```

You can use any Jupyter notebook client you like!
See [install Jupyter](https://jupyter.org/install.html)
for setting these up.

# Usage

[Start the ghidra-bridge server](https://github.com/justfoxing/ghidra_bridge#start-server).
When you start the Ghidra kernel in Jupyter it will connect to ghidra-bridge and you'll have
access to the Ghidra API in whatever context the bridge was started in.

Once ghidra-bridge is started, you can launch a Jupyter Lab and select "Ghidra" to start the
kernel, and connect to ghidra-bridge.

To run Jupyter lab:

```bash
pip install jupyterlab
jupyter-lab
```

Or launch directly in the terminal
```bash
jupyter console --kernel ghidra
```

Once you're in the Jupyter shell, try something like:

```python3
print(currentProgram)
print(currentAddress)
```

You'll have access to the
[FlatAPI](https://ghidra.re/ghidra_docs/api/ghidra/program/flatapi/FlatProgramAPI.html)
along with the rest of the Ghidra API, just as you would in the normal Ghidra python terminal,
except thanks to Ghidra Bridge you'll have Python3.
