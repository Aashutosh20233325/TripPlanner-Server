import contextlib
from fastapi import FastAPI
from Events_mcp_server import mcp as Events_mcp
from Map_mcp_server import mcp as Map_mcp
from Weather_mcp_server import mcp as Weather_mcp
from config import PORT


# Create a combined lifespan to manage both session managers
@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    async with contextlib.AsyncExitStack() as stack:
        await stack.enter_async_context(Events_mcp.session_manager.run())
        await stack.enter_async_context(Map_mcp.session_manager.run())
        await stack.enter_async_context(Weather_mcp.session_manager.run())
        yield


app = FastAPI(lifespan=lifespan)
app.mount("/events", Events_mcp.streamable_http_app())
app.mount("/map", Map_mcp.streamable_http_app())
app.mount("/weather", Weather_mcp.streamable_http_app())



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)
