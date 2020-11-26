var result = window.prompt();
console.log(typeof(result));
console.log(result);


function typeOfElements() {
    var text = document.forms[0].elements[0].value;
    var number = document.forms[0].elements[1].value;

    alert(text + ", " + number);
    
    console.log(typeof(text))
    console.log(typeof(number))
}
