#!/usr/bin/env python3
from ghidra_bridge import GhidraBridge
from ipykernel.kernelbase import Kernel
import logging
import traceback
from io import StringIO
from contextlib import redirect_stdout

class GhidraKernel(Kernel):
    implementation = 'ghidra_kernel'
    implementation_version = '1.0.0'
    language_info = {
        'name': 'Ghidra Python',
        'mimetype': 'text/x-python3',
        'file_extension': '.py',
        'pygments_lexer': 'python3',
        'codemirror_mode': 'Python',
    }
    help_links = [
        {'text': "Ghidra", 'url': "https://ghidra-sre.org"},
        {'text': "Ghidra Bridge", "url": "https://github.com/justfoxing/ghidra_bridge"},
        {"text": "Ghidra API", "url": "https://ghidra.re/ghidra_docs/api/ghidra/program/flatapi/FlatProgramAPI.html"}
    ]

    _bridge: GhidraBridge = None
    @property
    def bridge(self):
        if self._bridge is None:
            # Reset any state
            self._globals = {}
            self._locals = {}
            print("Connecting to the bridge")
            self._bridge = GhidraBridge(namespace=self._globals,
                interactive_mode=True,
                hook_import=True)
            return self._bridge
        else:
            return self._bridge
    _banner: str = None
    @property
    def banner(self):
        if self._banner is None:
            self._banner = "Ghidra Python3 Kernel"
            return self._banner
        else:
            return self._banner
    _globals: dict = {}
    _locals: dict = {}


    def __init__(self, **kwargs):
        print("Starting GhidraKernel...")
        Kernel.__init__(self, **kwargs)
        _  = self.bridge

    def do_execute(self, code, silent, store_history=True, user_expressions=None, allow_stdin=False):
        _ = self.bridge
        out_buff = StringIO()
        try: 
            with redirect_stdout(out_buff):
                exec(code, self._globals, self._locals)
            result = out_buff.getvalue()
            content = {
                'name': 'stdout',
                'text': str(result)
            }
        except Exception as e:
            result = traceback.format_exc()
            content = {'name': 'stderr', 'text': str(result)}
        self.send_response(self.iopub_socket, 'stream', content)

        return {
            'status': 'ok',
            'execution_count': self.execution_count,
            'payload': [],
            'user_expressions': {}
        }

    def do_shutdown(self, restart):
        # We probably don't want to _actually_
        # shut down the server within Ghidra
        # self.bridge.remote_shutdown()
        self._bridge = None
        self._locals = {}
        self._globals = {}
        
        if restart:
            _ = self.bridge
        return {
            'status': 'ok',
            'restart': restart
        }
if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=GhidraKernel)
