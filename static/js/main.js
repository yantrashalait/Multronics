(function($) {
  'use strict';
$(document).ready(function(){

  $('.sh_hd_megamenu').click(function(){
    $(".toggle_openmenu_nav").slideToggle('fast');
  })

  $('body').click(function(e){
    if(!($(e.target).is(".sh_hd_megamenu"))){
          $(".toggle_openmenu_nav").slideUp('fast');
    }


  });

      $('.mainslider_caro').owlCarousel({
        loop:true,
        margin:10,
        dots:true,
        autoplay:true,
        autoplayTimeout:5000,
        autoplayHoverPause:true,
        responsive:{
            0:{
                items:1
            },
            600:{
                items:1
            },
            1000:{
                items:1
            }
        }
    })

    $('.mainslider2_caro').owlCarousel({
        loop: true,
        rewind: true,
        responsiveClass: true,
        nav: false,
        autoplay:true,
        autoplayTimeout:5000,
        smartSpeed: 500,
        dots: true,
        responsive : {
            992 : {
                items: 1
            },

            768 : {
                items: 1
            },

            576 : {
                items: 1
            },

            0 : {
                items: 1
            }
        }
    });

    $('.featured_caro').owlCarousel({
        loop: false,
        rewind: true,
        responsiveClass: true,
        nav: true,
        smartSpeed: 500,
        dots: false,
        navText: ['<i class="fa fa-angle-left" aria-hidden="true"></i>', '<i class="fa fa-angle-right" aria-hidden="true"></i>'],
        responsive:{
            0:{
                items:1
            },
            600:{
                items:3
            },
            1000:{
                items:4
            }
        }
    })
    $('.thumimg_caro').owlCarousel({
        loop: false,
        rewind: true,
        responsiveClass: true,
        nav: true,
        smartSpeed: 500,
        dots: false,
        navText: ['<i class="fa fa-angle-left" aria-hidden="true"></i>', '<i class="fa fa-angle-right" aria-hidden="true"></i>'],
        responsive:{
            0:{
                items:1
            },
            600:{
                items:2
            },
            1000:{
                items:3
            }
        }
    })
    $('.brand_caro').owlCarousel({
        loop: false,
        rewind: true,
        responsiveClass: true,
        nav: true,
        smartSpeed: 500,
        dots: false,
        margin:30,
        navText: ['<i class="fa fa-angle-left" aria-hidden="true"></i>', '<i class="fa fa-angle-right" aria-hidden="true"></i>'],
        responsive:{
            0:{
                items:2
            },
            600:{
                items:3
            },
            1000:{
                items:6
            }
        }
    })


    var newarrv_height = $('.mainslider_holder').outerHeight();
    $('.newarrivals_itms').css({'height': (newarrv_height/4) + 'px'})




// for header dropdowns

    $('.drpdwn_cls').click(function(){
        $(this).parent().hide()
    })

    $('body').click(function(e){
        if($(e.target).is('.fabclick')){
            $('.fav_drp').toggle()
        }else if($(e.target).is('.cartclick') || $(e.target).is('.waitclick') || $(e.target).is('.hd_notofi') || $(e.target).is('.hd_usr_prof') ){
            if($('.fav_drp').is(':visible')){
                $('.fav_drp').hide()
            }
        }

        if($(e.target).is('.cartclick')){
            $('.cart_drp').toggle()
        }else if($(e.target).is('.fabclick') || $(e.target).is('.waitclick') || $(e.target).is('.hd_notofi') || $(e.target).is('.hd_usr_prof') ){
            if($('.cart_drp').is(':visible')){
                $('.cart_drp').hide()
            }
        }

        if($(e.target).is('.waitclick')){
            $('.wait_drp').toggle()
        }else if($(e.target).is('.fabclick') || $(e.target).is('.cartclick') || $(e.target).is('.hd_notofi') || $(e.target).is('.hd_usr_prof') ){
            if($('.wait_drp').is(':visible')){
                $('.wait_drp').hide()
            }
        }

        if($(e.target).is('.hd_notofi')){
            $('.notifi_drp').toggle()
        }else if($(e.target).is('.fabclick') || $(e.target).is('.cartclick') || $(e.target).is('.waitclick') || $(e.target).is('.hd_usr_prof') ){
            if($('.notifi_drp').is(':visible')){
                $('.notifi_drp').hide()
            }
        }

    })



    $('.resp_srch').click(function(){
        $('.rsp_srch_bx_hldr').slideToggle();
    })

    $('.rsp_srch_close').click(function(){
        $('.rsp_srch_bx_hldr').slideUp();
    })




    // for slide menu


    $('.clk_show_dh_catlist').each(function(){
        $(this).click(function(){
            $(this).siblings('.pg_links_cat').toggle()
            $(this).toggleClass('open')
        })
    })

    $('.resp_tggl_main_menu').click(function(){
        $('.mb_slide_meu').addClass('mob_menu_open')
        $('.mb_slide_menu_back').show()
    })

    $('.mb_sld_hide').click(function(){
        $('.mb_slide_meu').removeClass('mob_menu_open')
        $('.mb_slide_menu_back').hide()
    })



    $(window).on('resize',function() {
    var hdheight =  $('.main_header').outerHeight()
    $('.contentspacer').css({'height' : hdheight + 'px'})
    }).trigger('resize');


    /* Product Details Image Slider */
    $('.pdetails-largeimages').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        dots: false,
        fade: true,
        asNavFor: '.pdetails-thumbs'
    });

    $('.pdetails-thumbs:not(.pdetails-thumbs-vertical)').slick({
        slidesToShow: 4,
        slidesToScroll: 1,
        asNavFor: '.pdetails-largeimages',
        arrows: true,
        dots: false,
        focusOnSelect: true,
        vertical: false
    });


    /* Product Details Zoom */
    $('.pdetails-imagezoom').lightGallery({
        selector: '.pdetails-singleimage'
    });


    // for height of product details contents

    var heightOfPdetailsImg = $('.pdetails-images').outerHeight()
    $('.pdetails_details').css({'min-height' : heightOfPdetailsImg + 'px'})

});// document ready


$(window).scroll(function(){
    var scroll__ = $(window).scrollTop();
    if(scroll__ > 10){
        $('.req__item').slideUp()
    }else{
        $('.req__item').slideDown();
    }
})

})(window.jQuery);
