function predict() {
    const data = {
        disease: document.querySelector("select").value,
        features: [
            parseFloat(document.getElementById("pregnancies").value),
            parseFloat(document.getElementById("glucose").value),
            parseFloat(document.getElementById("bp").value),
            parseFloat(document.getElementById("skin").value),
            parseFloat(document.getElementById("insulin").value),
            parseFloat(document.getElementById("bmi").value),
            parseFloat(document.getElementById("dpf").value),
            parseFloat(document.getElementById("age").value)
        ]
    };

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(data => {
        console.log(data);
        alert("Prediction: " + data.prediction);
    })
    .catch(err => {
        console.error(err);
    alert("Prediction: " + data.prediction +"\nRisk Probability: " + (data.probability * 100).toFixed(2) + "%");
    });
}