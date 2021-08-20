#!/usr/bin/env python3
from ghidra_bridge import GhidraBridge
from ipykernel.ipkernel import IPythonKernel

class GhidraKernel(IPythonKernel):
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
            print("Connecting to the bridge")
            self._bridge = GhidraBridge(namespace=self.shell.user_ns, # from IPythonKernel
                interactive_mode=True,
                hook_import=True)
            return self._bridge
        else:
            return self._bridge
            
    _banner: str = None
    @property
    def banner(self):
        if self._banner is None:
            self._banner = "Ghidra Python3 Kernel (connected to {host}:{port})".format(host=self.bridge.client.host, port=self.bridge.client.port)
            return self._banner
        else:
            return self._banner
            
    def __init__(self, **kwargs):
        print("Starting GhidraKernel...")
        super(GhidraKernel, self).__init__(**kwargs)
        self.shell.user_ns["bridge"] = self.bridge            
    
    def do_shutdown(self, restart):
        # We probably don't want to _actually_
        # shut down the server within Ghidra
        # self.bridge.remote_shutdown()
        self._bridge = None
        
        super(GhidraKernel, self).do_shutdown(restart)
        
        if restart:
            _ = self.bridge
        return {
            'status': 'ok',
            'restart': restart
        }    
    
if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=GhidraKernel)
