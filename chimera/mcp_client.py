import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from typing import Dict, Any, Optional

class MCPClient:
    def __init__(self, server_path: str, server_args: list = []):
        self.server_params = StdioServerParameters(
            command="python",
            args=[server_path] + server_args
        )
        self.session: Optional[ClientSession] = None
        self._exit_stack = None

    async def connect(self):
        print(f"Connecting to MCP server...")
        self._exit_stack = asyncio.ExitStack()
        read, write = await self._exit_stack.enter_async_context(stdio_client(self.server_params))
        self.session = await self._exit_stack.enter_async_context(ClientSession(read, write))
        await self.session.initialize()
        print("MCP Session initialized.")

    async def list_tools(self):
        if not self.session:
            raise RuntimeError("Session not connected")
        tools = await self.session.list_tools()
        return tools

    async def call_tool(self, tool_name: str, arguments: Dict[str, Any]):
        if not self.session:
            raise RuntimeError("Session not connected")
        print(f"Calling MCP Tool: {tool_name} with {arguments}")
        result = await self.session.call_tool(tool_name, arguments)
        return result

    async def disconnect(self):
        if self._exit_stack:
            await self._exit_stack.aclose()
            print("MCP Session disconnected.")

async def test_client():
    # This is a placeholder for testing with a real server
    # client = MCPClient("path/to/server.py")
    # await client.connect()
    # tools = await client.list_tools()
    # print(tools)
    # await client.disconnect()
    pass

if __name__ == "__main__":
    asyncio.run(test_client())
