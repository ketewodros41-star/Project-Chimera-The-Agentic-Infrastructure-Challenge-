import os
import functools
from typing import Optional, Dict
import time

# Dimension 4: Agentic Commerce Safety
# Redis-backed/In-memory daily spend tracking
DAILY_SPEND = 0.0
MAX_DAILY_LIMIT = 500.0

def budget_check(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        amount = kwargs.get('amount', args[2] if len(args) > 2 else 0.0)
        global DAILY_SPEND
        if DAILY_SPEND + amount > MAX_DAILY_LIMIT:
            print(f"❌ [CFO_REJECT] Transaction of {amount} exceeds MAX_DAILY_LIMIT ({MAX_DAILY_LIMIT}). Current Spend: {DAILY_SPEND}")
            raise Exception("BudgetExceededError: Transaction rejected by CFO sub-agent.")
        return await func(*args, **kwargs)
    return wrapper

class CommerceManager:
    def __init__(self):
        self.api_key_name = os.getenv("CDP_API_KEY_NAME")
        self.api_key_private_key = os.getenv("CDP_API_KEY_PRIVATE_KEY")
        self.wallet_provider = "MOCK_PROVIDER" if self.api_key_name else None

    async def get_wallet_balance(self, asset: str = "usdc") -> float:
        """SRS §4.5 FR 5.1: Check balance before transaction."""
        print(f"Fetching {asset} balance via MCP...")
        return 1000.0

    @budget_check
    async def send_payment(self, to_address: str, amount: float, asset: str = "usdc") -> bool:
        """
        Dimension 4: CFO Judge sub-agent rejection logic via decorator.
        """
        balance = await self.get_wallet_balance(asset)
        if balance < amount:
            print(f"❌ [INSUFFICIENT_FUNDS] Balance {balance} < {amount}")
            return False

        print(f"✅ [COMMERCE_APPROVED] Executing {amount} {asset} to {to_address}")
        global DAILY_SPEND
        DAILY_SPEND += amount
        return True

if __name__ == "__main__":
    import asyncio
    manager = CommerceManager()
    try:
        asyncio.run(manager.send_payment("0x123", 100.0))
        asyncio.run(manager.send_payment("0x456", 450.0)) # Should trigger CFO reject
    except Exception as e:
        print(e)
