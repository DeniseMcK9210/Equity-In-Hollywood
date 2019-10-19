//Fill title select boxes(function)
function titles(data) {
    // Grab a reference to the dropdown select elements
    var title1 = d3.select("#title1-input");
    var title2 = d3.select("#title2-input");
  
    //Define lists of genres and decades
    var titles = data.title;

    //Options for title 1
    titles.forEach((t) => {
        title1
        .append("option")
        .text(t)
        .property("value", t);
    });

    //Options for title2
    titles.forEach((tt) => {
        title2
            .append("option")
            .text(tt)
            .property("value", tt);
        });
  }


//Display stats for titles (function)
function titlesearch(select) {
    
    //Get selected title
    var title = d3.select(`#title${select}-input option:selected`).text();
  
    //Pull in data 
    d3.json("link from app.py").then(function(data) {
      
      //Filter the data w/ title inputs
      var titledata = data.filter(d =>
        d.title == title);
      
        //Add html to list stats for each title
        //Select div for stats
        var titletron = d3.select(`#ts${select}`)

        // Use `.html("") to clear any existing metadata
        titletron.html("");

        // Use `Object.entries` to add each key and value pair to the panel
        Object.entries(data).forEach(([key, value]) =>
        metadataid.append("h4").text(`${key} : ${value}`));

      }).catch(error => console.log(error)); 

    };

//Display title 1 stats
d3.select("#button1").on("click", titlesearch(1))

//Display title 2 stats
d3.select("#button2").on("click", titlesearch(2))