$("#slidingBottles").on("scroll", function() {
  $(".slide").css({
    "background-position": $(this).scrollLeft()/6-100+ "px 0"
  });
});
