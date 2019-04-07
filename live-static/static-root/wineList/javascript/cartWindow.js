var cartImg= document.getElementById('cart-img');
var cartWindow= document.getElementById('cart-window');
var closeWindow= document.getElementById('closebtn');

cartImg.addEventListener('click', showWindow);
closeWindow.addEventListener('click', hiddeWindow);

function showWindow(){
  cartWindow.style.display='block';
}
function hiddeWindow(){
  cartWindow.style.display='none';
}
