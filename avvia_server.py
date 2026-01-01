#!/usr/bin/env python3
"""
Script per testare la bibliografia localmente
Avvia un server web semplice per evitare problemi CORS
"""

import http.server
import socketserver
import webbrowser
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Aggiungi header CORS per permettere il caricamento del CSV
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def start_server():
    handler = MyHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print("=" * 60)
        print("🚀 SERVER AVVIATO!")
        print("=" * 60)
        print(f"\n📂 Cartella: {os.getcwd()}")
        print(f"🌐 URL: http://localhost:{PORT}/bibliografia_ricercabile_csv.html")
        print("\n💡 Il browser si aprirà automaticamente...")
        print("\n⚠️  Per fermare il server: premi Ctrl+C")
        print("=" * 60)
        
        # Apri automaticamente il browser
        webbrowser.open(f'http://localhost:{PORT}/bibliografia_ricercabile_csv.html')
        
        # Avvia il server
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n✅ Server fermato. Arrivederci!")

if __name__ == "__main__":
    start_server()
