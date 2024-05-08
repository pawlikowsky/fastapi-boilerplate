import os

import uvicorn

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="FastAPI Project")
    parser.add_argument("--host", default="0.0.0.0", help="Host address")
    parser.add_argument("--port", type=int, default=8080, help="Port number")
    parser.add_argument("--reload", action="store_true", help="Enable auto-reload")
    parser.add_argument("--workers", type=int, default=1, help="Number of worker processes")
    parser.add_argument("--config", type=str, default="development", help="Load config")
    args = parser.parse_args()

    os.environ.setdefault("FASTAPI_CONFIG", str(args.config))
    print(f"CONFIG: {args.config}")

    uvicorn.run(
        "core.app:app",
        host=args.host,
        port=args.port,
        reload=args.reload,
        workers=args.workers,
    )
