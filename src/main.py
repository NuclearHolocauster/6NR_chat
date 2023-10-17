from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exception_handlers import http_exception_handler
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.staticfiles import StaticFiles


from di_container import Container
from controllers import chat_controller


def create_app() -> FastAPI:

    container = Container()
    container.config.from_yaml('config/config.yaml')
    app = FastAPI(
        title='6NR_chat',
        version='0.0.1',

    )
    container.wire(
        modules=[
            chat_controller,
        ]
    )
    
    app.container = container
    app.include_router(chat_controller.router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.mount("/static", StaticFiles(directory="static"), name="static")

    return app


app = create_app()


@app.on_event('startup')
async def startup() -> None:
    pass


@app.on_event('shutdown')
async def shutdown() -> None:
    pass


@app.exception_handler(StarletteHTTPException)
async def http_error_handler(
    request: Request,
    ex: Exception
) -> JSONResponse:

    return await http_exception_handler(request, ex)


@app.exception_handler(Exception)
async def internal_errors_handler(
    request: Request,
    exc: Exception
) -> JSONResponse:

    return JSONResponse(
        status_code=500,
        content={'detail': "Internal server error"}
    )
