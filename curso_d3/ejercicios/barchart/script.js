
var w = 500;
var h = 2000;

var svg = d3.select("body")
    .append("svg")
    .attr("width", w)
    .attr("height", h);

    var dataset = null;
    d3.csv("cars.csv", 
	function (cars) {
	    dataset = cars;
	    var weights = dataset.map(function(d){
					 return parseInt(d['weight (lb)']);});

	    /**
	     * Adaptado al alto del SVG
	     */
	    var barWidth = h / weights.length;

	    svg.selectAll('.bar')
		.data(weights)
	      .enter()
		.append('rect')
		.attr('class', 'bar')
		.attr('y', function(d,i) {return i*barWidth;})
		.attr('width', function(d){return d * 0.05;})
		.attr('height', barWidth);

       });
