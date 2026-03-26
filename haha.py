from flask import Flask, request

app = Flask(__name__)


@app.route("/lisaa_tieto", methods=["POST"])
def lisaa_tieto():
    vastaanottettu_data = request.get_json(force=True)
    print(vastaanottettu_data["mittaus"])
    return "200"


if __name__ == "__main__":
    app.run()