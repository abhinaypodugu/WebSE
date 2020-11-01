// =============================================
// Parallax Init
// =============================================

jQuery(window).bind('load', function() {
    parallaxInit();
});

function parallaxInit() {
    jQuery('.parallax').each(function() {
        jQuery(this).parallax("30%", 0.3);
    });
}

function parallax() {
    var scrollPosition = $(window).scrollTop();
    $('#parallax').css('top', (0 - (scrollPosition * 0.3)) + 'px'); // bg image moves at 30% of scrolling speed
    $('#hero').css('opacity', ((100 - scrollPosition / 2) * 0.01));
}


	jQuery(document).ready(function($){

		/*	Parallax
		================================================== */

		$(window).on('scroll', function(e) {
			parallax();
		});

		/*	Wow Anim
		================================================== */
		new WOW().init();

		/*	Local Scroll
		================================================== */

		jQuery('.navbar').localScroll({
			offset: -80,
			duration: 500
		});

		/*	Active Menu
		================================================== */

		jQuery(function() {
			var sections = jQuery('section');
			var navigation_links = jQuery('nav a');
			sections.waypoint({
				handler: function(direction) {
					var active_section;
					active_section = jQuery(this);
					if (direction === "up") active_section = active_section.prev();
					var active_link = jQuery('nav a[href="#' + active_section.attr("id") + '"]');
					navigation_links.parent().removeClass("active");
					active_link.parent().addClass("active");
					active_section.addClass("active-section");
				},
				offset: '35%'
			});
		});

		/*	Gallery
		================================================== */
			$('#gallery').magnificPopup({
				delegate: 'a',
				type: 'image',
				tLoading: 'Loading image #%curr%...',
				mainClass: 'mfp-img-mobile',
				gallery: {
					enabled: true,
					navigateByImgClick: true,
					preload: [0, 1] // Will preload 0 - before current, and 1 after the current image
				},
				image: {
					tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
					titleSrc: function(item) {
						return item.el.attr('title') + '<small></small>';
					}
				}
			});


		/*	Bootstrap Carousel
		================================================== */

		jQuery('.carousel').carousel()


	});

  $('.alert').alert()
  //
  // function pherror(){
  //   var pherror = document.getElementById('pherror')
  //   var number = document.getElementById('phone')
  //   if(number.length!=10)
  // }
