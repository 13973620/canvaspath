function drawlinechart(chartid, xnum, data) {
    var wd = $(chartid).width();
    var wh = $(chartid).height();
    var margin = { top: 20, left: 60, bottom: 50, right: 20 };
    var height = wh - margin.top - margin.bottom,
        width = wd - margin.left - margin.right;
    var svg = d3.select(chartid).append("svg")
        .attr("width", (width + margin.left + margin.right) + "px")
        .attr("height", (height + margin.top + margin.bottom) + "px")
        .append('g')
        .attr("transform", "translate(${margin.left}, ${margin.right})");
    var x = d3.scaleBand().rangeRound([0, width]).padding(0.1),
        y = d3.scaleLinear().rangeRound([height, 0]);
    var g = svg.append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


    var line = d3.line()
        .x(function (d) {
            return x(d.timestamp);
        })
        .y(function (d) {
            return y(d.yvalue);
        })

    x.domain(data.map(function (d) {
        return d.timestamp;
    }));

    y.domain([0, d3.max(data, function (d) {
        return d.yvalue;
    })]);
    g.append("g")
        .attr("class", "axis axis--y")
        .attr("transform", "translate(0," + height + ")")
        .attr("dy", "0.71em")
        .attr("fill", "#000")
        .call(d3.axisBottom(x).ticks(xnum));

    g.append("g")
        .attr("class", "axis axis--y")
        .call(d3.axisLeft(y))
        .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", "0.71em")
        .attr("text-anchor", "end")
        .text("yvalue");

    g.append("path")
        .datum(data)
        .attr("class", "line")
        .attr("d", line);

    g.selectAll("circle")
        .data(data)
        .enter().append("circle")
        .attr("class", "circle")
        .attr("cx", function (d) {
            return x(d.timestamp);
        })
        .attr("cy", function (d) {
            return y(d.yvalue);
        })
        .attr("r", 4);
}

