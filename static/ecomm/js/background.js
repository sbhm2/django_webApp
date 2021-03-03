document.addEventListener("DOMContentLoaded", function(event) { 
    //do work
    console.log("doc ready");
    changeBackground();
  });

function changeBackground() {
    console.log("this is from javascript");
    var colors = ['aliceblue', 'antiquewhite', 'azure'];
    var random_color = colors[Math.floor(Math.random() * colors.length)];
    document.getElementById('ecomm_list').style.backgroundColor = random_color;
}