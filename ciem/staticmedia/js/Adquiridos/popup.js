var w = $(this).width()/ 2+document.body.scrollTop();
var h = $(this).height()/2+document.body.scrollLeft();
   
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
   obj.style.left = x + theLeft + 'px' ;
   obj.style.top = y + theTop  + 'px' ;
   setTimeout("placeIt('pop')",500);
}
window.onscroll = setTimeout("placeIt('pop')",500);


