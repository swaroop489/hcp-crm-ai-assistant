def format_hcp_name(name: str) -> str:
    if not name.lower().startswith("dr."):
        return f"Dr. {name}"
    return name
