from flask import Flask, render_template, request
import io
import base64
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/render", methods=["GET"])
def plotView():
    v1 = request.args.get('v1')
    v2 = request.args.get('v2')
    v3 = request.args.get('v3')
    return render_template("index.html", image=chartgenerator(v1,v2,v3),v1=v1,v2=v2,v3=v3)

def chartgenerator(v1 = 0,v2 = 0,v3 = 0):
    # Generate plot // inspired by https://gitlab.com/snippets/1924163
    fig = Figure()
    axis = fig.add_subplot(1,1,1)
    axis.set_title("Chart Generator from URL")
    axis.set_xlabel("x-axis")
    axis.set_ylabel("y-axis")
    axis.grid()
    axis.plot(range(1,4), [v1, v2, v3], "ro-")

    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    
    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    return pngImageB64String

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444, debug=True)