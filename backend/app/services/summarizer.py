def generate_basic_summary(topics: str, sentiment: str) -> str:
    """
    Fallback basic summary generator.
    """
    return f"Discussed: {topics}. Overall sentiment was {sentiment}."
