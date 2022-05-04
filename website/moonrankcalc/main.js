const getResult = () => {
    let score = document.getElementById('score').value;
    let time = document.getElementById('time').value;

    if(document.getElementsByTagName('input').value==""){
        alert("Please Enter Some Value");
    }
    let total = parseFloat(score) + (parseFloat(time) - 100) ;
    let percentage = (total * 100) / 200;

    if (percentage >= 90) {
        document.getElementById("grade").innerHTML = "Master Chief";
    }
    else if (percentage >= 80) {
        document.getElementById("grade").innerHTML = "Chief Master Sergeant";

    }
    else if (percentage >= 60) {
        document.getElementById("grade").innerHTML = "Master Sergeant";

    }
    else if (percentage >= 40) {
        document.getElementById("grade").innerHTML = "Sergeant";

    }
    else if (percentage >= 20) {
        document.getElementById("grade").innerHTML = "Specialist";

    }
    else {
        document.getElementById("grade").innerHTML = "No Rank";

    }


    document.getElementById('percentage').innerHTML = percentage;
    document.getElementById('total').innerHTML = total;
}// JavaScript Document