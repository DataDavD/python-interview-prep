from typing import Optional


def hello(s: Optional[str] = None) -> str:
    if not s:
        return "Hello, World!"
    return f"Hello, {s}!"
