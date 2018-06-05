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
  return e.value
}
