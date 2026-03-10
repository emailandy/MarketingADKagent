import http.server
import socketserver
import json
import os
import sys
import asyncio

# Fix sys.path to include ADK source and marketing-agency root
current_dir = os.path.dirname(os.path.abspath(__file__))
adk_src = os.path.abspath(os.path.join(current_dir, '../ADK/src'))

sys.path.insert(0, current_dir)
sys.path.insert(0, adk_src)

# Authentication Configuration
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"
os.environ["GOOGLE_CLOUD_PROJECT"] = "nodepeel"
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"

from backend.agents.marketing_manager import marketing_manager
from google.adk.runners import InMemoryRunner
from google.genai import types

PORT = 8080
SESSION_ID = "marketing_session_123"

# Global Runner to persist session state in memory
runner = InMemoryRunner(
    agent=marketing_manager,
    app_name="MarketingDepartment"
)
runner.auto_create_session = True

class MarketingAgencyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.ui_dir = os.path.join(current_dir, 'frontend', 'ui')
        super().__init__(*args, directory=self.ui_dir, **kwargs)

    def do_GET(self):
        if self.path == '/':
            self.path = '/templates/index.html'
        return super().do_GET()

    def do_POST(self):
        if self.path == '/api/chat':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                message = data.get('message', '')
                
                response_text = self.run_agent_sync(message)
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = json.dumps({'response': response_text})
                self.wfile.write(response.encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                error_resp = json.dumps({'error': str(e)})
                self.wfile.write(error_resp.encode('utf-8'))
        else:
            self.send_error(404, "Not Found")

    def run_agent_sync(self, user_message: str) -> str:
        return asyncio.run(self._run_agent(user_message))

    async def _run_agent(self, user_message: str) -> str:
        content = types.Content(
            role='user',
            parts=[types.Part.from_text(text=user_message)]
        )
        
        response_text = ""
        async for event in runner.run_async(
            user_id="default_user",
            session_id=SESSION_ID,
            new_message=content
        ):
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        response_text += part.text
        return response_text

if __name__ == "__main__":
    print(f"Starting Marketing Department Agency on http://localhost:{PORT}")
    try:
        with socketserver.TCPServer(("", PORT), MarketingAgencyHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
