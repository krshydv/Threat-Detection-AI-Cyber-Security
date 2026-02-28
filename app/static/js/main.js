function displayPredictionResult(predictionCounts) {
    const resultContainer = document.getElementById('result');
    const chartContainer = document.getElementById('chartContainer');

    // Clear previous results
    resultContainer.innerHTML = '';
    chartContainer.innerHTML = '<canvas id="resultChart"></canvas>';

    // Format counts as a table
    let table = '<table><thead><tr><th>Threat Type</th><th>Count</th></tr></thead><tbody>';
    const labels = [];
    const data = [];

    for (const [label, count] of Object.entries(predictionCounts)) {
        table += `<tr><td>${label}</td><td>${count}</td></tr>`;
        labels.push(label);
        data.push(count);
    }
    table += '</tbody></table>';

    resultContainer.innerHTML = table;

    // Render pie chart
    const ctx = document.getElementById('resultChart').getContext('2d');
    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                label: 'Threats',
                data: data,
                backgroundColor: [
                    '#1abc9c', '#3498db', '#9b59b6', '#e67e22', '#e74c3c',
                    '#f1c40f', '#2ecc71', '#34495e', '#95a5a6'
                ]
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom'
                },
                title: {
                    display: true,
                    text: 'Prediction Breakdown'
                }
            }
        }
    });
}
