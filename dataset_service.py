from flask import Flask
import manager.dataset_manager as dm

app = Flask(__name__)

pixels, labels, dates = dm.get_dataset()


@app.route("/dataset/")
def data_set():
    return {"pixels": pixels.tolist(), "labels": labels.tolist(), "dates": dates}


if __name__ == "__main__":
    app.run()
