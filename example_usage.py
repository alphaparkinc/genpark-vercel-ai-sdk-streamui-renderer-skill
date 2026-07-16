from client import VercelStreamUiRendererClient
client = VercelStreamUiRendererClient()
print(client.render_component("ProductCard", {"price": "99", "title": "Zenith Earbuds"}))