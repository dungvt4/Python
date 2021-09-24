function changeColor() {
	document.getElementById('paragraph1').style.color = 'green';
    document.getElementById('paragraph2').style.color = 'yellow';
    document.getElementById('paragraph3').style.color = 'red';
}


function changeBgColor(color) {
	document.body.style.backgroundColor = color;
}


function copyContent(par1, par2) {
	document.getElementById(par1).innerHTML = document.getElementById(par2).innerHTML; 
}


function changeFontSize(x) {
	var els = document.getElementsByClassName('par');
    for (i=0;i<els.length;i++) {
    	els[i].style.fontSize=x + "px";
    }
}


function increaseFontSize(id) {
	var el = document.getElementById(id);
    var fontSize = Number(window.getComputedStyle(el).getPropertyValue('font-size').match(/\d+/)[0]);
    if (fontSize > 30) {
    	alert('font size ko vuot qua 30');
        return;
    }
    el.style.fontSize = fontSize + 1 + "px";
}


function decreaseFontSize(id) {
	var el = document.getElementById(id);
    var fontSize = Number(window.getComputedStyle(el).getPropertyValue('font-size').match(/\d+/)[0]);
    if (fontSize < 10) {
    	alert('font size ko nho hon 10');
        return;
    }
    el.style.fontSize = fontSize - 1 + "px";
}