from __future__ import annotations
from fastmcp import FastMCP

mcp = FastMCP("math")

def _as_number(x):
    """ Accept integers/floats or numeric strings; raise TypeError otherwise. """
    if isinstance(x, (int, float)):
        return float(x)
    if isinstance(x, str):
        return float(x.strip())
    raise TypeError(f"Expected int, float, or numeric string, got {type(x)}")

@mcp.tool()
async def add(a: float, b: float) -> float:
    """ Return the sum of two numbers. """
    a = _as_number(a)
    b = _as_number(b)
    return a + b

@mcp.tool()
async def subtract(a: float, b: float) -> float:
    """ Return the difference of two numbers. """
    a = _as_number(a)
    b = _as_number(b)
    return a - b

@mcp.tool()
async def multiply(a: float, b: float) -> float:
    """ Return the product of two numbers. """
    a = _as_number(a)
    b = _as_number(b)
    return a * b

@mcp.tool()
async def divide(a: float, b: float) -> float:
    """ Return the quotient of two numbers. """
    a = _as_number(a)
    b = _as_number(b)
    return a / b

@mcp.tool()
async def power(base: float, exponent: float) -> float:
    """ Return the base raised to the exponent power. """
    base = _as_number(base)
    exponent = _as_number(exponent)
    return base ** exponent

@mcp.tool()
async def modulus(a: float, b: float) -> float:
    """ Return the modulus of two numbers. """
    a = _as_number(a)
    b = _as_number(b)
    return a % b

@mcp.tool()
async def root(a: float, b: float) -> float:
    """ Return the nth root of a number. """
    a = _as_number(a)
    b = _as_number(b)
    return a ** (1 / b)

if __name__ == "__main__":
    mcp.run()