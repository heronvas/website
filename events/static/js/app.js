$(window).scroll(function(){
  $(".top").css("opacity", 1 - $(window).scrollTop() / 600);
});
$(window).scroll(function(){
  $(".mid").css("opacity", 1.7 - $(window).scrollTop() / 1000);
});
