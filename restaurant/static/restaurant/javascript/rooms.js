var modal = document.getElementById('modal');
var alamo = document.getElementById('alamo');
var capis = document.getElementById('capis');
var jose = document.getElementById('jose');
var espada = document.getElementById('espada');
var terrace = document.getElementById('terrace');
var a = "alamo";
    alef = "6%";
var c = "capis";
    clef = "23%";
var j = "jose";
    jlef = "40%";
var e = "espada";
    elef = "57%"
var t = "terrace";
    tlef = "75%";

alamo.addEventListener('click', function(){displayImg(a, alef);});
capis.addEventListener('click', function(){displayImg(c, clef);});
jose.addEventListener('click', function(){displayImg(j, jlef);});
espada.addEventListener('click', function(){displayImg(e, elef);});
terrace.addEventListener('click', function(){displayImg(t, tlef);});


function displayImg(imgPref, position){
  modal.style.backgroundImage= 'url(/static/restaurant/img/' + imgPref + '.jpg)';
  modal.style.display='block';
}


window.addEventListener('scroll', function(e){
    modal.style.display="none";
    console.log("It worked");
});
