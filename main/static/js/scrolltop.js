

window.onscroll = function(e) {
   var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
   if (scrollTop > 500) {
     document.querySelector('#scroll-top').style.hidden = false;
   } else {
     document.querySelector('#scroll-top').style.hidden = true;
   }
};

