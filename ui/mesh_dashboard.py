# CONTRACT: system_state -> http_server -> 3d_mesh_visualizer
# Purpose: 3D interactive God View of the Stretford Mesh.

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MeshDashboardHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        node_data = {
            "node": "29", "status": "SOVEREIGN", "mesh_peers": 15
        }

        # The 3D Payload (HTML + Three.js)
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Sovereign Mesh - God View</title>
            <style>
                body {{ margin: 0; overflow: hidden; background-color: #050505; color: #228b22; font-family: monospace; }}
                #hud {{ position: absolute; top: 20px; left: 20px; z-index: 10; pointer-events: none; text-shadow: 0 0 5px #000; }}
                h1 {{ margin: 0; font-size: 24px; color: #fff; letter-spacing: 2px; }}
                .glitch {{ color: #ff3333; display: none; }}
            </style>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        </head>
        <body>
            <div id="hud">
                <h1>🏺 STRETFORD MESH: GOD VIEW</h1>
                <p>NODE: {node_data['node']} | STATUS: <span style="color:#00ff00;">{node_data['status']}</span> | PEERS: {node_data['mesh_peers']}</p>
                <p>> 10^47 Neural Swarm Active.</p>
            </div>
            
            <script>
                // 1. Setup Scene
                const scene = new THREE.Scene();
                // Add some dark fog for depth
                scene.fog = new THREE.FogExp2(0x050505, 0.002);

                const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
                const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
                renderer.setSize(window.innerWidth, window.innerHeight);
                document.body.appendChild(renderer.domElement);

                // 2. Create the Swarm (Nodes)
                const nodes = [];
                const geometry = new THREE.SphereGeometry(2, 16, 16);
                const material = new THREE.MeshBasicMaterial({{ color: 0x228b22, wireframe: true }}); // Pine Green

                for(let i = 0; i < 25; i++) {{
                    const sphere = new THREE.Mesh(geometry, material);
                    sphere.position.x = (Math.random() - 0.5) * 200;
                    sphere.position.y = (Math.random() - 0.5) * 200;
                    sphere.position.z = (Math.random() - 0.5) * 200;
                    
                    // Make Node 29 stand out
                    if (i === 0) {{
                        sphere.scale.set(3, 3, 3);
                        sphere.material = new THREE.MeshBasicMaterial({{ color: 0xffffff, wireframe: true }});
                    }}
                    
                    scene.add(sphere);
                    nodes.push(sphere);
                }}

                // 3. Create Connections (Lines)
                const lineMaterial = new THREE.LineBasicMaterial({{ color: 0x114411, transparent: true, opacity: 0.5 }});
                const lines = [];
                
                for(let i=0; i < nodes.length; i++) {{
                    for(let j=i+1; j < nodes.length; j++) {{
                        // Only connect if they are close enough
                        if(nodes[i].position.distanceTo(nodes[j].position) < 80) {{
                            const points = [];
                            points.push(nodes[i].position);
                            points.push(nodes[j].position);
                            const lineGeo = new THREE.BufferGeometry().setFromPoints(points);
                            const line = new THREE.Line(lineGeo, lineMaterial);
                            scene.add(line);
                            lines.push({{ line: line, n1: nodes[i], n2: nodes[j] }});
                        }}
                    }}
                }}

                camera.position.z = 150;

                // 4. Animate the Swarm
                function animate() {{
                    requestAnimationFrame(animate);
                    
                    // Rotate entire scene slowly
                    scene.rotation.y += 0.001;
                    scene.rotation.x += 0.0005;

                    // Pulse the nodes slightly
                    nodes.forEach(node => {{
                        node.rotation.x += 0.01;
                        node.rotation.y += 0.01;
                    }});

                    // Keep lines attached to nodes
                    lines.forEach(link => {{
                        const positions = link.line.geometry.attributes.position.array;
                        positions[0] = link.n1.position.x; positions[1] = link.n1.position.y; positions[2] = link.n1.position.z;
                        positions[3] = link.n2.position.x; positions[4] = link.n2.position.y; positions[5] = link.n2.position.z;
                        link.line.geometry.attributes.position.needsUpdate = true;
                    }});

                    renderer.render(scene, camera);
                }}

                // Handle Window Resize
                window.addEventListener('resize', () => {{
                    camera.aspect = window.innerWidth / window.innerHeight;
                    camera.updateProjectionMatrix();
                    renderer.setSize(window.innerWidth, window.innerHeight);
                }});

                animate();
            </script>
        </body>
        </html>
        """
        self.wfile.write(bytes(html, "utf8"))

def run_dashboard(server_class=HTTPServer, handler_class=MeshDashboardHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"[DASHBOARD] Serving 3D God View at http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run_dashboard()
