import sys
import json
import subprocess
import threading
import uuid

class MCPClient:
    def __init__(self, command, args):
        self.process = subprocess.Popen(
            [command] + args,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )
        self.responses = {}
        self.lock = threading.Lock()
        self.running = True
        
        self.reader_thread = threading.Thread(target=self._read_loop, daemon=True)
        self.reader_thread.start()

    def _read_loop(self):
        while self.running:
            try:
                line = self.process.stdout.readline()
                if not line:
                    break
                msg = json.loads(line)
                if 'id' in msg:
                    with self.lock:
                        self.responses[msg['id']] = msg
            except Exception as e:
                print(f"Read error: {e}", file=sys.stderr)

    def _send(self, req):
        req_str = json.dumps(req)
        self.process.stdin.write(req_str + '\n')
        self.process.stdin.flush()

    def call(self, method, params=None):
        req_id = str(uuid.uuid4())
        req = {
            "jsonrpc": "2.0",
            "id": req_id,
            "method": method,
            "params": params or {}
        }
        self._send(req)
        
        # Wait for response
        import time
        start = time.time()
        while time.time() - start < 60:
            with self.lock:
                if req_id in self.responses:
                    return self.responses.pop(req_id)
            time.sleep(0.1)
        raise TimeoutError("No response from MCP server")

    def call_tool(self, tool_name, args=None):
        resp = self.call("tools/call", {
            "name": tool_name,
            "arguments": args or {}
        })
        if 'error' in resp:
            raise Exception(resp['error'])
        return resp.get('result')

    def shutdown(self):
        self.running = False
        self.process.terminate()

def run():
    client = MCPClient("C:\\Users\\shaii\\AppData\\Local\\Python\\pythoncore-3.14-64\\Scripts\\notebooklm-mcp.exe", [])
    try:
        # Initialize
        init_res = client.call("initialize", {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "TestClient", "version": "1.0.0"}
        })
        client._send({"jsonrpc": "2.0", "method": "notifications/initialized"})
        
        # Call tool: notebook_list
        res = client.call_tool("notebook_list")
        print(json.dumps(res, indent=2, ensure_ascii=False))
        
    finally:
        client.shutdown()

if __name__ == "__main__":
    run()
