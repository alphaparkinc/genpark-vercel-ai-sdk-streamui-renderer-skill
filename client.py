class VercelStreamUiRendererClient:
    def render_component(self, component_name: str, component_props: dict) -> dict:
        props_str = " ".join([f"{k}='{v}'" for k, v in component_props.items()])
        return {"rendered_ui_markup": f"<{component_name} {props_str} /> [StreamUI Rendered]"}