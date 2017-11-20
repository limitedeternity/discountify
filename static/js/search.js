"use strict";

$(document).ready(function() {

  var images = $(".image");
  var fadeinCalled = false;

  var searchReveal = function() {
    if  ( $("#searchInput").is(":visible") ) {
      $("#searchInput").focus();
    }
  }

  setInterval(searchReveal, 150)

  var inputChecker = function() {
    if ( $("#searchInput").val().length > 0 ) {
      searchInput();
      fadeinCalled = false;

    } else {
      if (!fadeinCalled) {
        images.each( function(element) {
          $(this).parent().fadeIn();
          fadeinCalled = true;
        });
      }
    }
  }

  setInterval(inputChecker, 200);

  var searchInput = function() {
    var value = $("#searchInput").val().toLowerCase();

    images.each( function(element) {
      var searchParams = $(this).attr("data-search").split(", ");
      var matches = false;

      searchParams.forEach( function(param) {
        if ( param.startsWith(value) ) {
          matches = true;
        }
      });

      if ( !matches && value != '') {
        $(this).parent().fadeOut();

      } else if (matches) {
        $(this).parent().fadeIn();
      }

    });
  }

});
