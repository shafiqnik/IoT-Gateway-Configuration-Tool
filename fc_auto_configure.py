#Source example https://www.uvicorn.org/

import uvicorn

async def app(scope, receive, send):
    print('running the fc_auto_configure.py')

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, log_level = "info")