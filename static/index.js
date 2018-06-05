window.onload = (e) => {
  populateSampleNames();

}

let populateSampleNames = () => {
  let array;
  Plotly.d3.json('/names', (error, data) => {
    if(error){
      console.log(error);
    } else {
        data.forEach( element => {
            let option = document.createElement("option");
            let t = document.createTextNode(element);
            option.appendChild(t);
            document.getElementById("inputGroupSelect01").appendChild(option);
        });
    }
  });
}

let onSampleChange = (e) => {
  console.log("Changed to: ", e.value);

  // Code that draws graph
  Plotly.d3.json(`/samples/${e.value}`, (error, data) => {
    if (error) {
        console.log(error);
    } else {
        // Plotly.d3.json('/otu', (error, otudata) => {
        //     console.log(data);
        //     console.log(otudata);
        // })
        graphData = [{
          values: data[1].sample_Values.slice(0,10),
          labels: data[0].otu_ids.slice(0,10),
          type: "pie"
        }]
        layout = {
          paper_bgcolor: '#AED9DA',
          width: '425',
          height: '425'
        }

        console.log(graphData);

        Plotly.newPlot('plotGraph', graphData, layout);
    }
  })
}
