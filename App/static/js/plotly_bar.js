d3.json("/cmovies").then(function(data) {
  // Create the Trace
  var trace1 = {
    x: data.bechdel_rating,
    y: data.dom_gross,
    type: "bar",
    name: "Avg. Domestic Gross",
    marker: {
      color: '#ee3ec9'
    },
    transforms: [{
      type: 'aggregate',
      groups: data.bechdel_rating,
      aggregations: [
        {target: 'y', func: 'avg', enabled: true},
      ]
    }]
  };

  var trace2 = {
    x: data.bechdel_rating,
    y: data.int_gross,
    type: "bar",
    name:"Avg. International Gross",
    marker: {
      color: '#ff6e4e'
    },
    transforms: [{
      type: 'aggregate',
      groups: data.bechdel_rating,
      aggregations: [
        {target: 'y', func: 'avg', enabled: true},
      ]
    }]
  };

  var trace3 = {
    x: data.bechdel_rating,
    y: data.budget,
    type: "bar",
    name:"Avg. Budget",
    marker: {
      color: '#f3ff13'
    },
    transforms: [{
      type: 'aggregate',
      groups: data.bechdel_rating,
      aggregations: [
        {target: 'y', func: 'avg', enabled: true},
      ]
    }]
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
