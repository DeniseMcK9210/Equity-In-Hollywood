
d3.json("/cmovies").then(function(data) {
  //var arrAvg = arr => arr.reduce((a,b) => a + b, 0) / arr.length
  // Create the Trace
  var trace1 = {
    x: data.bechdel_rating,
    y: data.dom_gross,
    type: "bar",
    name: "Domestic Gross",
    marker: {
      color: '#ee3ec9'
    }
  };

  var trace2 = {
    x: data.bechdel_rating,
    y: data.int_gross,
    type: "bar",
    name:"International Gross",
    marker: {
      color: '#ff6e4e'
    }
  };

  var trace3 = {
    x: data.bechdel_rating,
    y: data.budget,
    type: "bar",
    name:"Budget",
    marker: {
      color: '#f3ff13'
    }
  };


  // Create the data array for the plot
  var data = [trace3, trace1,trace2];

  // Define the plot layout
  var layout = {
    xaxis: { title: "Bechdel Test" },
    yaxis: { title: "Gross ($ 2013)" }
  };

  // Plot the chart to a div tag with id "bar-plot"
  Plotly.newPlot("viz1", data, layout);

}).catch(error => console.log(error)); 
