#!/usr/bin/env python3
"""Mini serveur local : sert la page et lance vraiment la commande via `claude -p`.
Usage : python3 server.py   puis ouvrir http://localhost:8765
Prérequis : Claude Code installé + le plugin du dossier ../clone-dir/instagram-agent-skill
"""
import json, os, re, subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
SKILLS_DIR = os.path.join(HERE, "..", "clone-dir", "instagram-agent-skill")
ALLOWED = re.compile(r"^/ig-(reel|caption|carousel|story|plan|profile|viral|audit|comment|reply|dm|repurpose|human)\b")

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        body = open(os.path.join(HERE, "index.html"), "rb").read()
        self.send_response(200); self.send_header("Content-Type", "text/html; charset=utf-8"); self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        data = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        cmd = data.get("command", "")
        if not ALLOWED.match(cmd):  # seulement les 13 skills
            self.send_response(400); self.end_headers(); return
        try:
            out = subprocess.run(["claude", "--plugin-dir", SKILLS_DIR, "--allowedTools", "Bash(python3:*)", "-p", cmd],
                                 capture_output=True, text=True, timeout=300, cwd=HERE).stdout or "(aucune réponse)"
        except Exception as e:
            out = f"Erreur : {e}"
        self.send_response(200); self.send_header("Content-Type", "application/json"); self.end_headers()
        self.wfile.write(json.dumps({"output": out}).encode())

HTTPServer(("127.0.0.1", 8765), H).serve_forever()
