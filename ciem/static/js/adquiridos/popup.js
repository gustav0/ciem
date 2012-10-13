var w = $(this).width();
var h = $(this).height();
   
   //Centra el popup   
   x = (w/2) - (400/2);
   y = (h/2) - (300/2);

function setVisible(obj)
{
   obj = document.getElementById(obj);
   obj.style.visibility = (obj.style.visibility == 'visible') ? 'hidden' : 'visible';
}
function placeIt(obj)
{
   obj = document.getElementById(obj);
   if (document.documentElement)
   {
      theLeft = document.documentElement.scrollLeft;
      theTop = document.documentElement.scrollTop;
   }
   else if (document.body)
   {
      theLeft = document.body.scrollLeft;
      theTop = document.body.scrollTop;
   }
   var screenTop = $(document).scrollTop();
   theLeft += x;
   theTop += y;
   obj.style.left = theLeft + 'px' ;
   obj.style.top = y + screenTop + 'px' ;
   setTimeout("placeIt('pop')",500);
}
window.onscroll = setTimeout("placeIt('pop')",500);


