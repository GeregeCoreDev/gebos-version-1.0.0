"""
Core ERP module exports
"""

from .finance import Finance
from .hr import HR
from .inventory import Inventory
from .sales import Sales
from .production import Production

__all__ = ['Finance', 'HR', 'Inventory', 'Sales', 'Production']
