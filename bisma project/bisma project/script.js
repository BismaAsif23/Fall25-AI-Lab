document.getElementById("predictForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const data = {
    number_of_peak: parseFloat(document.getElementById("number_of_peak").value),
    Age: parseFloat(document.getElementById("Age").value),
    Length_of_cycle: parseFloat(document.getElementById("Length_of_cycle").value),
    Estimated_day_of_ovulution: parseFloat(document.getElementById("Estimated_day_of_ovulution").value),
    Length_of_Leutal_Phase: parseFloat(document.getElementById("Length_of_Leutal_Phase").value),
    Length_of_menses: parseFloat(document.getElementById("Length_of_menses").value),
    Height: parseFloat(document.getElementById("Height").value),
    Weight: parseFloat(document.getElementById("Weight").value),
    BMI: parseFloat(document.getElementById("BMI").value),
    Mean_of_length_of_cycle: parseFloat(document.getElementById("Mean_of_length_of_cycle").value),
    Menses_score: parseFloat(document.getElementById("Menses_score").value)
  };

  try {
    const res = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });

    const json = await res.json();
    document.getElementById("result").innerHTML =
      `Result: <b>${json.result}</b> (Code: ${json.prediction})`;

  } catch (error) {
    document.getElementById("result").innerHTML =
      "Error connecting to API. Make sure backend is running.";
  }
});
