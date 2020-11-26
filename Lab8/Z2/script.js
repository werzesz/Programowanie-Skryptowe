"use strict";
var mainSum = 0;

//Suma cyfr
function numbers(text) {
    var summ = 0;
    var x;
    var i;
    for (i = 0; i < text.length; i++) { 

        if (Number.isInteger(parseInt(text[i]))) {
            summ = summ + parseInt(text[i])
        }
    }
    return summ;

}

//Suma liter
function letters(text) {
    var summ = 0;
    var x;
    var i;
    for (i = 0; i < text.length; i++) { 
        x = parseInt(text[i])
        if (isNaN(x)) {
            summ = summ + 1
        }
    }
    return summ;
}

function summ(text) {
    var first = parseInt(text[0]); 
    var x;
    var i;
    var j;
    if (Number.isInteger(parseInt(first))){

            for (j = text.length - 1; j >= 0; j--) {
                x = parseInt(text.substring(0, j + 1))  
                
                if (Number.isInteger(parseInt(x))) {
                    mainSum = mainSum + x;
                    
                    return mainSum; 
                }
            }
    }
    
    return mainSum;  

}

var text;
var k = 0;
text = prompt("Podaj tekst: ");
while ( text != null){
    
    
    var sumNum = numbers(text);          
    var sumLet = letters(text);
    summ(text);
   
    console.log(sumLet + ", " + sumNum + ", " + mainSum);  
    text = prompt("Podaj tekst: ");    

}


mainSum = 0;
