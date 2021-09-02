$(document).ready(function(){
    var mouseX, mouseY;
    var ww = $( window ).width();
    var wh = $( window ).height();
    var traX, traY;
    $(document).mousemove(function(e){
      mouseX = e.pageX;
      mouseY = e.pageY;
      traX = ((4 * mouseX) / 300) + 150;
      traY = ((4 * mouseY) / 300) + 120;
      console.log(traX);
      $(".title").css({"background-position": traX + "%" + traY + "%"});
    });
  });