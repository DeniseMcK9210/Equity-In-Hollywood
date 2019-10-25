
d3.json("/cmovies").then(function(data) {
  // Create the Trace
  var trace1 = {
    x: data.bechdel_rating,
    y: data.dom_gross,
    type: "bar",
    name: "Domestic Gross"
  };

  var trace2 = {
    x: data.bechdel_rating,
    y: data.int_gross,
    type: "bar",
    name:"International Gross"
  };

  // Create the data array for the plot
  var data = [trace1];

  // Define the plot layout
  var layout = {
    title: "Bechdel Binary Test v Domestic Gross",
    xaxis: { title: "Binary Test" },
    yaxis: { title: "Domestic Gross ($)" }
  };

  // Plot the chart to a div tag with id "bar-plot"
  Plotly.newPlot("viz1", data, layout);

}).catch(error => console.log(error)); 
