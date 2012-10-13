$(document).ready(function(){
  // Reset Font Size
  var originalFontSize = $('.ajustarFont').css('font-size');
  $(".resetFont").click(function(){
  	$('.ajustarFont').css('font-size', originalFontSize);
  });
  // Increase Font Size
  $(".increaseFont").click(function(){
  	var currentFontSize = $('.ajustarFont').css('font-size');
 	var currentFontSizeNum = parseFloat(currentFontSize, 10);
    var newFontSize = currentFontSizeNum*1.2;
	$('.ajustarFont').css('font-size', newFontSize);
	return false;
  });
  // Decrease Font Size
  $(".decreaseFont").click(function(){
  	var currentFontSize = $('.ajustarFont').css('font-size');
 	var currentFontSizeNum = parseFloat(currentFontSize, 10);
    var newFontSize = currentFontSizeNum*0.8;
	$('.ajustarFont').css('font-size', newFontSize);
	return false;
  });
});