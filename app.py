from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.get("/")
def index():
    return render_template( "index.html" )

@app.get("/search")
def search():
    args = request.args.get( "q" )
    return redirect( f"https://google.com/search?q= {args} " )

@app.get("/lucky")
def lucky():
    args = request.args.get( "q" )
    return redirect( f"https://www.google.com/search?q={args}&btnI=&sourceid=navclient&gfns=1" )

if __name__ == "__main__":
    app.run()