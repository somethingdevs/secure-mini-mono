import uvicorn

if __name__ == '__main__':
    uvicorn.run("main:app",
                host="0.0.0.0",
                port=8432,
                reload=True,
                ssl_certfile="./tls/ca-cert.pem",
                ssl_keyfile="./tls/ca-key.pem"
                )