from flask import Flask, jsonify, render_template
import pandas as pd
import json
import re

app = Flask(__name__)

@app.route("/")
def index():
    """returns dashboard homepage"""
    return render_template('index.html')




@app.route("/names")
def names():
# Read in CSV to DF
    namesdf = pd.read_csv('./data/belly_button_biodiversity_samples.csv')
    nameList = namesdf.columns.values[1:]
    return jsonify(nameList.tolist())




@app.route('/otu')
def otu():
# Read in CSV to DF
    otudf = pd.read_csv('./data/belly_button_biodiversity_otu_id.csv')
    return jsonify(otudf['lowest_taxonomic_unit_found'].tolist())




@app.route('/metadata/<sample>')
def metadata(sample):
    if not sample.isdigit():
        return("<h1>Not a digit</h1>")

    samplesdf = pd.read_csv('./data/Belly_Button_Biodiversity_Metadata.csv')
    resultantdf = samplesdf[samplesdf['SAMPLEID'] == int(sample)]
    returnResult = {
        "AGE": resultantdf['AGE'].values[0].item(),
        "BBTYPE": resultantdf['BBTYPE'].values[0],
        "ETHNICITY": resultantdf['ETHNICITY'].values[0],
        "GENDER": resultantdf['GENDER'].values[0],
        "LOCATION": resultantdf['LOCATION'].values[0],
        "SAMPLEID": resultantdf['SAMPLEID'].values[0].item()
    }
    return jsonify(returnResult)




@app.route('/wfreq/<sample>')
def wfreq(sample):
    bbdf = pd.read_csv('./data/Belly_Button_Biodiversity_Metadata.csv')
    searchedRow = bbdf[bbdf['SAMPLEID'] == int(sample)]
    print(int(searchedRow['WFREQ'].values[0]))
    return jsonify(int(searchedRow['WFREQ'].values[0]))




@app.route('/samples/<sample>')
def samples(sample):
    samples = pd.read_csv('./data/belly_button_biodiversity_samples.csv')
    s = sample
    # return render_template('index.html')
    resultantdf = samples.loc[ samples[s] > 0, [s, 'otu_id']]
    returnDict = [
        {
            "otu_ids": resultantdf[s].tolist()
        },
        {
            "sample_Values": resultantdf['otu_id'].values.tolist()
        }
    ]
    return jsonify(returnDict)

if __name__ == "__main__":
    app.run(debug=True)
