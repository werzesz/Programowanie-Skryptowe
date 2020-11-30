var storage = window.localStorage;
var lastLine = 0;

function split(text){
    var array = [];
    var startOfLine = 0;
    var endOfLine = 0;
    var i = 0;

    while (i < text.length) {
        if (text.charCodeAt(i)==10) {
            
            endOfLine = i;

            var x = text.substring(startOfLine, endOfLine);
            array.push(x);
            startOfLine = endOfLine + 1;
        }
        i++;
    }

    return array;
}


//SAME CYFRY
function numbers(text, checkBoxValue) {
    var str = "";
    var splitArray = split(text);
    var array = [];
    //Jeśli checkBox nie jest zaznaczony zerujemy Storage
    if (checkBoxValue == false){
    storage.clear();
    lastLine = 0;
    }

    for (var i=0; i<splitArray.length; i++) {
        
            if (localStorage.getItem(splitArray[i]) == null) {
                localStorage.setItem(splitArray[i], i+lastLine+1);
            }
            else {
                var element = localStorage.getItem(splitArray[i]);
                var newElement = `${element}, ${i+lastLine+1}`;
                localStorage.setItem(splitArray[i], newElement);
            }
    }

    
    for (var j = 0; j < localStorage.length; j++) {
        var key = localStorage.key(j);
        var value = localStorage.getItem(key);
        str = `${str} ${key} ${value}`;
        console.log(key + " " + value);
    }
    lastLine = lastLine + i;
    return str;
    
}

//SAME LITERY
function letters(text, checkBoxValue) {

    var splitArray = split(text);
       

    if (checkBoxValue == false){
        storage.clear();
    }

    for (var i=0; i<splitArray.length; i++) {
        
        if (localStorage.getItem(splitArray[i]) == null) {
            localStorage.setItem(splitArray[i], 1);
        }
        else {
            var element = localStorage.getItem(splitArray[i]);
            var newElement = parseInt(element)+1;
            localStorage.setItem(splitArray[i], newElement);
        }
}
    
    for (var j = 0; j < localStorage.length; j++) {
        var key = localStorage.key(j);
        var value = localStorage.getItem(key);
        console.log(key + " " + value);
    }

}


function counter() {
    var text = document.forms[0].elements[0].value;
    var checkBoxValue = document.getElementById("Check");


    if (checkBoxValue.checked == true) {
        checkBoxValue = true;
    } else {
        checkBoxValue = false;

    }


    if (!isNaN(parseInt(text[0]))) {
        numbers(text, checkBoxValue);
    }
    else{
        letters(text, checkBoxValue);
    }

}

