
function getFormData() {
	const form = document.getElementById("prediction-form");
	const inputs = [...form.getElementsByTagName("input")]
		.filter(i => i.type == "range")
		.reduce((a,b) => {
			a[b.name] = `${(parseFloat(b.value)*100).toFixed(4)}%`;
			return a;
		},{});
	return inputs;
}

function updateStatus(new_status = "None") {
	// Updates the "status" section of the results
	const span = document.getElementById("prediction-status");
	span.textContent = new_status;
}

function updateResults(preds = {}) {
	// Updates the values in the prediction tables
	const set = document.getElementById("pred-pct-set");
	const ver = document.getElementById("pred-pct-ver");
	const vir = document.getElementById("pred-pct-vir");
	set.textContent = preds['setosa'] || "Unknown";
	ver.textContent = preds['versicolor'] || "Unknown";
	vir.textContent = preds['virginica'] || "Unknown";
}

async function postData(url, data) {
	const response = await fetch(url,{
		method: "POST",
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(data)
	});
	return response.json();
}

function handleSuccess(r) {
	updateResults(r.result);
}

function handleError(r) {
	console.error(r);
}

function checkForResults(rid = "") {
	fetch(`/api/get-result/${rid}`)
		.then(r => r.json())
		.then(r => {
			console.log("Checking results...");
			const stat = r.status;
			updateStatus(stat);
			if (stat == "SUCCESS")
				handleSuccess(r);
			else if (stat == "error" || stat == "FAILURE")
				handleError(r);
			else
				setTimeout(() => checkForResults(rid), 100);
		});
}

function makePrediction() {
	// Called by form prediction button.
	// Sends initial post request & gets result id.
	// Waits & polls api until result complete (updating status)
	// If successful, writes results to the table.
	// If unsuccessful, writes error message.
	console.log("Starting prediction...");
	const data = getFormData();
	console.log("Data:");
	console.log(data);

	updateStatus("Predicting...");
	
	// Send data as POST request
	postData("/api/predict",{'input-data':data})
		.then(data => data['result-id'])
		.then(rid => checkForResults(rid));	
}



