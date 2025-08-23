var b = null;
$( '.carousel-frame ul' ).on( 'mousemove', function(e) {
    var container = $(this).parent();
    var container2 = $(".custom-scroll-bar");
    console.log(container2);
    if ((e.pageX - container.offset().left) < container.width() / 2) {
        var direction = function() {
            container.animate( {scrollLeft: '-=600'}, 1500, 'linear', direction );
            container2.animate( {scrollLeft: '-=600'}, 2800, 'linear', direction );
        }
        if ((b == false) || (b == null)) {
            b = true;
            container.stop( true ).animate( {scrollLeft: '-=600'}, 1500, 'linear', direction );
            container2.stop( true ).animate( {scrollLeft: '-=600'}, 2800, 'linear', direction );
        }
    } else {
        var direction = function() {
            container.animate( {scrollLeft: '+=600'}, 1500, 'linear', direction );
            container2.animate( {scrollLeft: '+=600'}, 2800, 'linear', direction );
        }
        if ((b == true) || (b == null)) {
            b = false;
            container.stop( true ).animate( {scrollLeft: '+=600'}, 1500, 'linear', direction );
            container2.stop( true ).animate( {scrollLeft: '+=600'}, 2800, 'linear', direction );
        }
    }
}).on ( 'mouseleave', function() {
    var container = $(this).parent();
    container.stop( true );
    var container2 = $(".custom-scroll-bar");
    container2.stop( true );
    b = null;
});